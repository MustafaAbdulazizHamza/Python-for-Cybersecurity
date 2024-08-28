import socket
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("192.168.0.120", 8088))
    while True:
        Rdata, Address = sock.recvfrom(1024)
        print("- {}".format(Rdata.decode('UTF-8')))
        Sdata = input("= ")
        sock.sendto(Sdata.encode('UTF-8'), Address)
except:
    pass
finally:
    sock.close()