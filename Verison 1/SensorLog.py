# Wiring Schmatic
# GND to GND
# Signal to Signal Pin
# PWR to PWR
# 4.7K Resistor from PWR to Signal pin (Pull-up Resistor)
# Temperature is in Celsius

import machine, onewire, ds18x20, time, json

def SensorInitialize():
    
    temp_pin = machine.Pin(22)
    temp_sensor = ds18x20.DS18X20(onewire.OneWire(temp_pin))
    
    return temp_sensor
    
def SensorLog(temp_sensor, display=False):

    log = {}
    roms = temp_sensor.scan()
    rtc = machine.RTC()
    
    if roms:
        #print ('Found DS devices: ', roms)

        temp_sensor.convert_temp()

        for rom in roms:
            timeStamp = rtc.datetime()
            stamp = "%04d-%02d-%02d %02d:%02d:%02d"%(timeStamp[0:3] + timeStamp[4:7])
            log[stamp] = temp_sensor.read_temp(rom)
        return log
    return False
