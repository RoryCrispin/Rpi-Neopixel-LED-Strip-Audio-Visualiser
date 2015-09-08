import time
import _rpi_ws281x as ws
from neopixel import *
import coreRGB

# LED strip configuration:
LED_COUNT      = 300      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)


# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
	strip.begin()


class ledStrip(object):
    def __init__(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS):
    self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
    self.strip.begin()
        
    def output(self):
        strip.show()

class canvas(object):
    def __init__(self, length):
        for i in length:
            self.pixels[i] = 


# LED strips exist as a chain of objects, from individual RGBLEDs>Groups of LEDs> Canvases> Physical strip
# Canvases sit between LED groups and the physical LED strips - allowing for filters to be placed over led groups before outputting, eg hue transformations, kaleidoscopes, motions and so on.
class ledGroup(object):
    def __init__(self, groupid = 0):
        
        self.ledArray = [] 
    def populate():
        for i in LED_COUNT:
            self.ledArray[i] = rgbLED(groupid)      

class rgbLED(object):
    def __init__(self, group):
        self.colour = coreRGB.rgbColour(0,0,0)
        self.group = group
    
    def setColour(self, color):
        self.colour = color
    
    def turnOff(self):
        self.colour = coreRGB.rgbColour(0,0,0)


