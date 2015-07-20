'''
PwmPin class represents underlying PWM pin of Galileo board
- PWM pin is currently reusing GPIO pin
'''
class PwmIOPin(object):
    def __init__(self, pwm_linux_id, gpio_pin):
        assert(pwm_linux_id is not None)

        self.gpio_pin = gpio_pin
        self.pwm_linux_id = pwm_linux_id

    def select(self):
        self.gpio_pin.select()
