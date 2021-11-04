import sys
import time
from datetime import datetime
import configparser
import threading
import os
# insert at 1, 0 is the script path (or '' in REPL) 
sys.path.append('/meetfietsApp/Meetfiets')
import rs485
import rs485_crc16
import i2c
import api
import pathlib
import socket

#SETUP  
config = configparser.ConfigParser()
version = '0.1.9.1'

#Settings
try:
    config.read('/meetfietsApp/Meetfiets/settings.ini') #CHANGE THIS IF YOU HAVE MOVED THE SETTINGS.INI FILE!!! DEFAULT: /meetfietsApp/Meetfiets/settings.ini
    print(config.sections())
except Exception as e: print("ERROR: ", e) 

config['meetfietsApp']['fiets'] = str(socket.gethostname())
#config['meetfietsApp']['fiets']= "meetfiets02" #    debug
with open('settings.ini', 'w') as configfile:    # save
    config.write(configfile)
settings = config['meetfietsApp']
debug=settings['debug']
urlAPI=settings['urlAPI']
restartTime=settings['restartTime']
logFilePath=settings['logFilePath']
fiets=settings['fiets']
sps30dataPath=settings['sps30dataPath']
try:
    logFile = open(logFilePath, 'a')
except Exception as u: print("ERROR: ", u)

if debug == '2':
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
        sen_NO2 = '' #ND
        sen_BC = '' #BC
        sen_O3 = '' #OZ
        sen_SO2 = '' #SO
        sen_dB = '' #DB
        sen_NO = '' #NO
        sen_PM05 = '' #PM
        sen_PM1 = '' #PM
        sen_PM25 = '' #PM
        sen_PM4 = '' #PM
        sen_PM10 = '' #PM

        sensorID = ["02","03","04","05","06","07","69","70","71","72","73"]
        sensorType = ["ND","BC","OZ","SO","DB","NO","PM","PM","PM","PM","PM"]
        sensorFunc = [rs485_crc16.getNO2(debug),rs485_crc16.getBC(debug),rs485_crc16.getO3(debug),rs485.getSO2(debug),rs485.getdB(debug),rs485.getNO(debug),i2c.getPM05_count(sps30dataPath, debug),i2c.getPM1_count(sps30dataPath, debug),i2c.getPM25_count(sps30dataPath, debug),i2c.getPM4_count(sps30dataPath, debug),i2c.getPM10_count(sps30dataPath, debug)]
        sensorSpecialsA = [sen_NO2,sen_BC,sen_O3]
        sensorNorm = [sen_SO2,sen_dB,sen_NO]
        sensorSpecialsB = [sen_PM05,sen_PM1,sen_PM25,sen_PM4,sen_PM10]

        indx = 6
        for f in sensorFunc:
            
            if int(sensorFunc.index(f)) < 3:
                print("id: " + str(sensorFunc.index(f)) + "\n")
                print("vall: " + str(sensorFunc[int(sensorFunc.index(f))]) + "\n")
                sensorSpecialsA.insert(int(sensorFunc.index(f)), sensorFunc[int(sensorFunc.index(f))])
            if int(sensorFunc.index(f)) == indx:      
                print("id:2 " + str(indx) + "\n")
                print("vall2: " + str(sensorFunc[int(indx)]) + "\n")
                sensorSpecialsB.insert(int(indx), sensorFunc[int(indx)])
                indx = indx + 1
            sensorNorm.insert(int(sensorFunc.index(f)), sensorFunc[int(sensorFunc.index(f))])
            time.sleep(3) # Sleep for 3 seconds


        print("list: " + str(sensorSpecialsB) + "\n")
        try:
            for s in sensorSpecialsB:
                    if s != "":
                        val = sensorSpecialsB[sensorSpecialsB.index(s)] * 100
                        if debug == '2':
                            print("hex: " + hex(int(s)) + "\n")                 
                        val = hex(int(s))     
                        newVal =  val[2:]
                        if debug == '2':
                            print("new val: ", newVal, "\n")
                        if len(newVal) == 1:
                            newVal = "0" + newVal
                        newData = '00 00 00 '+newVal+' 00 00'
                        if debug == '2':
                            print("New data: " + str(newData) + "\n")
                        sensorSpecialsB[sensorSpecialsB.index(s)] = newData
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

        try:
            for m in sensorSpecialsA:
                    if m != "":
                        val = sensorSpecialsA[sensorSpecialsA.index(m)] 
                        if len(val) == 1:
                            val = "0" + val
                        newData = '00 00 00 '+val+' 00 00'
                        if debug == '2':
                            print("New data: " + str(newData) + "\n")
                        sensorSpecialsA[sensorSpecialsA.index(m)] = newData
            while('' in sensorSpecialsA) :
                sensorSpecialsA.remove('')
            while('' in sensorSpecialsB) :
                sensorSpecialsB.remove('')
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
        try:
            while('' in sensorNorm) :
                sensorNorm.remove('')
            del sensorNorm[:3]
            del sensorNorm[3:]
            newSenVal = sensorSpecialsA + sensorNorm + sensorSpecialsB
            if debug == '2':
                print("sensorSpecialsA len: ", len(sensorSpecialsA), "\n")
                print("sensorNorm len: ", len(sensorNorm), "\n")
                print("sensorSpecialsB len: ", len(sensorSpecialsB), "\n")
                print("sensorSpecialsA: ", sensorSpecialsA, "\n")
                print("sensorNorm: ", sensorNorm, "\n")
                print("sensorSpecialsB: ", sensorSpecialsB, "\n")
                print("NEW DATA LIST: ", newSenVal, "\n")
            now = datetime.utcnow()
            dateTime = now.strftime("%Y-%m-%dT%H:%M:%SZ")
            api.convertData(logFilePath, newSenVal, fiets, sensorID, sensorType, dateTime, urlAPI, debug)
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
        
    timer = threading.Timer(int(restartTime), main) #60.0
    timer.start()
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    msg = dt_string + "|INFO: Timer had been restarted for > 60sec\n"
    logFile = open(logFilePath, 'a')
    logFile.write(msg) 
    logFile.close()

timer = threading.Timer(1, main) 
timer.start() 