class Pin(object):
    def __init__(self, linux_id, mux_seletors={}):
        self.linux_id = linux_id
        self.mux_seletors = mux_seletors

PINS = {'IO0' : Pin(50, {40: 1}),
        'IO1' : Pin(51, {41: 1}),
        'IO2' : Pin(32, {31: 1}),
        'IO3' : Pin(18, {30: 1}),
        'IO4' : Pin(28),
        'IO5' : Pin(17),
        'IO6' : Pin(24),
        'IO7' : Pin(27),
        'IO8' : Pin(26),
        'IO9' : Pin(19),
        'IO10': Pin(16, {42: 1}),
        'IO11': Pin(25, {43: 1}),
        'IO12': Pin(38, {54: 1}),
        'IO13': Pin(39, {55: 1}),
        'IO14': Pin(44, {37: 1}),
        'IO15': Pin(45, {36: 1}),
        'IO16': Pin(46, {23: 1}),
        'IO17': Pin(47, {22: 1}),
        'IO18': Pin(48, {21: 1}),
        'IO19': Pin(49, {20: 1}),
        'A0'  : Pin(0, {37: 0}),
        'A1'  : Pin(1, {36: 0}),
        'A2'  : Pin(2, {23: 0}),
        'A3'  : Pin(3, {22: 0}),
        'A4'  : Pin(4, {21: 0}),
        'A5'  : Pin(5, {20: 0})}
