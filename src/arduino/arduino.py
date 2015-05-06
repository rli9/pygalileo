from pygalileo.io.gpio import Gpio
import time


def delay(ms):
    time.sleep(ms / 1000.0)

'''
Defining Digital Pins modes: INPUT, INPUT_PULLUP, and OUTPUT
'''
INPUT = 'in'
OUTPUT = 'out'

'''
Defining Pin Levels: HIGH and LOW
'''
HIGH = 1
LOW = 0

gpios = {}


def pinMode(pin, mode):
    if pin not in gpios:
        gpio = Gpio(pin)
        gpio.direction(mode)
        gpios[pin] = gpio
    else:
        gpio = gpios[pin]
        gpio.direction(mode)

def digitalWrite(pin, value):
    gpio = gpios[pin]
    gpio.value(value)

def digitalRead(pin):
    gpio = gpios[pin]
    return gpio.value()
