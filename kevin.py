#run with zbarcam --prescale=640x480 -S*.disable -Sqrcode.enable | python kevin.py

from strobeClass import Heartbeat
    
import sys
import time

from nbstreamreader import NonBlockingStreamReader as NBSR
nbsr = NBSR(sys.stdin)

#constants
baseline_hr = 70
max_hr = 220
min_hr = 30
change_time = 3
effect_time = 25
recovery_time = 5
hb = Heartbeat(70)

#variables
heart_rate = baseline_hr
qr_codes = []
target_rates = []
times_scanned = []
target_hr = baseline_hr

heart_rate = baseline_hr
scanned = False

switcher = {
    "QR-Code:altitude": 'altitude',
    "QR-Code:attraction": 'attraction',
    "QR-Code:dinosaur": 'dinosaur',
    "QR-Code:banana": 'banana',
    "QR-Code:nicotine": 'nicotine',
    "QR-Code:exercise": 'exercise',
    "QR-Code:ecstacy": 'ecstacy',
    "QR-Code:digitalis": 'digitalis',
    "QR-Code:beta-blocker": 'beta-blocker',
    "QR-Code:heroin": 'heroin',
    "QR-Code:caffeine": 'caffeine'
}

all_target_hrs = {
    'attraction':160,
    'dinosaur':220,
    'banana':180,
    'nicotine':90,
    'exercise':140,
    'altitude':150,
    'ecstacy':120,
    'digitalis':50,
    'beta-blocker':60,
    'heroin':40,
    'caffeine':70
}

def get_code_and_time():
    global qr_codes
    global times_scanned
    if switcher.has_key(line.strip()):
	qr_codes.append(code)
	print(qr_codes)
	times_scanned.append(time.time()) #adds time at same index
	    
def get_target_hr():
    global target_rates
    global target_hr
    global times_scanned
    global qr_codes
    if len(qr_codes) > 0:
	target_rates = [all_target_hrs[q] for q in qr_codes]
	if target_rates[-1]<70:
            target_hr = min(target_rates)
	else:
            target_hr = max(target_rates)

def decrease_to_baseline():
    global target_hr
    global times_scanned
    global qr_codes
    global target_rates
    global effect_time
    if len(times_scanned) !=0:
        if time.time()-times_scanned[-1]>effect_time:
            print('decreasing to baseline')
            target_hr = baseline_hr
            times_scanned = []
            qr_codes = []
            change_hr()

def change_hr():
    global heart_rate
    global target_hr
    if heart_rate - target_hr != 0:
	if target_hr > heart_rate:
            heart_rate += 1
        else:
	    heart_rate -= 1

while True:
    line=nbsr.readline(0.1)
    if not line:
        print(heart_rate),
        sys.stdout.flush()
        change_hr()
        hb.set_hr(heart_rate)
        decrease_to_baseline()
    else:
        code = switcher.get(line.strip())
        print(code)
        scanned = True
        get_code_and_time()
        get_target_hr()
        print(times_scanned)
