#from machine import Pin
from rgbLEDs import rgbLEDs
from time import sleep

class ledPatterns(rgbLEDs):
    
    def __init__ (self, pinNo, numLEDs):
        super().__init__(pinNo, numLEDs)
        self.sleep = 1 / numLEDs
        
    def __del__ (self):
        super().__del__()
        
    def pattern01(self):
        colors = [self.RED, self.GREEN, self.BLUE]
        
        for color in colors:
            #print(color)
            
            for end in reversed(range(1, self.n)):
                #print(end)
                self[0] = color
                self.write()
                sleep(self.sleep)
                
                for start in range(self.n - 1):
                    #print("{:d}, {:d}".format(start, end))
                    self.swap(start, start+1)
                    self.write()
                    sleep(self.sleep)
                    
            self[0] = color
            self.write()
            sleep(self.sleep * self.n)
        #sleep(self.sleep)
    
    
    def pattern02(self):
        colors = [self.RED, self.GREEN, self.BLUE]
        
        for color in colors:
            #print(color)
            
            for end in range(self.n - 1):
                #print(end)
                self[self.n - 1] = color
                self.write()
                sleep(self.sleep)
                
                for start in reversed(range(1, self.n)):
                    #print("{:d}, {:d}".format(start, end))
                    self.swap(start, start-1)
                    self.write()
                    sleep(self.sleep)
                    
            self[self.n - 1] = color
            self.write()
            sleep(self.sleep * self.n)
        #sleep(self.sleep)
            
            
    def pattern03(self, interval):
        self.fill((0, 0, 0))
        
        self[0] = (1, 0, 0) # 第１ピクセルを赤に設定
        self[2] = (0, 1, 0) # 第3ピクセルを緑に設定
        self[4] = (0, 0, 1) # 第5ピクセルを青に設定
        self[6] = (1, 0, 0) # 第１ピクセルを赤に設定
        self[8] = (0, 1, 0) # 第3ピクセルを緑に設定
        self[10] = (0, 0, 1) # 第5ピクセルを青に設定
        self.write()
        sleep(1)
        
        for i in range(10):
            self.shift(True)
            self.write()
            #sleep(self.sleep)
            sleep(interval)
            
        sleep(1)
        
        for i in range(10):
            self.shift(False)
            self.write()
            #sleep(self.sleep)
            sleep(interval)
            
            
    def pattern04(self):
        
        colors = [ self.RED, self.GREEN, self.YELLO, self.BLUE, self.PINK ]
        
        self.off()
        
        for color in colors:
            
            self[6] = color
            self.write()
            sleep(self.sleep)
            
            for i in range(self.n):
                self.shift()
                self.write()
                sleep(self.sleep)
                
            #sleep(1)
                
    def pattern05(self):
        
        colors = [ self.RED, self.GREEN, self.YELLO, self.BLUE, self.PINK]
        
        self.off()
        
        for i in range(self.n):
            self[i] = colors[int(i/3)]
        self.write()
        sleep(1)
        
        for i in range(self.n * 3):
            self.shift()
            self.write()
            sleep(self.sleep)
            
        sleep(1)
        
        for i in range(self.n * 3):
            self.shift(False)
            self.write()
            sleep(self.sleep)
            
            
    def pattern06(self):
        
        #colors = [ self.RED, self.GREEN, self.YELLO, self.BLUE, self.PINK, self.WHITE]
        colors = [ self.RED, self.RED, self.BLUE, self.BLUE, self.PINK, self.WHITE]
        
        self.off()
        
        for i in range(self.n):
            self[i] = colors[int(i/3)]
            
        self.write()
        sleep(1)
        
        for i in range(self.n / 2):
            self.flip(i)
            self.write()
            sleep(1)
            self.flip(i)
            self.write()
            sleep(1)
        