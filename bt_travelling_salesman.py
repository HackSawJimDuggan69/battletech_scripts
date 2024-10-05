import pandas as pd
from pulp import (
    LpProblem,
    LpMaximize,
    LpVariable,
    LpBinary,
    lpSum,
    LpStatus,
    value,
    LpContinuous, getSolver
)

def main():
    adjacency_df = pd.read_csv("data/complete_starmap.csv")
    adjacency = {}

    for _, row in adjacency_df.iterrows():
        system = row.iloc[0]
        neighbors = [str(value) for value in row.iloc[1:] if pd.notnull(value)]
        adjacency[system] = neighbors

    skulls_df = pd.read_csv("data/systems.csv")
    skulls = {}
    jump_distance = {}

    for _, row in skulls_df.iterrows():
        system = row['Name']
        skulls[system] = row['Energy']
        jump_distance[system] = row['JumpDistance']

    systems = list(adjacency.keys())
    edges = [(i, j) for i in systems for j in adjacency[i]]

    # Include 'Start' in the list of systems
    systems_with_start = ['Start'] + systems

    # Define the model
    model = LpProblem("StarshipOptimization", LpMaximize)

    # Variables
    # Create x_edge variables for all possible edges (i,j)
    x_edge_keys = [(i, j) for i in systems_with_start for j in systems_with_start if i != j]
    x_edge = LpVariable.dicts("x_edge", x_edge_keys, cat=LpBinary)
    collection = LpVariable.dicts("y", systems, cat=LpBinary)
    planetfall = LpVariable.dicts("v", systems, cat=LpBinary)
    visit = LpVariable.dicts("w", systems, cat=LpBinary)
    end_node = LpVariable.dicts("end_node", systems, cat=LpBinary)

    # Objective
    model += lpSum(collection[i] * skulls[i] for i in systems), "TotalCollectedEnergy"

    # Constraints

    valid_edges = set()
    valid_edges.update([('Start', 'Fagerholm')])
    valid_edges.update(edges)

    # Time constraints
    travel_time = 3 * lpSum(x_edge[i, j] for (i, j) in valid_edges)
    landing_time = lpSum(planetfall[i] * (3 + jump_distance[i]) for i in systems)
    model += travel_time + landing_time <= 1000, "TotalTimeConstraint"

    # Must visit at least 160 systems (passing through or landing)
    model += lpSum(visit[i] for i in systems) >= 160, "MinVisitedSystems"

    # You can only collect energy if you land
    for i in systems:
        model += collection[i] <= planetfall[i], f"CollectIfLand_{i}"

    # You can only land if you visit
    for i in systems:
        model += planetfall[i] <= visit[i], f"LandIfVisit_{i}"

    # Starting constraints
    starting_systems = ['Fagerholm']
    model += lpSum(x_edge['Start', i] for i in starting_systems) == 1, "StartAtOneSystem"

    for i in systems:
        if i == 'Fagerholm':
            pass
        else:
            # Cannot start here
            model += x_edge['Start', i] == 0, f"NoStartEdgeTo_{i}"

    # Ensure exactly one end node
    model += lpSum(end_node[i] for i in systems) == 1, "OneEndNode"

    # Ensure edges to 'Start' are zero (no incoming edges to 'Start')
    for i in systems_with_start:
        if i != 'Start':
            model += x_edge[i, 'Start'] == 0, f"NoEdgeToStartFrom_{i}"

    # Set x_edge[i, j] == 0 for invalid edges
    for (i, j) in x_edge_keys:
        if (i, j) not in valid_edges:
            model += x_edge[i, j] == 0, f"InvalidEdge_{i}_{j}"

    # Flow conservation constraints
    for i in systems_with_start:
        incoming = lpSum(x_edge[j, i] for j in systems_with_start if j != i)
        outgoing = lpSum(x_edge[i, j] for j in systems_with_start if j != i)
        if i == 'Start':
            model += outgoing == 1, "StartNodeOutgoingOne"
        elif i in systems:
            model += incoming == outgoing + end_node[i], f"FlowConservation_{i}"

    # Ensure no outgoing edges from the end node
    for i in systems:
        for j in systems_with_start:
            if j != i:
                model += x_edge[i, j] <= (1 - end_node[i]), f"NoOutgoingFromEndNode_{i}_{j}"

    # Ensure that each visited system is connected by the path
    for i in systems:
        incoming_edges = lpSum(x_edge[j, i] for j in systems_with_start if j != i)
        outgoing_edges = lpSum(x_edge[i, j] for j in systems_with_start if j != i)
        model += visit[i] <= incoming_edges, f"VisitIfIncoming_{i}"
        model += visit[i] <= outgoing_edges, f"VisitIfOutgoing_{i}"

    # MTZ Subtour Elimination Constraints
    n = len(systems)
    # MTZ variables: Order in which each system is visited
    u = LpVariable.dicts("u", systems_with_start, lowBound=0, upBound=n, cat=LpContinuous)

    # Fix u['Start'] = 0
    model += u['Start'] == 0, "Order_Start"

    # Set bounds for u[i]
    for i in systems:
        model += u[i] >= 1, f"Order_LowerBound_{i}"
        model += u[i] <= n, f"Order_UpperBound_{i}"

    # MTZ constraints for edges from 'Start' to systems
    for i in systems:
        if ('Start', i) in valid_edges:
            model += u[i] >= 1 * x_edge['Start', i], f"Order_FromStart_{i}"

    # MTZ constraints for all valid edges between systems
    for (i, j) in valid_edges:
        if i != 'Start' and j != 'Start' and i != j:
            model += u[i] - u[j] + n * x_edge[i, j] <= n - 1, f"MTZ_{i}_{j}"

    model.solve(getSolver("HiGHS", timeLimit=60*60*24))

    # Results
    status = LpStatus[model.status]
    if status == 'Optimal' or status == 'Feasible':
        print("Optimal solution found.")
        total_skulls = value(model.objective)
        print("Total collected skulls:", total_skulls)

        visited_systems = [i for i in systems if value(visit[i]) > 0.5]
        print("Number of systems visited:", len(visited_systems))

        landed_systems = [i for i in systems if value(planetfall[i]) > 0.5]
        print("Number of systems landed on:", len(landed_systems))

        collected_skulls_systems = [i for i in systems if value(collection[i]) > 0.5]
        print("Systems where skulls were collected:", collected_skulls_systems)

        construct_path(x_edge)
    else:
        print("No optimal solution found. Status:", status)

def construct_path(x_edge):
    next_system_map = {}

    for (from_system, to_system), var in x_edge.items():
        if value(var) > 0.5:
            next_system_map[from_system] = to_system

    current_system = 'Start'
    path = []

    while True:
        if current_system in next_system_map:
            next_system = next_system_map[current_system]
            if next_system == 'Start' or next_system in path:
                break  # Prevent loops back to start or cycles
            path.append(next_system)
            current_system = next_system
        else:
            break

    print("Path taken by the starship:")
    print(path)

if __name__ == "__main__":
    main()
