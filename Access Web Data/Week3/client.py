import socket

port = 12342
host = '127.0.0.1'

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((host,port))

client_socket.sendall(b'Hello from client')

print(client_socket.recv(1024))

