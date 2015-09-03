import pygame
import sys
import time
import StringIO

def getButtonsPressed():
    buttonsPressed = [dualshock.get_axis(0),
                      -dualshock.get_axis(1),
                      dualshock.get_axis(2),
                      -dualshock.get_axis(5),
                      dualshock.get_button(0),
                      dualshock.get_button(1),
                      dualshock.get_button(2),
                      dualshock.get_button(3),
                      dualshock.get_button(4),
                      dualshock.get_button(5),
                      dualshock.get_button(6),
                      dualshock.get_button(7),
                      dualshock.get_button(8),
                      dualshock.get_button(9)]
    return buttonsPressed

pygame.init()

joystick_count = pygame.joystick.get_count()
print "Joystick count", joystick_count
if joystick_count == 0:
    print "No Joystick Connected"
    sys.exit()

dualshock = pygame.joystick.Joystick(0)
dualshock.init()

if not dualshock.get_init():
    print "Could not initialize joystick."
    sys.exit()

while 1:
    #delay to simulate a "frame"
    time.sleep(.05)

    #use this to clear out the event queue to update the joystick table
    pygame.event.pump()

    #Get all axes and buttons pressed
    buttonsPressed = getButtonsPressed()

    print buttonsPressed

    if dualshock.get_button(12):
        sys.exit()
