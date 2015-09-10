import motorPWM
import sys

print "About to initialize motor"

motor1 = motorPWM.motor(27)

while (1):
    motor1.setRotor(input("Enter percent thrust for motor 1: "))
