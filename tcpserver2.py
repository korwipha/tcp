
import socket


host ="127.0.0.1"
port= 5000
server = socket.socket()
server.bind((host,port))
server.listen(1)

print("wait to connect Client  : ")
server,addr=server.accept()
print("connect From : "+str(addr))


    
with open( 'received_file.jpg', 'wb') as f:
    print "file opened"
    while True:
        print("receiving data...")
        data = server.recv(8192)
        print("data=%s", (data))
        if not data:
            f.close()
            print 'file close()'
            break
        # write data to a file
        f.write(data)

print("Successfully get the file")
server.close()
print("connection closed")
        
