from pin import PINS
from gpio import Gpio
import logging

LOG = logging.getLogger(__name__)
LOG.addHandler(logging.StreamHandler())

class Dio(Gpio):
    def __init__(self, arduino_id):
        if isinstance(arduino_id, int):
            arduino_id = "IO%d" % arduino_id

        pin = PINS[arduino_id]
        pin.select()

        Gpio.__init__(self, pin.gpio_linux_id, pin.pwm_linux_id)

        if self.pwm_linux_id is not None:
            self.period = 700000
            self.pwm_dir_name = "/sys/class/pwm/pwmchip0/pwm%s" % str(self.pwm_linux_id)

            LOG.info("%s > %s" % (str(self.period), "%s/period" % self.pwm_dir_name))
            with open("%s/period" % self.pwm_dir_name, "w") as f:
                f.write(str(self.period))

    def pwm(self, value):
        if self.pwm_linux_id is not None:
            self.value(1)

            duty_cycle = int(round(((self.period * value) / 255)))

            LOG.info("%s > %s" % (str(duty_cycle), "%s/duty_cycle" % self.pwm_dir_name))
            with open("%s/duty_cycle" % self.pwm_dir_name, "w") as f:
                f.write(str(duty_cycle))
