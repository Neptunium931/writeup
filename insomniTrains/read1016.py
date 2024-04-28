from pymodbus.client import ModbusTcpClient


client = ModbusTcpClient("172.17.0.2")  # Create client object
client.connect()  # connect to device, reconnect automatically
result = client.read_holding_registers(1016, 11, slave=0)  # get information from device
# print(result)  # use information
print(result.registers)  # use information
hex = [hex(i) for i in result.registers]
print(hex)
ascii_string = [chr(int(i[2:4], 16)) for i in hex]
ascii_string2 = [chr(int(i[4:6], 16)) for i in hex]
ascii_string3 = ""
for i in range(len(ascii_string)):
    ascii_string3 += ascii_string[i]
    ascii_string3 += ascii_string2[i]
print(ascii_string3)
client.close()  # Disconnect device
