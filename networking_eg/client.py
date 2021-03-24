import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
param_tup = ('localhost', 9874)
sock.connect( param_tup )

# we can pass in system variables when we start the program
if len(sys.argv) > 1:
    message = ' '.join(sys.argv[1:]) # member 0 is the module name
else:
    message='default message'

# send our message to the server
sock.send( message.encode() )

# receive and handle any response from the server
data = sock.recv(4096) # up to 4096
print(data)
sock.close()