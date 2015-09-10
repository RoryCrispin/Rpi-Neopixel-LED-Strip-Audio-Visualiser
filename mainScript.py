import coreStrip
import coreRGB
import canvasHandler

def init_script():
        # LED strip configuration:
        LED_COUNT      = 300      # Number of LED pixels.
        LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
        LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
        LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
        LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
        LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
        return coreStrip.LedStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)

ledStrip = init_script()

canvas = canvasHandler.Canvas(strip=ledStrip)

for i in canvas.length:
    canvas.set_pixel(i, coreRGB.blue)

ledStrip.writeCanvas(canvas)