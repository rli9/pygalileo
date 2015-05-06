from pygalileo.nxt.color_sensor import ColorSensor
import logging
import time
from pygalileo.io.i2c import I2c

if __name__ == '__main__':
    log = logging.getLogger('pygalileo')
    log.setLevel(logging.INFO)

    i2c = I2c()
    bus = i2c.smbus
    bus.write_byte_data(0x20, 0x29, 0x04)

    color_sensor = ColorSensor()

    while True:
        print color_sensor.aio.value()
        #color_sensor.i2c.smbus.write_byte(0x41, 0x00)

        #color_sensor.color()

        time.sleep(1)
