import snap7

#IP PLC


ip = '192.168.0.22'
slot = 2
rack = 0

#Reading from db
db_number = 1
start_adress = 0
size = 6

#Connecring to PLC
plc = snap7.client.Client()
plc.connect(ip, rack, slot)

#Reading status
print(f'Connect: {plc.get_connected()}')
print(f'CPU Status: {plc.get_cpu_state()}')

#Reading from db
db = plc.db_read(db_number, start_adress, size)
value = snap7.util.get_char(db, 2)
print(f'char: {value}')
value = int.from_bytes(db[1:2], byteorder='big')
print(f'byte: {value}')

value = int.from_bytes(db[4:6], byteorder='big')
print(f'int: {value}')
value = bool(db[0])
print(f'boll: {value}')

#Writing to db
buffer = bytearray([0, 25])
plc.db_write(db_number, 6, buffer)
plc.db_write(db_number, 4, bytearray([0, 15]))
plc.db_write(db_number, 0, bytearray([False]))

#Reading from merker member
merker = plc.mb_read(1, 2)
value_merker = int.from_bytes(merker, byteorder='big')
print(f'Merker Word 1: {value_merker}')

#Writing to merker
plc.mb_write(4, 2, bytearray([0,255]))

merker = plc.mb_read(0, 1)
value_merker = bool(merker[0])
print(f'Status merker M0.0: {value_merker}')

plc.mb_write(0, 1, bytearray([True]))


