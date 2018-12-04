import Adafruit_PCA9685 as Ada
from time import sleep


pwm = Ada.PCA9685(address=0x40, busnum=1)  # Set 2c to 0x40 on bus 1
pwm.set_pwm_freq(60)  # Set freq to 60


class Movements:
    def __init__(self):
        self.lower = 120  # Min pwm val
        self.middle = 455  # Pwm val for mid point
        self.upper = 600  # Max pwm val
        self.mtr_0_pwm = self.lower  # Home pos for base.
        self.mtr_1_pwm = self.middle  # Home pos for motor 1.
        self.mtr_2_pwm = self.upper  # Home pos for motor 2.
        self.mtr_3_pwm = self.upper  # Home pos for Grabber.
        self.move_speed = 13  # Speed of movements

    def home(self):
        self.mtr_0_pwm = self.lower
        self.mtr_1_pwm = self.middle
        self.mtr_2_pwm = self.upper
        self.mtr_3_pwm = self.upper
        pwm.set_pwm(0, 0, self.mtr_0_pwm)
        sleep(.35)
        pwm.set_pwm(1, 0, self.mtr_1_pwm)
        sleep(.35)
        pwm.set_pwm(2, 0, self.mtr_2_pwm)
        sleep(.35)
        pwm.set_pwm(3, 0, self.mtr_3_pwm)

    def refresh(self):
        pwm.set_pwm(0, 0, self.mtr_0_pwm)
        pwm.set_pwm(1, 0, self.mtr_1_pwm)
        pwm.set_pwm(2, 0, self.mtr_2_pwm)
        pwm.set_pwm(3, 0, self.mtr_3_pwm)
        print("Mtr 0: {}\nMtr 1: {}\nMtr 2: {}\nMtr 3: {}".format(self.mtr_0_pwm, self.mtr_1_pwm, self.mtr_2_pwm, self.mtr_3_pwm))

    def up(self, mtr_num):
        if mtr_num == 0:
            if self.mtr_0_pwm <= self.upper - self.move_speed:
                self.mtr_0_pwm += self.move_speed
        elif mtr_num == 1:
            if self.mtr_1_pwm <= self.upper - self.move_speed:
                self.mtr_1_pwm += self.move_speed
        elif mtr_num == 2:
            if self.mtr_2_pwm <= self.upper - self.move_speed:
                self.mtr_2_pwm += self.move_speed
        elif mtr_num == 3:
            # if self.mtr_3_pwm <= self.upper - self.move_speed:
            self.mtr_3_pwm += self.move_speed
        self.refresh()

    def down(self, mtr_num):
        if mtr_num == 0:
            if self.mtr_0_pwm >= self.lower + self.move_speed:
                self.mtr_0_pwm -= self.move_speed
        elif mtr_num == 1:
            if self.mtr_1_pwm >= self.lower + self.move_speed:
                self.mtr_1_pwm -= self.move_speed
        elif mtr_num == 2:
            if self.mtr_2_pwm >= self.lower + self.move_speed:
                self.mtr_2_pwm -= self.move_speed
        elif mtr_num == 3:
            # if self.mtr_3_pwm >= self.lower + self.move_speed:
            self.mtr_3_pwm -= self.move_speed
        self.refresh()


