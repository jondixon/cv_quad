import motorPWM
import sys

print "About to initialize motor"


motor1 = motorPWM.motor(05)
motor2 = motorPWM.motor(06)
motor3 = motorPWM.motor(13)
motor4 = motorPWM.motor(19)

while (1):
    thrust = input("Enter percent thrust: ")
    motor1.setRotor(thrust)
    motor2.setRotor(thrust)
    motor3.setRotor(thrust)
    motor4.setRotor(thrust)
