import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, # type: ignore
    board.IO47,
    board.IO33, # type: ignore
    board.IO34, # type: ignore
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39,
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

# main loop
min_thr = 20000
count = 2000
arr = [min_thr + i * count for i in range(len(led_pins))]
while True:
    volume = microphone.value

    print(volume)

    for i in range(len(led_pins)):
        if volume > arr[i]:
            leds[i].value = True
        else:
            leds[i].value = False

    sleep(0.1)
