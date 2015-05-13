from pin import GPIO_PINS
from gpio import Gpio
import logging

LOG = logging.getLogger(__name__)
LOG.addHandler(logging.StreamHandler())

class Dio(Gpio):
    def __init__(self, arduino_id):
        if isinstance(arduino_id, int):
            arduino_id = "IO%d" % arduino_id

        pin = GPIO_PINS[arduino_id]
        pin.select()

        Gpio.__init__(self, pin.gpio_linux_id)