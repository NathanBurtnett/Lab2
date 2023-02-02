import pyb
import utime

class Control:
    """!
    """
    def __init__(self, Kp, setpoint, initial_output):
        """!
        """
        self.t_start = utime.ticks_ms()
        self.Kp = Kp
        self.setpoint = setpoint
        self.output = initial_output
        self.time = []
        self.position = []

    def run(self, setpoint, measured_output):
        """!
        """
        error = setpoint - measured_output
        motor_actuation = self.Kp * error
        self.times.append(utime.ticks_ms() - self.t_start)
        self.positions.append(measured_output)
        return motor_actuation

    def set_setpoint(self, setpoint):
        """!
        """
        self.setpoint = setpoint

    def set_Kp(self, Kp):
        """!
        """
        self.Kp = Kp

    def print_time(self):
        """!
        """
        for i in range(len(self.times)):
            print("{}, {}".format(self.times[i],self.positions[i]))
