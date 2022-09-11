# Wiring Schmatic
# GND to GND
# Signal to Signal Pin
# PWR to PWR
# 4.7K Resistor from PWR to Signal pin (Pull-up Resistor)
# Temperature is in Celsius

import machine, onewire, ds18x20, time


temp_pin = machine.Pin(22)
temp_sensor = ds18x20.DS18X20(onewire.OneWire(temp_pin))

roms = temp_sensor.scan()

print ('Found DS devices: ', roms)

while True:
    temp_sensor.convert_temp()
    time.sleep_ms(750)
    
    for rom in roms:
        print(rom)
        print(temp_sensor.read_temp(rom))
        
    time.sleep(5)