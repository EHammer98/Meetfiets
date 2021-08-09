from pymodbus.client.sync import ModbusSerialClient
#from pymodbus.register_read_message import ReadInputRegisterResponse
client = ModbusSerialClient(method = "rtu", port = "/dev/ttyAMA0", stopbits = 1, bitesize = 8, parity = 'N', baudrate = 4800)

def getO3():   
    con = client.connect()
    print(con)
    val = client.read_holding_registers(address=10, count=1, unit=4)
    client.close()
    return val.registers
def getNO2():
    con = client.connect()
    print(con)
    val = client.read_holding_registers(address=0, count=1, unit=3)
    client.close()
    return val.registers
    ################################
def getNO2():
    con = client.connect()
    print(con)
    val = client.read_holding_registers(address=0, count=1, unit=2)
    print(val.registers)
    client.close()
    return val.registers