#!/usr/bin/env python

""" hearbeat thread
Drives the led output (normally on GPIO12, pin 32)

usage:
To initialise...
    from strobeClass import Heartbeat
    hb = Heartbeat(<initial_bpms>)
(at this point the heart will start beating)

when you want to change the heartrate
    hb.set_hr(<new_bpm>)
"""

import pigpio
import time

from threading import Thread
from Queue import Queue, Empty

from sevenseg import spi_update, spi_init


class Heartbeat:

    def __init__(self, default_heartrate):

        self.pi = pigpio.pi()

        self.pwm_pin = 12
        self.strobe_pin = 21
        self.pi.set_mode(self.strobe_pin, pigpio.OUTPUT)

        self.bpm = default_heartrate

        self._q = Queue()

        self.time_step = 60.0/(self.bpm*40)

        self.pi.hardware_PWM(self.pwm_pin, 0, 0)

        spi_init()

        def set_brightness(value):
            self.pi.hardware_PWM(self.pwm_pin, 38000, value*10000)

        def _do_heartbeat(queue):
            while True:
                self.pi.write(self.strobe_pin,1)
                for v in range(0,101,5):
                    while not queue.empty():
                        self.bpm = queue.get_nowait()
                        self.time_step = 60.0/(self.bpm*40)
                        spi_update(self.bpm)
                    set_brightness(v)
                    time.sleep(self.time_step)
                self.pi.write(self.strobe_pin,0)
                for v in range(100,0,-5):
                    while not queue.empty():
                        self.bpm = queue.get_nowait()
                        self.time_step = 60.0/(self.bpm*40)
                        spi_update(self.bpm)
                    set_brightness(v)
                    time.sleep(self.time_step)

        self._t = Thread(target = _do_heartbeat,
                args = (self._q,))
        self._t.daemon = True
        self._t.start() #start collecting new hearbeats

    def set_hr(self, new_hr):
        self._q.put(new_hr)

    def tidyup(self):
        self.pi.set_mode(self.pwm_pin, pigpio.OUTPUT)
        self.pi.write(self.pwm_pin, 1)

