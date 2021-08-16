import sys
import time
import configparser
sys.path.insert(1, '/home/pi/.local/lib/python3.7/site-packages (3.5)')
import serial
# insert at 1, 0 is the script path (or '' in REPL) 
sys.path.insert(1, '/meetfietsApp/Meetfiets')
import rs485.py
import rs485_crc16.py
import i2c.py
#SETUP  
config = configparser.ConfigParser()
version = '0.0.3'

#Settings
try:
    config.read('/meetfietsApp/Meetfiets/settings.ini') #CHANGE THIS IF YOU HAVE MOVED THE SETTINGS.INI FILE!!!
    print(config.sections())
except Exception as e: print("ERROR: ", e) 
PDFmerger_Settings = config['meetfietsApp']
debug=PDFmerger_Settings['debug']
urlAPI=PDFmerger_Settings['urlAPI']
restartTime=PDFmerger_Settings['restartTime']
logFilePath=PDFmerger_Settings['logFilePath']


try:
    logFile = open(logFilePath, 'a')
except Exception as u: print("ERROR: ", u)

if debug == 2:
    print('Version: '+version)
    print('DEBUG ENABLED')
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    msg = dt_string + "|INFO: Loaded settings> " + str(config.sections()) + "\n" 
    logFile = open(logFilePath, 'a')
    logFile.write(msg)
    logFile.close()

def main():
    try:
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
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                msg = dt_string + "|INFO: Sensor value (x100)> " + str(v) + "\n" 
                logFile = open(logFilePath, 'a')
                logFile.write(msg)
                logFile.close()


        for s in sensorSpecials:
            val = val * 100
            val = hex(s)
            val.removeprefix('0x')
            s = '000000'+val+'0000'

        #DEBUG
        if debug == 1: 
            for s in sensorSpecials:
                    print('Sensor calc. value (x100): '+v)
                    now = datetime.now()
                    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                    msg = dt_string + "|INFO: Sensor calc. value (x100)> " + str(v) + "\n" 
                    logFile = open(logFilePath, 'a')
                    logFile.write(msg)
                    logFile.close()

    except Exception as u:
        now = datetime.now()
        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("ERROR: ", u, exc_type, fname, exc_tb.tb_lineno)
        msg = dt_string + "|ERROR: " + str(u) + " " +  str(exc_type) + " " + str(fname) + "Line: " + str(exc_tb.tb_lineno) +  "\n" 
        logFile = open(logFilePath, 'a')
        logFile.write(msg)
        logFile.close()
        
    timer = threading.Timer(restartTime, main) #60.0
    timer.start()
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    msg = dt_string + "|INFO: Timer had been restarted for > 60sec\n"
    logFile = open(logFilePath, 'a')
    logFile.write(msg) 
    logFile.close()

timer = threading.Timer(1.0, main) 
timer.start() 