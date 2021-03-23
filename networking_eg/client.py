import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
param_tup = ('localhost', 9874)
sock.connect( param_tup )

message='quit'

# send our message to the server
sock.send( message.encode() )

# receive and handle any response from the server
data = sock.recv(4096) # up to 4096
print(data)
sock.close()