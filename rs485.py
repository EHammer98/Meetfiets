import serial

def getSO2():
    ser = serial.Serial('/dev/ttyAMA0', 4800, timeout=4)
    cmd = [0x05, 0x03, 0x00, 0x06, 0x00, 0x01, 0x65, 0x8F]
    ser.write(serial.to_bytes(cmd))
    response = ser.read(128)
    return response.hex()

def getdB():
    cmd = [0x06, 0x03, 0x00, 0x0C, 0x00, 0x01, 0x45, 0xBE]
    ser.write(serial.to_bytes(cmd))
    response = ser.read(128)
    return response.hex()

def getNO():
    cmd = [0x07, 0x03, 0x00, 0x06, 0x00, 0x01, 0x64, 0x6D]
    ser.write(serial.to_bytes(cmd))
    response = ser.read(128)
    return response.hex()
