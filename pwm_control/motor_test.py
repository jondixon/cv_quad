import motorPWM

print "About to initialize motor"

motor1 = motorPWM.motor(27)

while (1):
    motor1Percent = raw_input("Enter percent thrust for motor 1: ")
    motor1.setRotor(motor1Percent)
