from ledPatterns import ledPatterns

leds = ledPatterns(22, 12)  # Use GPIO22 and 12 LEDs

leds.off()

leds.pattern01()
sleep(1)

leds.pattern02()
sleep(1)

leds.pattern03(0.1)
sleep(1)

leds.pattern04()
sleep(1)

leds.pattern05()
sleep(1)

leds.pattern05()
sleep(5)

leds.off()
