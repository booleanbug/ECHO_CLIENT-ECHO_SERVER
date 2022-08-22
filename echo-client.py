# import necessary libraries
from email import message
import socket
import sys
from typing import final

# create TCP/IP socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# connect to the socket to port of server
server_address = ('localhost',10000)
print('connectign to {} port {}'.format(*server_address))
sock.connect(server_address)

# send the data and get hte response
try:
    # send the data
    message = b'this the message.It will be repeated'
    print('sending {!r}'.format(message))
    sock.sendall(message)

    # get the response
    amount_received = 0
    amount_expected = len(message)

    # take all messages
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received+=len(data)
        print('recieved {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()