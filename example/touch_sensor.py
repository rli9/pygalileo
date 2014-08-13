from pygalileo.nxt.touch_sensor import TouchSensor
import time

if __name__ == '__main__':
    touch_sensor = TouchSensor(10)

    while True:
        if touch_sensor.pressed():
            print "Pressed"
        else:
            print "Unpressed"

        time.sleep(0.5)
