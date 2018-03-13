from strobeClass import Heartbeat as Hb
import time

hb = Hb(72)

try:
    while True:
        for hr in range(70,220,5):
            print (hr)
            hb.set_hr(hr)
            time.sleep(5)

except KeyboardInterrupt:
    hb.tidyup()

#except:
#    print("Other error")
