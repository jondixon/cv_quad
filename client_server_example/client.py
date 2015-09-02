"""
    cv_quad client script

    This module is the client script to be run by the quad copter.
    The client will wait until a connection is established with 
    the server (a PC with a Playstation 4 controller). When the 
    client and server establish a connection, the client will then 
    begin to read in a stream of joystick information sent from the 
    server. The joystick info will be transferred to the motor 
    controller module to determine power levels to each of the 4 
    propellers in order to facilitate quad copter movement.

    Example:
        $ python socket_client.py

    Attributes:
        HOST (str): Hostname for computer we're trying to connect to
        PORT (int): Port on Host computer
        errorcode (int): value to determine error code

    CV Quad Project Wiki:
        http://github.com/jondixon/cv_quad/wiki
"""

import socket
import errno
import time
"""
Setting HOST to localhost 
for now...
"""
HOST = 'localhost'
PORT = 50007

"""
Set Up Socket
"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

errorcode = -10

"""
Try to connect to the host
"""
print "Trying to connect to server..."
while True:
    try:
        s.connect((HOST, PORT))
        errorcode=-10
        """
        If the host isn't present,
        handle the error gracefully
        """
    except socket.error, v:
        errorcode=v[0]
        """
        Check if an error occurred,
        Carry on if everything is fine
        """
    finally:
        if errorcode==errno.ECONNREFUSED:
            """
            Sleep for a moment before
            giving it another shot
            """
            time.sleep(1)
        else:
            break

s.send('Hello World from Client!')
data = s.recv(1024)
s.close()
print 'Received', data
