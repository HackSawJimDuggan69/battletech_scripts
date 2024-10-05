from pynput.mouse import Button, Controller

from time import sleep

import pyautogui
import psutil

def get_pixel_values(points):
    """
    Returns the pixel values at the specified points using PyAutoGUI.

    :param points: A list of (x, y) tuples representing screen coordinates.
    :return: A dictionary with points as keys and RGB pixel values as values.
    """
    pixel_values = {}
    for point in points:
        # Get the pixel value at the specified point
        pixel = pyautogui.pixel(point[0], point[1])
        pixel_values[point] = pixel

    return pixel_values


def start_bt():
    mouse = Controller()
    mouse.position = (2617, 685)
    mouse.press(Button.left)
    mouse.release(Button.left)
    sleep(15)
    mouse.position = (913, 1496)
    mouse.press(Button.left)
    mouse.release(Button.left)
    sleep(0.5)
    mouse.position = (1387, 1585)
    mouse.press(Button.left)
    mouse.release(Button.left)
    sleep(20)
    mouse.position = (441, 1425)
    mouse.press(Button.left)
    mouse.release(Button.left)
    sleep(2)
    mouse.position = (1998, 1295)
    mouse.press(Button.left)
    mouse.release(Button.left)
    sleep(10)


if __name__ == '__main__':
    not_found = True
    while not_found:
        start_bt()

        # Define the points where you want to get the pixel values
        points = [
            (1550, 450),
            (1550, 600),
            (1550, 800),
            (1550, 950),
            (1550, 1100),
            (1550, 1220),
            (1550, 1380),
        ]

        # Get the pixel values
        pixels = get_pixel_values(points)

        total = 0
        for point, pixel in pixels.items():
            if pixel.red > 30 and pixel.green > 30 and pixel.blue > 30:
                total += 1
        print(total)
        if total >= 5:
            not_found = False
        else:
            for proc in psutil.process_iter():
                if 'BattleTech' == proc.name():
                    proc.kill()
            sleep(5)

