from src.encoder_reader import EncoderReader
from src.control import Control
from src.motor_driver import MotorDriver
import pyb

if __name__ == '__main__':
    # u2 = pyb.UART(1, baudrate=115200)
    # u2.read(1) # Wait for connection
    # u2.writechar("t")

    m1 = MotorDriver(pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)
    # m2 = MotorDriver(pyb.Pin.board.PC1, pyb.Pin.board.PA0, pyb.Pin.board.PA1, 5)
    enc = EncoderReader(pyb.Pin.board.PB6, pyb.Pin.board.PB7, 4)
    while True:
        Kp = input("Enter a value for Kp")
        con = Control(Kp, setpoint=0, initial_output=0)
        setpoint = input("Enter setpoint")
        utime.sleep_ms(10)
        while: #ADD CONDITIONAL
            measured_output = enc.read
            motor_actuation = con.run(setpoint,measured_output)

        con.print_time()