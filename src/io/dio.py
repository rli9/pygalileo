from galileo_config import DIO_MAPPINGS
from gpio import Gpio


'''
Dio represents digital IO of Galileo board
'''
class Dio(Gpio):
    def __init__(self, arduino_id):
        if isinstance(arduino_id, int):
            arduino_id = "IO%d" % arduino_id

        pin = DIO_MAPPINGS[arduino_id]
        pin.select()

        Gpio.__init__(self, pin.gpio_linux_id)
