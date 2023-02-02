import serial
import matplotlib.pyplot as plt

with serial.Serial('COM3', baudrate=115200) as s:
    s.write(b'start')
    plot_data(time_list,position_list)

def read_serial_data(s):
    time_list = []
    position_list = []
    while True:


        try:
            line = s.readline().strip().split(b',')
            time = float(line[0])
            position = float(line[1])
            time_list.append(time)
            position_list.append(position)

    return time_list,position_list


def plot_data(time, position):
    plt.plot(time, position)
    plt.xlabel("Time (ms)")
    plt.ylabel("Position")
    plt.title("Step Response")
    plt.show()

