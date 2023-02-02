import serial

with serial.Serial('COM3', baudrate=115200) as s:
    s.write(b'somthing')

import matplotlib.pyplot as plt
ser = serial.Serial('COM3', baudrate=115200)

def read_serial_data(s_port):
    data =[]
    while True:
        line = s_port.readline().strip().split(b',')
        if
>>>>>>> Stashed changes
