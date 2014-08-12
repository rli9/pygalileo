class Pin(object):
    def __init__(self, linux_id, mux_seletors = {}):
        self.linux_id = linux_id
        self.mux_seletors = mux_seletors

Pins = {'IO0' : Pin(50, {40: 1}),
        'IO4' : Pin(28),
        'IO5' : Pin(17),
        'IO10': Pin(16, {42: 1}),
        'IO11': Pin(25, {43: 1}),
        'IO13': Pin(39, {55: 1})}