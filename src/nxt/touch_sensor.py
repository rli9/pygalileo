from pygalileo.io.gpio import Gpio


class TouchSensor(object):
    def __init__(self, arduino_id):
        self.gpio = Gpio(arduino_id)
        self.gpio.direction('in')

    def pressed(self):
        '''
        return value: True if pressed, False if unpressed
        '''
        return self.gpio.value() == '0'
