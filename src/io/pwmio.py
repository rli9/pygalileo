from galileo_config import PWMIO_MAPPINGS
from gpio import Gpio
import logging

LOG = logging.getLogger(__name__)
LOG.addHandler(logging.StreamHandler())

class PwmIO(Gpio):
    def __init__(self, arduino_id):
        if isinstance(arduino_id, int):
            arduino_id = "PWM%d" % arduino_id

        pin = PWMIO_MAPPINGS[arduino_id]
        pin.select()

        self.pwm_linux_id = pin.pwm_linux_id

        Gpio.__init__(self, pin.gpio_pin.gpio_linux_id)

        self.period = 700000
        self.pwm_dir_name = "/sys/class/pwm/pwmchip0/pwm%s" % str(self.pwm_linux_id)

        LOG.info("%s > %s" % (str(self.period), "%s/period" % self.pwm_dir_name))
        with open("%s/period" % self.pwm_dir_name, "w") as f:
            f.write(str(self.period))

    def pwm(self, value):
        self.value(1)

        duty_cycle = int(round(((self.period * value) / 255)))

        LOG.info("%s > %s" % (str(duty_cycle), "%s/duty_cycle" % self.pwm_dir_name))
        with open("%s/duty_cycle" % self.pwm_dir_name, "w") as f:
            f.write(str(duty_cycle))

    def export(self):
        Gpio.export(self)

        # FIXME rli9 error handling is required
        # FIxME rli9 only export pwm when pwm() is called
        LOG.info("%s > %s" % (str(self.pwm_linux_id), "/sys/class/pwm/pwmchip0/export"))
        with open("/sys/class/pwm/pwmchip0/export", 'w') as f:
            f.write(str(self.pwm_linux_id))

        with open("/sys/class/pwm/pwmchip0/pwm%s/enable" % self.pwm_linux_id, 'w') as f:
            f.write("1")

    def unexport(self):
        try:
            LOG.info("%s > %s" % (str(self.pwm_linux_id), "/sys/class/pwm/pwmchip0/unexport"))
            with open("/sys/class/pwm/pwmchip0/unexport", 'w') as f:
                f.write(str(self.pwm_linux_id))
        except Exception as e:
            LOG.warning("%s" % e)

        Gpio.unexport(self)
