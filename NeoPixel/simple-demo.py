from machine import Pin
from neopixel import NeoPixel

# 12LED用の NeoPixel Ring を GPIO 22 で制御する
np = NeoPixelPin(22, Pin.OUT), 12)

np.fill((1, 1, 1))  # すべてのLEDを白に設定する
np.write()         # 全LEDにデータ書込み(点灯)
