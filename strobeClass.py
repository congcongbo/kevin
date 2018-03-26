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

import pigpio, os, time

from threading import Thread
from Queue import Queue, Empty

from sevenseg import spi_update, spi_init

from heartLeds import set_brightness, init_brightness

class Heartbeat:

    def __init__(self, default_heartrate):

        self.pi = pigpio.pi()

        self.strobe_pin = 21
        self.pi.set_mode(self.strobe_pin, pigpio.OUTPUT)

        self.bpm = default_heartrate

        self._q = Queue()

        self.time_step = 60.0/(self.bpm*40)

        init_brightness()
        spi_init()

        def _do_heartbeat(queue):
            while True:
                os.system('/usr/bin/aplay /home/pi/Development/kevin/lub.wav 2>/dev/null &')
                for v in range(0,181,15):
                    while not queue.empty():
                        self.bpm = queue.get_nowait()
                        self.time_step = 60.0/(self.bpm*40)
                        spi_update(self.bpm)
                    set_brightness(v)
                    time.sleep(self.time_step)
                os.system('/usr/bin/aplay /home/pi/Development/kevin/dub.wav 2>/dev/null &')
                for v in range(180,256,15):
                    while not queue.empty():
                        self.bpm = queue.get_nowait()
                        self.time_step = 60.0/(self.bpm*40)
                        spi_update(self.bpm)
                    set_brightness(v)
                    time.sleep(self.time_step)
                for v in range(255,0,-15):
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

