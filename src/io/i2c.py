from pin import PINS
from smbus import SMBus


#FIXME do we name i2c as I2c or I2C
class I2c(object):
    def __init__(self):
        self.bus_id = 0
        self.smbus = SMBus(self.bus_id)

        sda_pin = PINS['I2C_SDA']
        scl_pin = PINS['I2C_SCL']

        sda_pin.select()
        scl_pin.select()

    def value(self):
        vals = self.smbus.read_block_data(0x02, 0x42)
        print vals

I2C = I2c
