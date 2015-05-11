from gpio import Gpio


class MuxSelector(Gpio):
    def __init__(self, linux_id, v):
        Gpio.__init__(self, linux_id)
        self.v = v

    def select(self):
        self.direction('out')
        self.value(self.v)
