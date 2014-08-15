from pygalileo.io.gpio import Gpio
import logging
import time

if __name__ == '__main__':
    log = logging.getLogger('pygalileo')
    log.setLevel(logging.INFO)
#     #FIXME built in LED blink doesn't work
#     led_gpio = Gpio(13)
#     led_gpio.direction('out')
#
#     while True:
#         led_gpio.value(1)
#         time.sleep(1)
#
#         led_gpio.value(0)
#         time.sleep(1)

    gpio10 = Gpio(10)
    gpio11 = Gpio(11)

    gpio10.direction('out')
    gpio11.direction('out')

    gpio10.value(1)
    gpio11.value(0)

    time.sleep(1)
    gpio10.value(0)

    gpio10.unexport()
    gpio11.unexport()
