import os


def info():
    print("Static path: ", STATIC_PATH)
    print("Display Width: ", 1440, "Display Hight: ", 900)


# System
STATIC_PATH = os.path.realpath(os.path.dirname(os.path.realpath(__file__)) + '/static')
DISPLAY_WIDTH, DISPLAY_HIGHT = 1440, 900

# Colours
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)
PURPLE = (128, 0, 128)
