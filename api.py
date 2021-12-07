import json
import requests
import sys
import time
from datetime import datetime
import os

def convertData(logFileP, dataList, bike, idList, typeList, dateTime, url, debug, version):
    try:
        for i in dataList:
            x = {
              "identifier": bike,
              "version": version,
              "measurements": [
                {"deveui": bike[-2:] + str(idList[dataList.index(i)]), "type": typeList[dataList.index(i)], "datetime": str(dateTime), "payload": str(dataList[dataList.index(i)]).replace(" ", "")}
              ]
            }
                                       
            #DEBUG
            if debug == '1' or debug == '2':      
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                msg = dt_string + "|INFO: Sensor-ID> " + str(bike[-2:] + str(idList[dataList.index(i)])) + "\n" 
                logFile = open(logFileP, 'a')
                logFile.write(msg)
                logFile.close()
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                msg = dt_string + "|INFO: Version> " + str(version) + "\n" 
                logFile = open(logFileP, 'a')
                logFile.write(msg)
                logFile.close()
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                msg = dt_string + "|INFO: Sensor-Type> " + str(typeList[dataList.index(i)].replace(" ", "")) + "\n"
                logFile = open(logFileP, 'a')
                logFile.write(msg)
                logFile.close()
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                msg = dt_string + "|INFO: Sensor-Data> " + str(dataList[dataList.index(i)]) + "\n"
                logFile = open(logFileP, 'a')
                logFile.write(msg)
                logFile.close()
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                msg = dt_string + "|INFO: DateTime " + str(dateTime) + "\n"
                logFile = open(logFileP, 'a')
                logFile.write(msg)
                logFile.close()
          
            headers =  {'Content-Type': 'application/json'}
            print("URL: ", url, "\n")
            print("DATA: ", str(json.dumps(x)), "\n")
            response = requests.request("POST", url, headers=headers, data=json.dumps(x))
            print(response, "\n")
            #DEBUG
            if debug == '1' or debug == '2':      
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                msg = dt_string + "|INFO: HTTP-code> " + str(response.status_code) + "\n" 
                logFile = open(logFileP, 'a')
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
        logFile = open(logFileP, 'a')
        logFile.write(msg)
        logFile.close()