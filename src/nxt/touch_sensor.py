from pyquark.io.dio import Dio


class TouchSensor(object):
    def __init__(self, arduino_id):
        self.dio = Dio(arduino_id)
        self.dio.direction('in')

    def pressed(self):
        '''
        return value: True if pressed, False if unpressed
        '''
        return self.dio.value() == '0'
