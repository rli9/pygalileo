from pygalileo.arduino import *
import logging


if __name__ == '__main__':
    log = logging.getLogger('pygalileo')
    log.setLevel(logging.INFO)

    pinMode(10, OUTPUT)
    pinMode(11, OUTPUT)

    digitalWrite(10, HIGH)
    digitalWrite(11, LOW)

    delay(1000)
    digitalWrite(10, LOW)