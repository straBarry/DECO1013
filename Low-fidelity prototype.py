
from microbit import *
import neopixel
from random import randint


# Setup the Neopixel strip on pin0 with a length of 8 pixels
np = neopixel.NeoPixel(pin0, 30)
display.show(Image.HAPPY)
sleep(1000)
display.clear()
temp = temperature()

# set up a logica value for loading time.
var = 1
while True:
    temp = temperature()

    if temp < 45 and var == 1:
        display.scroll(temp)
        for pixel_id in range(0, len(np)):
            red = 255
            green = 0
            blue = 0
            np[pixel_id] = (red, green, blue)
            np.show()
    elif temp == 40:
        var += 1

    while var >= 2:
        display.scroll(temp)
        if temp > 44:
            for pixel_id in range(0, len(np)):
                    red = 255
                    green = 0
                    blue = 0
                    np[pixel_id] = (red, green, blue)
                    np.show()
        elif (temp >=37 and temp <= 43):
            for pixel_id in range(0, len(np)):
                    red = 200
                    green = 100
                    blue = 0
                    np[pixel_id] = (red, green, blue)
                    np.show()
                    sleep(100)
        elif(temp >= 34 and temp <= 36):
            for pixel_id in range(0, len(np)):
                    red = 100
                    green = 200
                    blue = 0
                    np[pixel_id] = (red, green, blue)
                    np.show()
                    sleep(100)
        elif(temp >= 28 and temp <= 33):
            for pixel_id in range(0, len(np)):
                    red = 0
                    green = 100
                    blue = 255
                    np[pixel_id] = (red, green, blue)
                    np.show()
                    sleep(100)
        else:
            for pixel_id in range(0, len(np)):
                    red = randint(0, 60)
                    green = randint(0, 60)
                    blue = randint(0, 60)
                    np[pixel_id] = (red, green, blue)
                    np.show()
                    sleep(100)