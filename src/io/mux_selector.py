from gpio_raw import GpioRaw


class MuxSelector(GpioRaw):
    def __init__(self, linux_id, v):
        GpioRaw.__init__(self, linux_id)
        self.v = v

    def select(self):
        self.direction('out')
        self.value(self.v)
