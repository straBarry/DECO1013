from microbit import *
display.show(Image.HAPPY)
sleep(1000)
display.clear()

while True:
    raw = pin0.read_analog() * (3000 / 1023.0)
    temp_C = ((raw - 100.0) / 10) - 40.0

    temp= round(temp_C,2)
    display.scroll(temp)
    sleep(1000)