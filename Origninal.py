
from microbit import *
import neopixel
from random import randint


# Setup the Neopixel strip on pin0 with a length of 30 pixels
np = neopixel.NeoPixel(pin1, 17)
display.show(Image.HAPPY)
sleep(1000)
display.clear()


# set up a logica value for loading time.

while True:
    raw = pin0.read_analog() * (3000 / 1023.0)
    temp_C = ((raw - 100.0) / 10) - 40.0

    temp = round(temp_C, 1)
    display.scroll(temp)


    if temp > 29:
            for pixel_id in range(0, len(np)):
                    red = 255
                    green = 0
                    blue = 0
                    np[pixel_id] = (red, green, blue)
                    np.show()


    elif(temp > 27 and temp < 28):
            for pixel_id in range(0, len(np)):
                    red = 100
                    green = 200
                    blue = 0
                    np[pixel_id] = (red, green, blue)
                    np.show()

    elif (temp > 25 and temp < 27):
            for pixel_id in range(0, len(np)):
                    red = 0
                    green = 100
                    blue = 255
                    np[pixel_id] = (red, green, blue)
                    np.show()

    elif (temp <25 ):
            for pixel_id in range(0, len(np)):
                    red = randint(0, 60)
                    green = randint(0, 60)
                    blue = randint(0, 60)
                    np[pixel_id] = (red, green, blue)
                    np.show()
                    sleep(10)