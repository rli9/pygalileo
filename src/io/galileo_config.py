from gpio_pin import GpioPin
from pwmio_pin import PwmIOPin

GPIO_PIN_MAPPINGS = {'50': GpioPin(50, {40: 1}),
                     '51': GpioPin(51, {41: 1}),
                     '32': GpioPin(32, {31: 1}),
                     '18': GpioPin(18, {30: 1}),
                     '28': GpioPin(28),
                     '17': GpioPin(17),
                     '24': GpioPin(24),
                     '27': GpioPin(27),
                     '26': GpioPin(26),
                     '19': GpioPin(19),
                     '16': GpioPin(16, {42: 1}),
                     '25': GpioPin(25, {43: 1}),
                     '38': GpioPin(38, {54: 1}),
                     '39': GpioPin(39, {55: 1}),
                     '44': GpioPin(44, {37: 1}),
                     '45': GpioPin(45, {36: 1}),
                     '46': GpioPin(46, {23: 1}),
                     '47': GpioPin(47, {22: 1}),
                     '48': GpioPin(48, {21: 1}),
                     '49': GpioPin(49, {20: 1}),
                     'LED': GpioPin(3), # FIXME rli9 galileo V1 specific, not sure for V2 yet
                     }

# FIXME rli9 is it better to mapping to arduino ID, e.g. PwmPin(3, GPIO_PIN_MAPPINGS["IO3"]
PWMIO_MAPPINGS = {'PWM3': PwmIOPin(3, GPIO_PIN_MAPPINGS["18"]), # IO3
                  'PWM5': PwmIOPin(5, GPIO_PIN_MAPPINGS["17"]), # IO5
                  'PWM6': PwmIOPin(6, GPIO_PIN_MAPPINGS["24"]), # IO6
                  'PWM9': PwmIOPin(1, GPIO_PIN_MAPPINGS["19"]), # IO9
                  'PWM10': PwmIOPin(7, GPIO_PIN_MAPPINGS["16"]), # IO10
                  'PWM11': PwmIOPin(4, GPIO_PIN_MAPPINGS["25"]) # IO11
                  }

DIO_MAPPINGS = {'IO0': GPIO_PIN_MAPPINGS['50'],
                'IO1': GPIO_PIN_MAPPINGS['51'],
                'IO2': GPIO_PIN_MAPPINGS['32'],
                'IO3': GPIO_PIN_MAPPINGS['18'],
                'IO4': GPIO_PIN_MAPPINGS['28'],
                'IO5': GPIO_PIN_MAPPINGS['17'],
                'IO6': GPIO_PIN_MAPPINGS['24'],
                'IO7': GPIO_PIN_MAPPINGS['27'],
                'IO8': GPIO_PIN_MAPPINGS['26'],
                'IO9': GPIO_PIN_MAPPINGS['19'],
                'IO10': GPIO_PIN_MAPPINGS['16'],
                'IO11': GPIO_PIN_MAPPINGS['25'],
                'IO12': GPIO_PIN_MAPPINGS['38'],
                'IO13': GPIO_PIN_MAPPINGS['39'],
                'IO14': GPIO_PIN_MAPPINGS['44'],
                'IO15': GPIO_PIN_MAPPINGS['45'],
                'IO16': GPIO_PIN_MAPPINGS['46'],
                'IO17': GPIO_PIN_MAPPINGS['47'],
                'IO18': GPIO_PIN_MAPPINGS['48'],
                'IO19': GPIO_PIN_MAPPINGS['49'],
                'LED': GPIO_PIN_MAPPINGS['LED'],
                }

AIO_MAPPINGS = {'A0': GpioPin(0, {37: 0}),
                'A1': GpioPin(1, {36: 0}),
                'A2': GpioPin(2, {23: 0}),
                'A3': GpioPin(3, {22: 0}),
                'A4': GpioPin(4, {21: 0}),
                'A5': GpioPin(5, {20: 0}),
                }

I2C_MAPPINGS = {'I2C_SDA': GpioPin(-1),
                'I2C_SCL': GpioPin(-1, {29: 0}),
                }

