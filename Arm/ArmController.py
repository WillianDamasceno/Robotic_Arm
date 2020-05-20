import serial
import time

ser = serial.Serial('COM4', baudrate=9600, timeout=1)
time.sleep(3)

movement = open(r'User\movement.txt', 'r')

valStr = movement.read()
valByte = bytes(valStr, 'utf-8')
ser.write(valByte)

movement.close()

time.sleep(5)

validator = open(r'User\movement.txt', 'w')
validator.write('available')
validator.close()
