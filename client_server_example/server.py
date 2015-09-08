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

class server:
    def __init__(self, debug=False, host='localhost',port=50007):
        """
        Setting HOST to localhost 
        for now...
        """
        self.DEBUG = debug
        self.HOST = host
        self.PORT = port

        self.conn = 'null'
        self.addr = 'null'
        """
        Set Up Socket
        """
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def bind(self):
        """
        Bind the socket to HOST
        """
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind( ( self.HOST, self.PORT ) )

        """
        Wait for the client...
        """
        print "Waiting for client to connect..."
        self.sock.listen(1)
        self.conn, self.addr = self.sock.accept()
        if self.DEBUG: print 'Connected by', self.addr

    def send(self,message):
        self.conn.send(message)

    def recv(self):

        data = self.conn.recv(1024)
        """
        When Client data stream is empty,
        communication must be complete
        """
        if not data: return 'none'
        recv_msg = data

        """
        Verify Client Sent us a Message
        """
        print 'Received', recv_msg
        return recv_msg


    def close(self):
        self.conn.close()

if __name__ == "__main__":
    send_msg = "Hello World From Server!\n"
    s = server(debug=True)
    s.bind()
    s.recv()
    s.send(send_msg)
    s.close()
