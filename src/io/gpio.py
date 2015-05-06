from pin import PINS
from gpio_raw import GpioRaw


class Gpio(GpioRaw):
    def __init__(self, arduino_id):
        if isinstance(arduino_id, int):
            arduino_id = "IO%d" % arduino_id

        pin = PINS[arduino_id]
        pin.select()

        GpioRaw.__init__(self, pin.linux_id)
