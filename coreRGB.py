from neopixel import *

class rgbColour(object):
    red = 0
    green = 0
    blue = 0

    def __init__(self, red, green, blue, safe_brightness=False):
        # By default safe_brightness will block low duty cycles to keep fade
        # motions smooth

        if not safe_brightness:
            self.red = red
            self.green = green
            self.blue = blue
        else:
            self.safe_brightnessF(red, green, blue, safe_brightness)


    def neoColour(self):
        return Color(self.red, self.green, self.blue)

    def with_brightness(self, multiplier):
        return rgbColour(
            self.red *
            multiplier,
            self.green *
            multiplier,
            self.blue *
            multiplier)

    def safe_brightnessF(self, red, green, blue, safe_b):
        def set_min(val, minimum):
            if val < minimum:
                return minimum
            else:
                return val

        self.red = set_min(red, safe_b)
        self.blue = set_min(blue, safe_b)
        self.green = set_min(green, safe_b)


def hex_rgb_to_colour(r, g, b):
    hex_constant = 0.3921568627
    return rgbColour(int(hex_constant * r),
                     int(hex_constant * g),
                     int(hex_constant * b))


def hex_to_colour(v):
    if v[0] == '#':
        v = v[1:]
    assert (len(v) == 6)
    # return int(v[:2], 16), int(v[2:4], 16), int(v[4:6], 16)
    return hex_rgb_to_colour(int(v[:2], 16), int(v[2:4], 16), int(v[4:6], 16))


def percentageToHex(percentage):
    return 2.55 * percentage

def hexToPercentage(hex):
    return hex/255*100

# Preset Colours
red = rgbColour(100, 0, 0)
green = rgbColour(0, 100, 0)
blue = rgbColour(0, 0, 100)
orange = hex_rgb_to_colour(255, 127, 0)
yellow = hex_rgb_to_colour(255, 255, 0)
indigo = hex_rgb_to_colour(75, 0, 130)
lime = hex_rgb_to_colour(125,255,0)
ocean = rgbColour(0,54,100)
purple = rgbColour(100, 0, 100)
violet = purple
hot_pink = hex_rgb_to_colour(255,0,125)
aqua = rgbColour(0, 100, 100)
turquoise = rgbColour(0, 100, 30)

namedColours = {
    "red": red,
    "green": green,
    "blue": blue,
    "orange": orange,
    "yellow": yellow,
    "indigo": indigo,
    "lime": lime,
    "ocean": ocean,
    "purple": purple,
    "violet":purple,
    "hot pink": hot_pink,
    "aqua": aqua,
    "turquoise": turquoise
}


