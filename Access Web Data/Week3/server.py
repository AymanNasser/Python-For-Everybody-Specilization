import socket

# Creating a socket
server_soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Reserving a local port
port = 12342
host = '127.0.0.1'
# bind() method which binds it to a specific ip and port so that it can listen to incoming requests on that ip and port
# by specifying an empty string to ip ==> makes the server listen to requests coming from other computers on the network
server_soc.bind((host,port))

print('Socket is binded to {} port'.format(port))

max_tries = 5
# Setting the socket into listening mode.
# max_tries = 5 here means that 5 connections are kept waiting if the server is busy and
# if a 6th socket tries to connect then the connection is refused.

server_soc.listen(max_tries)
print('Socket is now listening')

# Make a while loop and start to accept all incoming connections and close those connections after
# a thank you message to all connected sockets
while True:

    # Returning a new socket object, it’s the socket that we’ll use to communicate with the client. It’s distinct from
    # the listening socket that the server is using to accept new connections
    connection,address = server_soc.accept()
    print('Got connection from {}'.format(address))

    # Sending bytes not string
    connection.send(b'Thank you for connecting to this socket')
    data = connection.recv(1024)
    # If conn.recv() returns an empty bytes object ('') then the client closed the connection and the loop is terminated.
    if not data:
        break
    connection.sendall(data)
    connection.close()

