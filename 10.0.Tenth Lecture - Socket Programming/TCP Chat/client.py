import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.0.120", 65000))
try:
    while True:
        Sdata = input("= ").encode('utf-8')
        client.send(Sdata)
        Rdata = client.recv(1024)
        print("- {}".format(Rdata.decode('utf-8')))
except:
    pass
finally:
    client.close()