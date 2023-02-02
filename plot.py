import serial
import matplotlib.pyplot as plt
import time


def wait_for_tok(ser, tok):
    r = ""
    while not r.startswith(tok):
        r = ser.readline().decode("ascii")
        print(f"SER: {r}", end="")


def init_board(ser):
    print("initializing board...")

    s.write(b'\x03')
    time.sleep(1)

    s.reset_input_buffer()

    s.write(b'\x04')


def proc_lines(csv_lines):
    x = [float(l.split(",")[0].strip()) for l in csv_lines]
    y = [float(l.split(",")[1].strip()) for l in csv_lines]

    return x, y


def run_step_response(s, kP, setpoint, num_pts=250):
    # Kp
    wait_for_tok(s, "$A")
    s.write(bytes(f"{kP}\r\n", 'ascii'))

    # setpoint
    wait_for_tok(s, "$B")
    s.write(bytes(f"{setpoint}\r\n", 'ascii'))

    wait_for_tok(s, "$E")
    s.write(bytes(f"{num_pts}\r\n", 'ascii'))

    wait_for_tok(s, "$C")
    print("Getting CSV")

    r = ""
    csv = []
    while True:
        r = s.readline().decode("ascii").strip()
        if r.startswith("$D"):
            break
        csv.append(r)

    return csv


with serial.Serial('COM3', baudrate=115200) as s:
    init_board(s)

    plt.plot(*proc_lines(run_step_response(s, .0025, 16000)), label="Kp=0.0025")
    plt.plot(*proc_lines(run_step_response(s, .005, 16000)), label="Kp=0.005")
    plt.plot(*proc_lines(run_step_response(s, .02, 16000)), label="Kp=0.02")

    plt.legend(loc='lower right')
    plt.xlabel("Time (ms)")
    plt.ylabel("Position (enc count)")
    plt.title("Step Response")
    plt.savefig("plot.png")
    plt.show()



