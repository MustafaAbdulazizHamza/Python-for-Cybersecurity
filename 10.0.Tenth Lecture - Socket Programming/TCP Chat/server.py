import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("", 65000))
server.listen(1)
Client, Address = server.accept()
try:
    while True:
        Rdata = Client.recv(1024)
        print("- {}".format(Rdata.decode('utf-8')))
        Sdata = input("= ")
        Client.send(Sdata.encode('utf-8'))
except:
    pass
finally:
    Client.close()
    server.close()