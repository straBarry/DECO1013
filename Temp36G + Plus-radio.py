from microbit import *
import neopixel
from random import randint
import radio


# Setup the Neopixel strip on pin0 with a length of 30 pixels
np = neopixel.NeoPixel(pin1, 30)
display.show(Image.HAPPY)
sleep(1000)
display.clear()
radio.on()


# Using tmp36G to measure tthe temp of water

while True:
    raw = pin0.read_analog() * (3000 / 1023.0)
    temp_C = ((raw - 100.0) / 10) - 40.0

    temp = round(temp_C, 0)
     3
    radio.send_number(temp)
    incoming = radio.receive()

    sleep(5)

    if temp > 60:
            for pixel_id in range(0, len(np)):
                    red = 255
                    green = 0
                    blue = 0
                    np[pixel_id] = (red, green, blue)
                    np.show()
    elif (temp >= 45 and temp <= 59):
            for pixel_id in range(0, len(np)):
                    red = 200
                    green = 100
                    blue = 0
                    np[pixel_id] = (red, green, blue)
                    np.show()
                    sleep(100)
    elif(temp >= 35 and temp <= 44):
            for pixel_id in range(0, len(np)):
                    red = 100
                    green = 200
                    blue = 0
                    np[pixel_id] = (red, green, blue)
                    np.show()
                    sleep(100)
    elif (temp > 25 and temp <= 35):
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