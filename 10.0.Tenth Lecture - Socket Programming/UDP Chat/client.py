import socket
server='192.168.0.120'
port= 8088
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    while True:
        Sdata = input("= ".format(server))
        sock.sendto(Sdata.encode('UTF-8'), (server, int(port)))
        Rdata, Address = sock.recvfrom(1024)
        print(f"- {Rdata.decode('UTF-8')}")
except: pass
finally: 
    sock.close()