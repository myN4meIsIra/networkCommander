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
    IP = netScanner.getOwnIP()
    netMask = "24"
    type = 'ARP'
    netScanner.scan(type, IP, netMask)


    return 1


if __name__ == "__main__":
    main()