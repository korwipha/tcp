import socket


host ="127.0.0.1"
port= 5000
server = socket.socket()
server.connect((host,port))
BUFFER_SIZE = 4096

filename="112.jpg"
f = open(filename,'rb')

while True:
    l = f.read()
    while (l):
        server.send(l)
        print("Sent ",repr(l))
        l = f.read()
    if not l:
        f.close()
        server.close()
        break


