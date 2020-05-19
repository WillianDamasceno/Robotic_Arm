import serial
import time

ser = serial.Serial('COM4', baudrate=9600, timeout=1)
time.sleep(3)

valStr = str(input('Digite o valor: '))
valByte = bytes(valStr, 'utf-8')
ser.write(valByte)

