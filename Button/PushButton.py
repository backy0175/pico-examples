from machine import Pin
import utime

class Debounced(Pin):
    """Extend micropython basic class 'Pin' to support debounced IRQ"""
    
    def __init__ (self, id, pull=-1):
        super().__init__(id, Pin.IN, pull)
        self.lastPressed = 0
        self.func = None
        self.bouncer = 500  # default debouncing time[mSec]
        
        
    def __del__ (self):
            super().__del__()


    def callback(self, pin):
        """ internal callback function to take care bounce """
        
        now = utime.ticks_ms()
        if now - self.lastPressed > self.bouncer:
            self.lastPressed = now
            self.func(pin)


    def debouncedIRQ(self, func, trigger, bouncer = 500):
        """ debounced IRQ support function

            Args:
            func: callback function to be called
            trigger: IRQ trigger same as Pin triggers
            bouncer: debouncing time in mSec
        """
        self.func = func
        self.bouncer = bouncer
        self.irq(self.callback, trigger)
