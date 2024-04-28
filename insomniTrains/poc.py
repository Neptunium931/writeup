from pymodbus.client import ModbusTcpClient
import time


def sendPaload(paload):
    for value in paload:
        client.write_registers(1001, value, slave=0)
        time.sleep(0.1)

    result = client.read_holding_registers(
        1016, 1, slave=0
    )  # get information from device
    print(result.registers)  # use information
    print(result.bits)  # use information
    time.sleep(0.1)


# client = ModbusTcpClient("192.168.111.123")  # Create client object
client = ModbusTcpClient("172.17.0.2")  # Create client object
client.connect()  # connect to device, reconnect automatically

# client.write_registers(1001, [17201, 21292, 12336], slave=0)
result = client.read_holding_registers(1016, 1, slave=0)  # get information from device
print(result.registers)  # use information
print(result.bits)  # use information
paload1 = [
    [17201, 21297, 12336],
    [21332, 21297, 12336],
    [17202, 21297, 12336],
    [21317, 21297, 12336],
]

paload2 = [
    [17201, 21299, 12336],
    [21332, 21299, 12336],
    [17202, 21299, 12336],
    [21317, 21299, 12336],
]

paload3 = [
    [17201, 21297, 12337],
    [21332, 21297, 12337],
    [17202, 21297, 12337],
    [21317, 21297, 12337],
]
# print("paload1")
# sendPaload(paload1)
# print("paload2")
# sendPaload(paload2)
print("paload3")
sendPaload(paload3)
time.sleep(5)
# print("paload3")
# sendPaload(paload3)
# time.sleep(10)
# result = client.read_holding_registers(1016, 1, slave=0)  # get information from device
# print(result.registers)  # use information
# print(result.bits)  # use information
client.close()  # Disconnect device
