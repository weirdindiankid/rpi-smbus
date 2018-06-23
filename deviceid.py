import smbus 
import time

bus = smbus.SMBus(1)

TSL2591_COMMAND_BIT = 0xA0
TSL2591_REGISTER_DEVICE_ID = 0x12
TSL2591_REGISTER_DEVICE_STATUS = 0x13
TSL2591_ADDR = 0x29

device_id = bus.read_byte_data(TSL2591_ADDR, TSL2591_COMMAND_BIT | TSL2591_REGISTER_DEVICE_ID)

print("Device ID: " + str(hex(device_id)))
