from dataclasses import dataclass
import socket
import sys
from typing import final

# make TCP/IP door
door = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# bind the door to entrance of home (for that you need home address and  home port)
server_address = ('localhost',10000)
print('starting up on {} port {}'.format(*server_address))
door.bind(server_address)

# listening for incoming guests
door.listen(1)

# now use this socket for listening to connections sent by clients
while True:
    print("Waiting for connection")
    connection,client_address = door.accept()
    try:
        print("connection from : ",client_address)
        while True:
            data = connection.recv(16)
            print('recieved {!r}'.format(data))
            if data:
                print("Sending back data to client")
                connection.sendall(data)
            else:
                print("no data from",client_address)
                break
    finally:
        connection.close()
