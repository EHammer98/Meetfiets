#import serial
#ser = serial.Serial('/dev/ttyAMA0', 4800, timeout=1)
#print(ser)

#ser.write(str.encode(':0603000C000145BE\r\n'))
#print(repr(ser.read(1000)))  # Read 1000 bytes, or wait for timeout

#Crontab job: * * * * * (At every minute.)



import serial

ser = serial.Serial('/dev/ttyAMA0', 4800, timeout=4)
cmd = [0x03, 0x03, 0x00, 0x00, 0x00, 0x01, 0x84, 0x0A]
ser.write(serial.to_bytes(cmd))
response = ser.read(128)

print(response.hex())
