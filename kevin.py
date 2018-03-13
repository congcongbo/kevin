import sys

from nbstreamreader import NonBlockingStreamReader as NBSR
nbsr = NBSR(sys.stdin)

#constants
baseline_hr = 70
max_hr = 220
min_hr = 30
change_time = 3
effect_time = 5
recovery_time = 5

#variables
heart_rate = baseline_hr
qr_codes = []
target_rates = []
times_scanned = []

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
    "QR-Code:heroin": 'heroin'
}

all_target_hrs = {
    'attraction':175,
    'dinosaur':200,
    'banana':175,
    'nicotine':90,
    'exercise':120,
    'altitude':150,
    'ecstacy':120,
    'digitalis':50,
    'beta-blocker':60,
    'heroin':40
}

def get_code_and_time():
    if switcher.has_key(line.strip()):
	    qr_codes.append(code)
	    print(qr_codes)
	    import datetime
	    times_scanned.append(datetime.datetime.now().time()) #adds time at same index
	    print(times_scanned)
	    
def get_target_hr():
	if len(qr_codes) > 0:
		target_rates = [all_target_hrs[q] for q in qr_codes]
		print(target_rates)
		target_hr = max(target_rates)
		print(target_hr)
'''
def change_hr():
	while heart_rate - target_hr != 0:
		if target_hr > heart_rate:
			heart_rate += 1
		else:
			heart_rate -= 1
'''
		
while True:
    line=nbsr.readline(0.1)
    if not line:
        print(heart_rate),
        sys.stdout.flush()
    else:
        code = switcher.get(line.strip())
        print(code)
        scanned = True
        get_code_and_time()
        get_target_hr()
'''
        if target_hr > heart_rate:
	    heart_rate += 1
	else:
	    heart_rate -= 1
'''