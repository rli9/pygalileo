from mux_selector import MuxSelector


'''
GpioPin class represents underlying GPIO pin of Galileo board
- Pin may need to be enabled through mux selector if it shares HW resource w/ another pin
  e.g. GPIO pin 50 (IO0) is muxed w/ UART0_RXD
'''
class GpioPin(object):
    def __init__(self, gpio_linux_id, mux_seletors={}):
        self.gpio_linux_id = gpio_linux_id
        self.mux_seletors = mux_seletors

    def select(self):
        for (key, value) in self.mux_seletors.items():
            mux_selector = MuxSelector(key, value)
            mux_selector.select()

