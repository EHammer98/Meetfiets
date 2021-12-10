import json
import requests
import sys
import time
from datetime import datetime
import os

def convertData(logFileP, dataList, bike, idList, typeList, dateTime, url, debug, version):
    try:
        body ={
                      "identifier": bike,
                      "version": version,
                      "measurements": []
        }
        itms=[]
        indx = 0
        for i in dataList:
            itms.append({"deveui": bike[-2:] + str(idList[indx]), "type": typeList[indx], "datetime": str(dateTime), "payload": str(dataList[indx]).replace(" ", "")})                                
            #DEBUG
            if debug == '1' or debug == '2':  
                print("index: ", str(indx), "\n")
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                msg = dt_string + "|INFO: Sensor-ID> " + str(bike[-2:] + str(idList[indx])) + "\n" 
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
                msg = dt_string + "|INFO: Sensor-Type> " + str(typeList[indx].replace(" ", "")) + "\n"
                logFile = open(logFileP, 'a')
                logFile.write(msg)
                logFile.close()
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                msg = dt_string + "|INFO: Sensor-Data> " + str(dataList[indx]) + "\n"
                logFile = open(logFileP, 'a')
                logFile.write(msg)
                logFile.close()
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                msg = dt_string + "|INFO: DateTime " + str(dateTime) + "\n"
                logFile = open(logFileP, 'a')
                logFile.write(msg)
                logFile.close()
            indx += 1

        body["measurements"].extend(itms)                                                
        headers =  {'Content-Type': 'application/json'}
        print("URL: ", url, "\n")
        print("DATA: ", str(json.dumps(body)), "\n")
        response = requests.request("POST", url, headers=headers, data=json.dumps(body))
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