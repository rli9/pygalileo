from pygalileo.io.i2c import I2c
from pygalileo.io.aio import Aio


class ColorSensor(object):
    def __init__(self):
        self.i2c = I2c()
        self.aio = Aio(2)

    def color(self):
        return self.i2c.value()
