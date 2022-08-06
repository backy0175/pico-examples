from machine import Pin
from time import sleep

from PushButton import Debounced


# Callback function
def pressButton(button):
    print("pressed ", button)
    

# Use GPIO 11, 12, 13    
p1 = Debounced(11, Pin.PULL_DOWN)
p2 = Debounced(12, Pin.PULL_DOWN)
p3 = Debounced(13, Pin.PULL_DOWN)


# request irq and assign callback function
p1.debouncedIRQ(pressButton, Pin.IRQ_RISING)
p2.debouncedIRQ(pressButton, Pin.IRQ_RISING)
p3.debouncedIRQ(pressButton, Pin.IRQ_RISING)


# loop
while True:
    print("waiting...")
    sleep(10)
