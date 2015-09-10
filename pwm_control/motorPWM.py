from RPIO import PWM

#Class definition for the motor class
class motor:
    def __init__(self, GPIOPIN):
        self.pin = GPIOPIN
        self.servo = PWM.Servo()

        #send init signal to ESC
        self.servo.set_servo(self.pin, 1000)

    def setRotor(percentThrust):
        self.servo.set_servo(self.pin, percentThrust*10+1000)

    def __del__(self):
        self.servo.stop_servo(self.pin)
