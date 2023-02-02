import serial
import matplotlib.pyplot as plt

with serial.Serial('COM3', baudrate=115200) as s:
    s.write(b'start')

def read_serial_data(s):
    data =[]
    while True:
        line = s.readline().strip().split(b',')
        if


def plot(time, position):
    plt.plot(time, position)
    plt.xlabel("Time (ms)")
    plt.ylabel("Position")
    plt.title("Step Response")
    plt.show()

