"""
    cv_quad server script

    This module is the server script to be run by the Host Computer.
    When the server script is executed, the computer will start 
    polling the controller input module for any joystick activity.
    All data being read in from the joystick will be bundled up into 
    a message stream and sent off to the quad copter, where the client 
    module will handle intercepting the controller data.

    Example:
        $ python socket_server.py

    Attributes:
        HOST (str): Hostname for computer we're trying to connect to
        PORT (int): Port on Host computer

    CV Quad Project Wiki:
        http://github.com/jondixon/cv_quad/wiki
"""

import socket

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

"""
Bind the socket to HOST
"""
s.bind((HOST, PORT))

"""
Wait for the client...
"""
print "Waiting for client to connect..."
s.listen(1)
conn, addr = s.accept()

"""
Send out a message
"""
send_msg = "Hello World From Server!\n"
recv_msg = "none"

"""
Verify connection has been established
"""
print 'Connected by', addr
while 1:
    data = conn.recv(1024)
    """
    When Client data stream is empty,
    communication must be complete
    """
    if not data: break
    recv_msg = data
    """
    Verify Client Sent us a Message
    """
    print 'Received', recv_msg

    for i in range(10):
      conn.send(send_msg)
    break


"""
Close the Connection
"""
conn.close()
