import serial
ser = serial.Serial('/dev/ttyAMA0', 4800, timeout=4)

def getSO2(debug):  
    if debug == '2':
        return "00 00 00 FF FF 00"
    else:
        cmd = [0x05, 0x03, 0x00, 0x06, 0x00, 0x01, 0x65, 0x8F]
        ser.write(serial.to_bytes(cmd))
        response = ser.read(128)
        return response.hex()

def getdB(debug):
    if debug == '2':
        return  "00 00 00 FF FF 00"
    else:
        cmd = [0x06, 0x03, 0x00, 0x0C, 0x00, 0x01, 0x45, 0xBE]
        ser.write(serial.to_bytes(cmd))
        response = ser.read(128)
        return response.hex()

def getNO(debug):
    if debug == '2':
        return "00 00 00 FF FF 00"
    else:
        cmd = [0x07, 0x03, 0x00, 0x06, 0x00, 0x01, 0x64, 0x6D]
        ser.write(serial.to_bytes(cmd))
        response = ser.read(128)
        return response.hex()
