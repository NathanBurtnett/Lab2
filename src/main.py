"""!
@file main.py
This file contains the main script. It exposes an interface over serial to
run a step command.
"""
from encoder_reader import EncoderReader
from control import Control
from motor_driver import MotorDriver
import pyb
import sys


def get_numeric_input(prompt):
    """!
    Checks if the value passed into the function, prompt, is an acceptable value
    if not, an error will be shown.
    :param prompt: The value input to be checked
    :return: the value of prompt as a float number
    """
    while True:
        try:
            i = input(prompt)
            return float(i)

        except ValueError:
            print("Invalid number")


if __name__ == '__main__':
    m1 = MotorDriver(pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)
    enc = EncoderReader(pyb.Pin.board.PB6, pyb.Pin.board.PB7, 4)
    while True:
        # Asks for values of Kp, the encoder position and the number
        # of points wanted to be shown on the plot
        Kp = get_numeric_input("$A Enter a value for Kp\n")
        setpoint = get_numeric_input("$B Enter a setpoint\n")
        num_pts = get_numeric_input("$E Enter num of points to get. 0 will run till steady state.\n")

        # Sets the variable con to be the output from the control file
        con = Control(Kp, setpoint=setpoint, initial_output=0)
        enc.zero()

        num_same = 0
        ss = 0

        # Checks if the system has reached steady state in order to determine if the
        # motor has reached its destination. The ss variable is the count of the number
        # of consecutive values of encoder position.
        while (num_pts == 0 and num_same < 25) or (num_pts != 0 and len(con.positions) < num_pts):
            measured_output = -enc.read()
            motor_actuation = con.run(setpoint, measured_output)
            m1.set_duty_cycle(motor_actuation)

            if ss != measured_output:
                ss = measured_output
                num_same = 0
            else:
                num_same += 1

            pyb.delay(10)

        m1.set_duty_cycle(0)
        print("$C Print CSV")
        con.print_time()
        print("$D CSV Done!")
