
from pymodbus.client.sync import ModbusSerialClient
from pymodbus.register_read_message import ReadInputRegisterResponse

client = ModbusSerialClient(method = "rtu", port = "/dev/ttyAMA0", stopbits = 1, bitesize = 8, parity = 'N', baudrate = 4800)

def getO3(debug):   
    if debug == '2':
        return "4"
    else:
        con = client.connect()
        print(con)
        val = client.read_holding_registers(address=10, count=1, unit=4)
        client.close()
        return val
        #val.registers
def getNO2(debug):
    if debug == '2':
        return "3"
    else:
        con = client.connect()
        print(con)
        val = client.read_holding_registers(address=0, count=1, unit=1)
        client.close()
        return val
        #val.registers
    ################################ BC
def getBC(debug):
    if debug == '2':
        return "17"
    else:
        con = client.connect()
        print(con)
        val = client.read_holding_registers(address=0, count=1, unit=3)
        client.close()
        return val
        #val.registers