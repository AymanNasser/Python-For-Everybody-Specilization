import socket
# Socket Handle
# AF_INET refers to the address family ipv4
# SOCK_STREAM means connection oriented TCP protocol
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connecting to port 80 which is HTTP Port
my_socket.connect(('data.pr4e.org',80))
# Using GET command
# .encode() ==> convert from unicode to UTF-8
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
my_socket.send(cmd)

# 1st output before parsing the file is Metadata of HTTP Header

while True:
    # Receive 512 Char ==> Bytes
    data = my_socket.recv(512)
    # End of transmit if data length is < 1 ==> end of file
    if len(data) < 1:
        break
    # .decode() ==> convert to Unicode
    print(data.decode(encoding= 'utf-8'))

my_socket.close()

