from scapy.all import IP, TCP, Ether, RandShort, srp

def Scanner(target: str,port: int) -> str:
    pkt = Ether()/IP(dst=target)/TCP(sport=RandShort(), dport=port, flags="S")
    r = srp(pkt, verbose=False, timeout=4)[0]
    return [port , str(r[0][1][TCP].flags)]



for port in [22, 80,443, 124]:
    result = Scanner("192.168.0.1", port)
    print(f"*{result[0]} ---> {result[1]}*")