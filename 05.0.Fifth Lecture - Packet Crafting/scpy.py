from scapy.all import *
pkt = Ether(dst="FF:34:56:63:27:fa")/IP(dst="192.168.0.10")/TCP(dport= 22, src=RandShort, flags="S")
print(RandShort)
