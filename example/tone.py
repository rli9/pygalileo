from pygalileo.arduino import *
import logging
import time

if __name__ == '__main__':
    log = logging.getLogger('pygalileo')
    log.setLevel(logging.INFO)

    pinMode(10, OUTPUT)

    digitalWrite(10, LOW)

    value = 0

    while True:
        analogyWrite(10, value)
        time.sleep(2)

        value = value + 50
        if value >= 255:
            value = 0
