import coreStrip
import coreRGB


class Canvas(object):
    def __init__(self, length=None, strip=None):
        self.pixels = []
        if length is None and strip is not None:
            self.length = strip.length
        else:
            self.length = length
        for i in self.length:
            self.pixels[i] = CanvasPixel()

    def set_pixel(self, i, colour):
        self.pixels[i].set_colour(colour)


class CanvasPixel(object):
    def __init__(self):
        self.color = coreRGB.rgbColour(0, 0, 0)

    def set_colour(self, colour):
        self.colour = colour

    def read_colour(self):
        return self.colour


