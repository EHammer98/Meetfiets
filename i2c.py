import configparser
data = configparser.ConfigParser()

def getData():
    try:
        data.read('/meetfietsApp/Meetfiets/sps30data.ini') #CHANGE THIS IF YOU HAVE MOVED THE SETTINGS.INI FILE!!!
        print(config.sections())
    except Exception as e: print("ERROR: ", e)

def getPM05_count():
    getData()
    val = data['count']
    return val

def getPM1_count():
    getData()
    val = data['count']
    return val
def getp1_ug():
    getData()
    val = data['ug']
    return val

def getPM25_count():
    getData()
    val = data['count']
    return val
def getPM25_ug():
    getData()
    val = data['ug']
    return val

def getPM4_count():
    getData()
    val = data['count']
    return val
def getPM4_ug():
    getData()
    val = data['ug']
    return val

def getPM10_count():
    getData()
    val = data['count']
    return val
def getPM10_ug():
    getData()
    val = data['ug']
    return val

def getPM_type():
    getData()
    val = data['type']
    return val