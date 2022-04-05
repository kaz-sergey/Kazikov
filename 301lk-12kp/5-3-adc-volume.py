import RPi.GPIO as GPIO
import time
def dec2bin(number):
    return [int(bit) for bit in bin(number)[2:].zfill(8)]
def adc():
    signal = dec2bin(0)
    for i in range(8):
        signal[i] = 1
        GPIO.output(dac, signal)
        time.sleep(0.0005)

        if GPIO.input(comp) == 0:
            signal[i] = 0 
    b = ''.join(map(str, signal)) 
    v = int(round(int(b, 2) * 9 / 256, 0))
    volume = [int(i < v) for i in range(8)]
    print(f"Current voltage -> {round((int(b, 2)) * 3.3 / 256, 3)}")
    GPIO.output(leds, volume)
    GPIO.output(dac, 0)
dac = [10, 9, 11, 5, 6, 13, 19, 26][::-1]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)
try:
    while True:
        adc()
        time.sleep(0.01)
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()