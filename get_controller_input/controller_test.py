import pygame
import sys
import time
import StringIO

class controller:
    def __init__(self):
        self.state = []
        pygame.init()

        joystick_count = pygame.joystick.get_count()
        print "Joystick count", joystick_count
        if joystick_count == 0:
            print "No Joystick Connected"
            sys.exit()

        self.dualshock = pygame.joystick.Joystick(0)
        self.dualshock.init()

        if not self.dualshock.get_init():
            print "Could not initialize joystick."
            sys.exit()


    def readState(self):
        #delay to simulate a "frame"
        time.sleep(.05)
        #use this to clear out the event queue to update the joystick table
        pygame.event.pump()
        self.state = [self.dualshock.get_axis(0),
                      -self.dualshock.get_axis(1),
                      self.dualshock.get_axis(2),
                      -self.dualshock.get_axis(5),
                      self.dualshock.get_button(0),
                      self.dualshock.get_button(1),
                      self.dualshock.get_button(2),
                      self.dualshock.get_button(3),
                      self.dualshock.get_button(4),
                      self.dualshock.get_button(5),
                      self.dualshock.get_button(6),
                      self.dualshock.get_button(7),
                      self.dualshock.get_button(8),
                      self.dualshock.get_button(9)]

        if self.state[12] and self.state[10] and self.state[6]:
            sys.exit()

    def getState(self):
        return self.state

if __name__ == "__main__":
    cState = controller()
    while 1:

        #Get all axes and buttons pressed
        cState.readState()

        print cState.getState() 
