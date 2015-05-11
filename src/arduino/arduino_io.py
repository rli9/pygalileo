from pygalileo.io.dio import Dio
from pygalileo.io.pwmio import Pwmio

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

_DIOS = {}


def pinMode(pin, mode):
    if pin not in _DIOS:
        dio = Dio(pin)
        dio.direction(mode)
        _DIOS[pin] = dio
    else:
        dio = _DIOS[pin]
        dio.direction(mode)

def digitalWrite(pin, value):
    dio = _DIOS[pin]
    dio.value(value)

def digitalRead(pin):
    dio = _DIOS[pin]
    return dio.value()

def analogyWrite(pin, value):
    dio = _DIOS[pin]
    return dio.pwm(value)