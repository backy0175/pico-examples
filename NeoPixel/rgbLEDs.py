from machine import Pin
from neopixel import NeoPixel

class rgbLEDs(NeoPixel):
    """Extend micropython basic class 'NeoPixel' to support some useful functions"""
    
    
    """Color Codes"""
    RED = (1, 0, 0)
    GREEN = (0, 1, 0)
    BLUE = (0, 0, 1)
    YELLO = (1, 1, 0)
    PINK = (1, 0, 1)
    WHITE = (1, 1, 1)
    
    
    def __init__ (self, pinNo, numLEDs):
        """Constractor of rgbLEDs

        Args:
            pinNo (int): Number of GPIO
            numLEDs (int): Number of LEDs that will be supported
        """
        super().__init__(Pin(pinNo, Pin.OUT), numLEDs)

        
    def __del__ (self):
        """Destoractor of rgbLEDs"""
        self.off()
        super().__del__()

        
    def swap(self, i, j):
        """Swap LED Color

        Args:
            i (int) : index number of LED(from 0 to numLEDs - 1)
            j (int) : index number of LED(from 0 to numLEDs - 1)
        """
        
        temp = self[i]
        self[i] = self[j]
        self[j] = temp

        
    def flip(self, pos):
        """Flip LED Color

        Args:
            pos (int) : index number of LED to be start position    
        """
        
        pos1 = pos
        pos2 = pos - 1
        
        for i in range(self.n / 2):
            if pos1 >= self.n:
                pos1 = 0
            if pos2 < 0:
                pos2 = self.n - 1
            
            self.swap(pos1, pos2)
            
            pos1 = pos1 + 1
            pos2 = pos2 - 1
        
        
    def shift(self, bCW = True):
        """Shift LED Color ClockWise or Counter ClockWise

        Args:
            bCW (bool): True  = Shift ClockWise
                        False = Shift Counter ClockWise
        """
        if bCW:
            temp = self[self.n -1]
            for i in reversed(range(self.n -1)):
                self[i+1] = self[i]
            self[0] = temp
        else:
            temp = self[0]
            for i in range(self.n -1):
                self[i] = self[i+1]
            self[i+1] = temp

        
    def off(self):
        """Turn off all LEDs"""
        
        self.fill((0, 0, 0))
        self.write()