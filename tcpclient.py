import socket


host ="127.0.0.1"
port= 5000
server = socket.socket()
server.connect((host,port))
data =raw_input("Number for fac : ")

while data!='' :
    server.send(data)
    data=server.recv(1024)
    print("fac is : "+data)
    data = raw_input("Number for fac : ")
server.close()

        

