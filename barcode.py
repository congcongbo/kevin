# python barcode processing
# run wuth zbarcode, as follows:

# zbarcam -S*.disable -Sqrcode.enable | python barcode.py



import sys

from nbstreamreader import NonBlockingStreamReader as NBSR
nbsr = NBSR(sys.stdin)

# functions to handle each case
def altitude():
    print ("altitude")

def attraction():
    print ("attraction")

def unknownQR():
    print ("oops")

switcher = {
    "QR-Code:altitude": altitude,
    "QR-Code:attraction": attraction
}

while True:
    line=nbsr.readline(0.1)
    if not line:
        print ("."),
        sys.stdout.flush()
    else:
        switcher.get(line.strip(), unknownQR)()

