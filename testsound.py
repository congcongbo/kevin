import os, time
import pigpio

sense_pin = 21 # pin 40
pi=pigpio.pi()
pi.set_pull_up_down(sense_pin, pigpio.PUD_UP)

def wait_pin(target_state):
    while pi.read(sense_pin) != target_state:
        pass

#for n in range(0,5):
while True:
    wait_pin(1)
    os.system('/usr/bin/aplay /home/pi/Development/kevin/edited_session.wav &')
    wait_pin(0)
