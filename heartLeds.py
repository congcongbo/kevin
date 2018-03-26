import pigpio
from time import sleep
pi = pigpio.pi()
pin = 18

def init_brightness():
    pi.set_mode(pin, pigpio.OUTPUT)
    pi.set_PWM_dutycycle(pin, 0) # use default range 0..255
    pi.set_PWM_frequency(pin, 125)

def set_brightness(b):
    ''' Set the LEDs to value between 0 (off) and 255 (full)
    '''
    pi.set_PWM_dutycycle(pin, b) # use default range 0..255

def tidyup():
    pi.set_mode(pin, pigpio.OUTPUT)
    pi.write(pin, 0)

if __name__=="__main__":
    init_brightness()
    while True:
        for i in range(0,255,10):
            set_brightness(i)
            sleep(0.2)