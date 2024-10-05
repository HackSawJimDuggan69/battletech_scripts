After 134 hours of playtime, I\'ve completed a perfect Kerensky run with
211 days remaining. I believe someone who aggressively rerolls contracts
and knows what I know now could improve this time significantly. I\'d
like to give back to the community that has helped me so much. While
Python experience isn\'t required, it would be very helpful for setting
up these scripts.

**[GitHub Repository Link](https://github.com/HackSawJimDuggan69/battletech_scripts)**

### Installation Guide:

1.  **Download Python 3** (developed in 3.10, but any modern version
    should work).

2.  **Download the scripts** from the GitHub repository.

3.  *(Optional)* **Create a virtual environment**:

    -   Run *python -m venv .venv*
    -   Activate with *source .venv/bin/activate*

4.  **Install dependencies**:

    -   Run *pip install -r requirements.txt*

5.  **Execute scripts**:

    -   Use *python ./name-of-script* while the virtual environment is
        active.

### Resources:

-   *****complete_starmap.csv*****: I generated a comprehensive starmap
    using
    [BTStarSystems](https://github.com/OutlierSeeker/BTStarSystems), as
    many available starmaps are incomplete.
-   *****longest_path.py*****: Record your visited systems in
    *data/visited.txt* and set your current location in *start_node*.
    This script finds the longest path before revisiting a system. I
    used this frequently for charting my next moves.
-   *****bt_travelling_salesman.py*****: Attempts to find the globally
    optimal path across the map. It doesn\'t account for planet
    difficulty or reputation requirements, so focus on which planets to
    land on rather than strictly following the path.

In its current configuration, the path starts at **Fagerholm** and must
visit **160 systems within 1000 days**. I chose Fagerholm because a merc
company that can handle 3-skull missions should scale up rapidly. The
script collects **225 skulls** worth of missions.

**Planets to Land On:**

*\[\'Alamagordo\', \'Amu Darya\', \'Andarmax\', \'Balawat\', \'Barras\',
\'Bellatrix\', \'Buenos Aires\', \'Burton\', \'Calseraigne\',
\'Carmichael\', \'Chennai\', \'Columbine\', \'Daol\', \'Decatur\',
\'Desolate Plains\', \'Dicon\', \'Espia\', \'Fjaldr\', \'Frazer\',
\'Gangtok\', \'Gardnaus\', \'Hastur\', \'Horsham\', \'Ingonish\',
\'Itsbur\', \'Jacomarle\', \'Jacson\', \'Katla\', \'Kazu\', \'Kern\',
\'Leyda\', \'Lochmantle\', \'Lopez\', \'Lucknow\', \'Maldive\',
\'Mattisskogen\', \'Mendham\', \'Menke\', \'Midale\', \'Muridox\',
\'Mystras\', \'New Roland\', \'Niomede\', \'Non Diz\', \'Nukus\',
\'Ordino\', \'Paf\', \'Pilpala\', \'Principia\', \'Prix\', \'Qalzi\',
\'Quimberton\', \'Repulse\', \'Robsart\', \'Rosendal\', \'Shaun\',
\'Shaunavon\', \'Shiba\', \'Sindalin\', \'Taurus\', \'Victoria\',
\'Wrentham\', \'Yuris\', \'Zathras\'\]*

**Path Found by the Script:**

*\[\'Fagerholm\', \'Mattisskogen\', \'Katla\', \'Ingonish\', \'Xanthe
III\', \'Pernik\', \'Leyda\', \'Claybrooke\', \'Thurrock\', \'Hastur\',
\'Aquagea\', \'Salardion\', \'Viribium\', \'Hibuarius\', \'Joppa\',
\'Alloway\', \'Úr Cruinne\', \'Cygnus\', \'Chandan\', \'Spencer\',
\'Fronc\', \'Addasar\', \'Balawat\', \'Dainmar Majoris\', \"Cate\'s
Hold\", \'New Abilene\', \'Brixtana\', \'Early Dawn\', \'Cassilda\',
\'Zathras\', \'Alamagordo\', \'Cursa\', \'Lopez\', \'Aomen\',
\'Sadurni\', \'Calseraigne\', \'Naryn\', \'Rosendal\', \'Lurgatan\',
\'Shiba\', \'Dicon\', \'Nukus\', \'Pell\', \'Primus\', \'Krakatau\',
\'Lucknow\', \'Shaun\', \'Amu Darya\', \'Decatur\', \'Columbine\',
\'Victoria\', \'Valdives\', \'Merdal\', \'Midthun\', \'Fjaldr\',
\'Pojos\', \'Kazu\', \'Muridox\', \'Enkra\', \'Mangzhangdian\',
\'Guldra\', \'Gangtok\', \'Katinka\', \'Artru\', \'Regis Roost\',
\'Qalzi\', \'Girondas\', \'Brinton\', \'Brisbane\', \'Rollis\',
\'Horsham\', \'Yuris\', \'Frazer\', \'Sindalin\', \'Menke\', \'Jacson\',
\'Gardnaus\', \'Lochmantle\', \'Shaunavon\', \'Mendham\', \'Maldive\',
\'Weitinger\', \'Daol\', \'Wrentham\', \'Robsart\', \'Midale\',
\'Merlin\', \"MacLeod\'s Land\", \'New Vallis\', \'Lindsay\',
\'Merope\', \'Carmichael\', \'Mithron\', \'Renfield\', \'Jamestown\',
\'Landmark\', \'Burton\', \'Paf\', \'Pyrrhus\', \'Spitz\',
\'Camadeirre\', \'Taurus\', \'Flaum\', \'Ishtar\', \'Illiushin\',
\'Atreus Prime\', \'Desolate Plains\', \"Jansen\'s Hold\", \'Bromhead\',
\'Corodiz\', \'Zanzibar\', \'Non Diz\', \'Laconis\', \'Kern\',
\'Ichlangis\', \'Hurik\', \'Kimi\', \'Cavalor\', \'Renown\',
\'Sunnywood\', \'Payia\', \'Ghorepani\', \'Andarmax\', \'Jacomarle\',
\'New Roland\', \'Arn\', \"Liu\'s Memory\", \'Espia\', \'Sax\',
\'Pilpala\', \'Athna\', \'Principia\', \'Turin\', \'Kurvasa\', \'Prix\',
\'Bellatrix\', \'Quimberton\', \'Itsbur\', \'Ordino\', \'Buenos Aires\',
\'Niomede\', \'Barras\', \'Chennai\', \'Drozan\', \'Gunthar\',
\'Repulse\', \'Adrar\', \'Linhauiguan\', \'Detroit\', \'Appian\',
\'Sacromonte\', \'Rockwellawan\', \'Independence\', \'Tiverton\',
\'Portland\', \'Tarragona\', \'Peratallada\', \'Gaucin\', \'Argos\',
\'Mystras\', \'Ahlat\'\]*

### *auto-bt.py*:

This script saved me many hours. Tired of arriving at systems with no
contracts, I wrote a script to automate rerolling contracts.

-   **Usage**:

    -   Arrive at a new system and **do not** click on contracts.
    -   Run the script; it will navigate to contracts and check how many
        are available by analyzing pixel values.
    -   If the number of contracts is less than the threshold on line
        72, the script restarts BattleTech and repeats the process.

**Note**: This script may require adjustments to work on your setup.

-   **System Requirements**:

    -   Fast machine (I use Linux, but OS shouldn\'t matter).
    -   Steam positioned on the right half of a 4K display.

-   **Adjustments Needed**:

    -   Modify mouse positions and sleep timings.
    -   Monitor the script closely during initial runs.

I\'ve also included *****listener.py***** to help identify cursor
positions.

### Lessons Learned:

1.  **Mech surgery isn\'t necessary if you reroll contracts**.

    -   I avoided dismantling mechs for salvage and still had plenty.

2.  **Pro-Kurita and Steiner flashpoints are important**.

    -   The Hatchetman and first Heavy Metal flashpoints provide rare
        reputation.
    -   Most other flashpoints, including subsequent Heavy Metal ones,
        weren\'t necessary.

3.  **Consistent headshots with three Marauders **is possible****.

    -   With 40 morale per turn and an Inferno support mech:

        -   **Infernos** shut down the mech with the highest damage
            reduction.
        -   **First Marauder** kills the shutdown mech (+10 morale, 50
            total).
        -   **Second Marauder** kills the next target (-30, then +10
            morale, 30 total).
        -   **Third Marauder** kills the third target.

    -   Chance of killing all three mechs: (0.79)\^3≈49%.

4.  **Unequipped mechs are free difficulty **points****.

    -   Purchasing a full SLDF mech grants all its standard double heat
        sinks.

5.  **All pilots were Vanguards**.

    -   I only regretted during the Badlands defend base mission.

6.  **Used \"Beyond MAD - A Headshot Guide\" by Wayward Raven** for mech
    designs.

    -   [Guide
        Link](https://steamcommunity.com/sharedfiles/filedetails/?id=3144092217)

    -   **Early Game Lance**: Lights and mediums with max medium lasers
        (e.g., FS9-H, BJ-1, CN9-AL, ENF-4R).

    -   **Midgame Build**:

        -   Two MAD-3Rs: 3× UAC2++, 4× M Laser++, Jump Jets.
        -   One HGN-333: LRM70+++.
        -   One CP-10-HQ: LRM40+++.

    -   **Late Game Lance**:

        -   Three MAD-2Rs: UAC2++, 6× ERMLaser++, Jump Jets.
        -   One GRF-2N: 4× Inferno++, 2× Flamer++, 2× TAG++, 1× TTS+++
            (missile), Jump Jets.

7.  **Skip intro movies for faster loading**.

    -   Edit *Settings.json* in
        *\<path-to-game\>\\BattleTech_Data\\StreamingAssets\\data\\debug*.
    -   Set *disableSplashScreens* and *disableIntroMovie* to *true*.
    -   Especially useful when rerolling contracts.

Lastly I would like to thank the community once more, especially
/u/EdmonEdmon and /u/guitarcoder.
