from mux_selector import MuxSelector


class GpioPin(object):
    def __init__(self, gpio_linux_id, mux_seletors={}):
        self.gpio_linux_id = gpio_linux_id
        self.mux_seletors = mux_seletors

    def select(self):
        for (key, value) in self.mux_seletors.items():
            mux_selector = MuxSelector(key, value)
            mux_selector.select()

GPIO_PINS = {'IO0': GpioPin(50, {40: 1}),
        'IO1': GpioPin(51, {41: 1}),
        'IO2': GpioPin(32, {31: 1}),
        'IO3': GpioPin(18, {30: 1}),
        'IO4': GpioPin(28),
        'IO5': GpioPin(17),
        'IO6': GpioPin(24),
        'IO7': GpioPin(27),
        'IO8': GpioPin(26),
        'IO9': GpioPin(19),
        'IO10': GpioPin(16, {42: 1}),
        'IO11': GpioPin(25, {43: 1}),
        'IO12': GpioPin(38, {54: 1}),
        'IO13': GpioPin(39, {55: 1}),
        'IO14': GpioPin(44, {37: 1}),
        'IO15': GpioPin(45, {36: 1}),
        'IO16': GpioPin(46, {23: 1}),
        'IO17': GpioPin(47, {22: 1}),
        'IO18': GpioPin(48, {21: 1}),
        'IO19': GpioPin(49, {20: 1}),
        'A0': GpioPin(0, {37: 0}),
        'A1': GpioPin(1, {36: 0}),
        'A2': GpioPin(2, {23: 0}),
        'A3': GpioPin(3, {22: 0}),
        'A4': GpioPin(4, {21: 0}),
        'A5': GpioPin(5, {20: 0}),
        'I2C_SDA': GpioPin(-1),
        'I2C_SCL': GpioPin(-1, {29: 0}),
        'LED': GpioPin(3),
        }

class PwmPin(object):
    def __init__(self, pwm_linux_id, gpio_pin):
        assert(pwm_linux_id is not None)

        self.gpio_pin = gpio_pin
        self.pwm_linux_id = pwm_linux_id

    def select(self):
        self.gpio_pin.select()
    
PWM_PINS = {'PWM3': PwmPin(3, GPIO_PINS["IO3"]),
            'PWM5': PwmPin(5, GPIO_PINS["IO5"]),
            'PWM6': PwmPin(6, GPIO_PINS["IO6"]),
            'PWM9': PwmPin(1, GPIO_PINS["IO9"]),
            'PWM10': PwmPin(7, GPIO_PINS["IO10"]),
            'PWM11': PwmPin(4, GPIO_PINS["IO11"])
            }  