import spidev
from time import sleep

spi = spidev.SpiDev()

def spi_init():
    global spi
    spi.close()
    spi.open(0, 0)
    spi.bits_per_word=8
    spi.max_speed_hz = 5000

    to_send = [0x0f, 0x00] # test mode off
    spi.xfer2(to_send)

    to_send = [0x09, 0xFF] # decode mode
    spi.xfer2(to_send)

    to_send = [0x0B, 0x02] # three digits
    spi.xfer2(to_send)

    to_send = [0x0C, 0x01] # shutdown -> normal mode
    spi.xfer2(to_send)

    to_send = [0x0A, 0x0F] # intensity
    spi.xfer2(to_send)

    to_send = [0x0B, 0x07] # scan limit
    spi.xfer2(to_send)

    for i in range(1,9): # blank all digits
        to_send = [i, 15]
        spi.xfer2(to_send)

def spi_update(value):
#    global spi

    to_send = [ 0x01, value % 10 ] # low digit
    spi.xfer2(to_send)

    to_send = [ 2, (value / 10)%10 ] # tens digit
    spi.xfer2(to_send)

    if value > 99:
        to_send = [ 3, (value /100) ] # hundreds digit
    else:
        to_send = [ 3, 0xF ] # blank the hundreds
    spi.xfer2(to_send)


if __name__ == "__main__":
    spi_init()
    for i in [70, 71 , 72, 102, 220, 70]:
        print i
        spi_update(i)
        sleep(1)
    spi.close()

