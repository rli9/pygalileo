from pin import PINS
from gpio import MuxSelector


class I2c(object):
    def __init__(self):
        self.bus_id = 0

        sda_pin = PINS['I2C_SDA']
        scl_pin = PINS['I2C_SCL']

        sda_pin.select()
        scl_pin.select()

    def value(self):
        #FIXME consider to open the file once in init, and seek to beginning to read every time
        with open("/sys/bus/iio/devices/iio:device0/in_voltage%d_raw" % self.linux_id, 'r') as f:
            return f.readline().rstrip('\r\n')
