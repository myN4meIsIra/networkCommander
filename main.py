# ARP poisoner
"""

"""

from multiprocessing import Process
from scapy.all import *

# custom libraries
from networkScanner import Scanner
netScanner = Scanner()



def main():
    # scan the network for all the devices on the network
    print(f'scanning network')
    IP = "10.42.0.114"
    netMask = "24"
    type = 'ICMP'
    netScanner.scan(type, IP, netMask)

    return 1


if __name__ == "__main__":
    main()