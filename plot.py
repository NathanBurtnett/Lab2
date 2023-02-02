import serial
with serial.Serial('COM3', baudrate=115200) as s:
    s.write(b'somthing')
