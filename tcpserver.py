
import socket


host ="127.0.0.1"
port= 5000
server = socket.socket()
server.bind((host,port))
server.listen(1)
print("wait to connect Client : ")
client,addr=server.accept()
print("connect From : "+str(addr))


while True :
    fac = 1
    data =client.recv(1024)
    n = (int)(data)
    if not data : break
    while n >=1:
        fac = fac*n
        n = n - 1
        
    data = (str)(fac)
    print("Message From Client : " +data)
    client.send(data)
client.close()

        

    
    
