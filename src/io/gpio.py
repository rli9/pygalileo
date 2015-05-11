import types
import logging

LOG = logging.getLogger(__name__)
LOG.addHandler(logging.StreamHandler())


class Gpio(object):
    def __init__(self, linux_id, pwm_linux_id=None):
        self.linux_id = linux_id
        self.pwm_linux_id = pwm_linux_id

        try:
            self.unexport()
        except Exception as e:
            LOG.warning("%s" % e)

        self.export()

    def __getattr__(self, name):
        '''
        This automatically generates functions for
            direction(self, arg = None)
                arg: 'out', 'in' to write to direction file. None to read from direction file.

            drive(self, arg = None)
                arg: 'pullup', 'strong', 'pulldown', 'hiz' to write to drive file. None to read from drive file.

            value(self, arg = None)
                arg: non-None to write to value file. None to read from value file.
        '''
        if name.startswith('_'):
            raise AttributeError(name)

        def _attr(self, arg=None):
            file_name = "/sys/class/gpio/gpio%d/%s" % (self.linux_id, name)

            if arg is not None:
                LOG.info("%s > %s" % (str(arg), file_name))

                #FIXME rli9 low performance to open/close file everytime
                with open(file_name, 'w') as f:
                    f.write(str(arg))

                return self
            else:
                with open(file_name, 'r') as f:
                    return f.readline().rstrip('\r\n')

        _attr.__name__ = name

        setattr(self, name, types.MethodType(_attr, self))
        return getattr(self, name)

    def export(self):
        #FIXME rli9 error handling is required
        LOG.info("%s > %s" % (str(self.linux_id), "/sys/class/gpio/export"))
        with open("/sys/class/gpio/export", 'w') as f:
            f.write(str(self.linux_id))

        if self.pwm_linux_id is not None:
            LOG.info("%s > %s" % (str(self.pwm_linux_id), "/sys/class/pwm/pwmchip0/export"))

            #FIXME rli9 error handling is required
            #FIxME rli9 only export pwm when pwm() is called
            with open("/sys/class/pwm/pwmchip0/export", 'w') as f:
                f.write(str(self.pwm_linux_id))

            with open("/sys/class/pwm/pwmchip0/pwm%s/enable" % self.pwm_linux_id, 'w') as f:
                f.write("1")

    def unexport(self):
        try:
            if self.pwm_linux_id is not None:
                LOG.info("%s > %s" % (str(self.pwm_linux_id), "/sys/class/pwm/pwmchip0/unexport"))
                with open("/sys/class/pwm/pwmchip0/unexport", 'w') as f:
                    f.write(str(self.pwm_linux_id))
        except Exception as e:
            LOG.warning(e)

        LOG.info("%s > %s" % (str(self.linux_id), "/sys/class/gpio/unexport"))
        with open("/sys/class/gpio/unexport", 'w') as f:
            f.write(str(self.linux_id))
