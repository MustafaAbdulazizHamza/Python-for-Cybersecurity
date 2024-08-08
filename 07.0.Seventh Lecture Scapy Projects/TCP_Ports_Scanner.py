from scapy.all import IP, TCP, Ether, RandShort, srp
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore
class Scanner:
    def __init__(self, target:str, ports:str) -> None:
        self._target = target
        if '-' in ports:
            self._ports = self.port_range(ports)
        elif ',' in ports:
            self._ports = [int(port) for port in ports.split(",")]
        else:
            self._ports = [int(ports)]
    def port_range(self, ports: str):
        ports = ports.split('-')
        return list(range(int(ports[0]),int(ports[1])+1))
    def __Scan(self, port:int):
        pkt = Ether()/IP(dst=self._target)/TCP(sport=RandShort(), dport=port, flags="S")
        r = srp(pkt, verbose=False, timeout=4)[0]
        return [port , str(r[0][1][TCP].flags)]
    def Scan(self):
        print(Fore.GREEN+f"Scanning results for target {self._target}\nPorts\t\t\tAnswer"+Fore.RESET)
        with ThreadPoolExecutor() as ex:
            results = ex.map(self.__Scan, self._ports)
            for res in results:
                print(Fore.CYAN+f"{res[0]}\t\t\t{res[1]}")
scanner = Scanner("192.168.0.1", "1-500")
scanner.Scan()