import pigpio
import time

def bleep():
    pi = pigpio.pi()

    pi.hardware_PWM(18, 660, 500000)
    time.sleep(0.05)
    pi.hardware_PWM(18, 440, 500000)
    time.sleep(0.1)

    pi.hardware_PWM(18, 0, 0)
    pi.set_mode(18, pigpio.OUTPUT)
    pi.write(18, 1)

if __name__ == "__main__":
    bleep()
