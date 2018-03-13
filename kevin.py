import sys

from nbstreamreader import NonBlockingStreamReader as NBSR
nbsr = NBSR(sys.stdin)

# functions to handle each case
def altitude():
    print "altitude"
    target_hr = 150

def attraction():
    print "attraction"

def unknownQR():
    print "oops"

switcher = {
    "QR-Code:altitude": altitude,
    "QR-Code:attraction": attraction,
    "QR-Code:dinosaur": dinosaur,
    "QR-Code:banana": banana,
    "QR-Code:nicotine": nicotine,
    "QR-Code:exercise": exercise,
    "QR-Code:altitude": altitude,
    "QR-Code:ecstacy": ecstacy,
    "QR-Code:digitalis": digitalis,
    "QR-Code:beta-blocker": beta-blocker,
    "QR-Code:heroin": heroin
}

code_target_hr = {
    'attraction':175
    'dinosaur':200,
    'banana':175,
    'nicotine':90,
    'exercise':120,
    'altitude':150,
    'ecstacy':120,
    'digitalis':50,
    'beta-blocker':60
    'heroin':40}

while True:
    line=nbsr.readline(0.1)
    if not line:
        print ".",
        sys.stdout.flush()
    else:
        switcher.get(line.strip(), unknownQR)()
        scanned = True


#constants
baseline_hr = 70
max_hr = 220
min_hr = 30
change_time = 3
effect_time = 5
recovery_time = 5

#state variables
heart_rate = baseline_hr
qr_codes = []
target_rates = []
times_scanned = []
code

heart_rate = baseline_hr
scanned = false
def scan:
	if scanned:
		qr_codes.append(code)
		import datetime
		times_scanned.append(datetime.datetime.now().time()) #adds time at same index
		scanned = false

def change_hr():
	while heart_rate - target_hr != 0:
		if target_hr > heart_rate:
			heart_rate += 1
		else:
			heart_rate -= 1

def scan_card:
	if len(qr_codes) > 0:
		target_rates = [code_target_hr[q] for q in qr_codes]
		target_hr = max(target_rates)
		change_hr
