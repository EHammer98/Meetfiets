import rs485.py
import rs485_crc16.py
import i2c.py
import time

version = '0.0.1'
debug = 1

if debug == 1:
    print('Version: '+version)
    print('DEBUG ENABLED')

sen_NO2 = ''
sen_BC = ''
sen_O3 = ''
sen_SO2 = ''
sen_dB = ''
sen_NO = ''
sen_PM05 = ''
sen_PM1 = ''
sen_PM25 = ''
sen_PM4 = ''
sen_PM10 = ''

sensorsVal = [sen_NO2,sen_BC,sen_O3,sen_SO2,sen_dB,sen_NO,sen_PM05,sen_PM1,sen_PM25,sen_PM4,sen_PM10]
sensorFunc = [getNO2,getBC,getO3,getSO2,getdB,getNO,getPM05,getPM1,getPM25,getPM4,getPM10]
sensorSpecials = [sen_NO2,sen_BC,sen_O3,sen_PM05,sen_PM1,sen_PM25,sen_PM4,sen_PM10]

for f in sensorFunc and v in sensorsVal:
    v = rs485.f()
    time.sleep(3) # Sleep for 3 seconds

#DEBUG
if debug == 1:      
    for v in sensorsVal:
        print('Sensor value (x100): '+v)


for s in sensorSpecials:
    val = val * 100
    val = hex(s)
    val.removeprefix('0x')
    s = '000000'+val+'0000'

#DEBUG
if debug == 1: 
    for s in sensorSpecials:
            print('Sensor calc. value (x100): '+v)