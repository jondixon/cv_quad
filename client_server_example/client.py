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
import Queue

class client:
    def __init__(self, debug=False, host='localhost',port=50007):
        """
        Setting HOST to localhost 
        for now...
        """
        self.DEBUG = debug
        self.HOST = host
        self.PORT = port


        """
        Set Up Socket
        """
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.errorcode = -10



    def connect(self):
        """
        Try to connect to the host
        """
        if self.DEBUG: print "Trying to connect to server..."
        while True:


            try:
                self.sock.connect( ( self.HOST, self.PORT ) )
                self.errorcode=-10
                """
                If the host isn't present,
                handle the error gracefully
                """
            except socket.error, v:
                self.errorcode=v[0]
                """
                Check if an error occurred,
                Carry on if everything is fine
                """
            finally:
                if self.errorcode==errno.ECONNREFUSED:
                    """
                    Sleep for a moment before
                    giving it another shot
                    """
                    time.sleep(1)
                else:
                    break


    def send(self,message):
        self.sock.send(message)

    def recv(self):
        data = self.sock.recv(1024)
        if self.DEBUG: print 'Received', data
        return data

    def close(self):
        self.sock.close()

if __name__ == "__main__":
    send_msg = "Hello World From Client!\n"
    c = client(debug=True)
    c.connect()
    c.send(send_msg)
    c.recv()
    c.close()
    


