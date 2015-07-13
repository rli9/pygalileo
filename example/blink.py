from pyquark.io.dio import Dio
import logging
import time

if __name__ == '__main__':
    log = logging.getLogger('pyquark')
    log.setLevel(logging.INFO)
    #FIXME built in LED blink doesn't work
    led = Dio("LED")
    led.direction('out')

    while True:
        led.value(1)
        time.sleep(1)

        led.value(0)
        time.sleep(1)