from galileo_config import I2C_MAPPINGS
from smbus import SMBus


class I2c(object):
    def __init__(self):
        self.bus_id = 0
        self.smbus = SMBus(self.bus_id)

        sda_pin = I2C_MAPPINGS['I2C_SDA']
        scl_pin = I2C_MAPPINGS['I2C_SCL']

        sda_pin.select()
        scl_pin.select()

    def value(self):
        vals = self.smbus.read_block_data(0x02, 0x42)
        print vals

I2C = I2c
