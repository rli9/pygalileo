from galileo_config import AIO_MAPPINGS


'''
Aio represents analog IO of Galileo board
'''
class Aio(object):
    def __init__(self, arduino_id):
        if isinstance(arduino_id, int):
            arduino_id = "A%d" % arduino_id

        pin = AIO_MAPPINGS[arduino_id]
        pin.select()

        self.arduino_id = arduino_id
        self.linux_id = pin.linux_id

    def value(self):
        # FIXME consider to open the file once in init, and seek to beginning to read every time
        with open("/sys/bus/iio/devices/iio:device0/in_voltage%d_raw" % self.linux_id, 'r') as f:
            return f.readline().rstrip('\r\n')
