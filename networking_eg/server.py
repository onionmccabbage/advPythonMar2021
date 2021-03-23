import socket

# we can instantiate a socket server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# param_tup = ('localhost', 9874)
# bind our server to some parameters
server.bind(param_tup) # this is a tuple
server.listen(5) # max requests
# tell the console what we're up to
print('Server is running on {} port {}'.format(param_tup[0], param_tup[1]))

# we create a run-loop to listen for requests and handle them
while True:
    (client, addr) = server.accept()
    # read the first 1024 bytes of the client request
    buf = client.recv(1024)
    print('server has received {}'.format(buf))
    # send a response to the client
    client.send( buf.upper() ) # send it back in upper case
    client.close()
    if buf == b'quit': # a byte-encoded text saying 'quit'
        print('server says bye')
        server.close()
        break