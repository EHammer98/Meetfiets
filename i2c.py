import configparser
dataFile = configparser.ConfigParser()


def getData(sps30dataPath):
    try:
        dataFile.read(sps30dataPath) #CHANGE THIS IF YOU HAVE MOVED THE SETTINGS.INI FILE!!!
        print(dataFile.sections())
    except Exception as e: print("ERROR: ", e)

def getPM05_count(sps30dataPath, debug):
    getData(sps30dataPath)
    data = dataFile['pm05']
    val = data['count']
    return val

def getPM1_count(sps30dataPath, debug):
    getData(sps30dataPath)
    data = dataFile['pm1']
    val = data['count']
    return val
def getPM1_ug(sps30dataPath, debug):
    getData(sps30dataPath)
    data = dataFile['pm1']
    val = data['ug']
    return val

def getPM25_count(sps30dataPath, debug):
    getData(sps30dataPath)
    data = dataFile['pm25']
    val = data['count']
    return val
def getPM25_ug(sps30dataPath, debug):
    getData(sps30dataPath)
    data = dataFile['pm25']
    val = data['ug']
    return val

def getPM4_count(sps30dataPath, debug):
    getData(sps30dataPath)
    data = dataFile['pm4']
    val = data['count']
    return val
def getPM4_ug(sps30dataPath, debug):
    getData(sps30dataPath)
    data = dataFile['pm4']
    val = data['ug']
    return val

def getPM10_count(sps30dataPath, debug):
    getData(sps30dataPath)
    data = dataFile['pm10']
    val = data['count']
    return val
def getPM10_ug(sps30dataPath, debug):
    getData(sps30dataPath)
    data = dataFile['pm10']
    val = data['ug']
    return val

def getPM_type(sps30dataPath, debug):
    getData(sps30dataPath)
    data = dataFile['pm']
    val = data['type']
    return val