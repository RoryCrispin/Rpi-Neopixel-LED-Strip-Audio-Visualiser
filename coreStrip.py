import _rpi_ws281x as ws
from neopixel import *
import coreRGB


class LedStrip(object):
    def __init__(self, LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT,
                 LED_BRIGHTNESS):
        self.length = LED_COUNT
        self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA,
                                       LED_INVERT, LED_BRIGHTNESS)
        self.strip.begin()

    def output(self):
        self.strip.show()

    def write_canvas(self, canvas):
        index=0 #TODO: TEST CODE
        for i in canvas.pixels:
            self.strip.setPixelColor(index, i.colour.neoColour())
            #self.strip.setPixelColor(index, i.read_neocolour)
            #self.strip.setPixelColor(index, canvas.pixels[index].colour.neoColour)
            index = index+1
        self.output()


# LED strips exist as a chain of objects, from individual RGBLEDs >
# Groups of LEDs > Canvases/Pixels > Physical strip
# Canvases sit between LED groups and the physical LED strips - allowing for
# filters to be placed over led groups before outputting, eg hue transforms,
# kaleidoscopes, motions and so on.


class LedGroup(object):
    def __init__(self, groupid=0, length=None, strip=None ):
        self.ledArray = []
        self.populate()
        self.groupid = groupid
        if length is None and strip is not None:
            self.length = strip.length
        else:
            self.length = length

    def populate(self):
        for i in self.length:
            self.ledArray[i] = RgbLED(self.groupid)


class RgbLED(object):
    def __init__(self, group):
        self.colour = coreRGB.rgbColour(0, 0, 0)
        self.group = group

    def set_colour(self, color):
        self.colour = color

    def turn_off(self):
        self.colour = coreRGB.rgbColour(0, 0, 0)
