from src.control import control
import pyb

if __name__ == '__main__':
    Kp = input("Enter a value for Kp")
    motor_con = control(Kp, setpoint=0, initial_output=0)
    while True:



#main loop code from motor driver
if __name__ == '__main__':
    # this is a comment
    m1 = MotorDriver(pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)
    enc = EncoderReader(pyb.Pin.board.PB6, pyb.Pin.board.PB7, 4)
    #m2 = MotorDriver(pyb.Pin.board.PC1, pyb.Pin.board.PA0, pyb.Pin.board.PA1, 5)
    level = 0
    while True:
        print(enc.read())
        pyb.delay(50)
        m1.set_duty_cycle(level)