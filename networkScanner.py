#
'''

'''

import subprocess
import socket
from scapy.all import srp, ARP, Ether
import scapy
import os

# logging
from logger import DataLogging
logger = DataLogging(True)


class Scanner:

    def __init__(self):
        return None


    # get your own IP address
    def getOwnIP(self):
        IP = '127.0.0.1'
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(("10.255.255.255", 1))
            IP = s.getsockname()[0]
            s.close()
        except:
            IP=IP

        logger.log(f'ip --> {IP}', 'networkScanner')

        return IP


    # scan the network for devices
    def scan(self, type, IP, netMask):
        port = 80

        # #of hosts = 2^bits - 2 -- I have -1 because the range starts at 1, so the first -1 wouldn't be needed
        hosts_range = (2 ** (32 - (int(netMask)))) - 1

        logger.log(f'netMaskRange = {hosts_range}', 'networkScanner')
        activeIPs = []
        for i in range(1, hosts_range):
            ip = IP.split('.')
            ip = f"{ip[0]}.{ip[1]}.{ip[2]}.{i}"


            # tcp scan
            if type == "TCP":
                logger.log(f'TCP pinging ip = {ip}', 'networkScanner')

                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # set a timeout
                socket.setdefaulttimeout(1)

                try:
                    # returns 0 if connection succeeds else raises error
                    if s.connect_ex((IP, port)) == 0:
                        activeIPs.append(IP)
                        logger.say(f'active device on {IP}')
                    else:
                        logger.log(f'no connection on {IP}:{port}', 'networkScanner')
                except:
                    logger.log(f'no connection on {IP}:{port}', 'networkScanner')

                s.close()


            # ping type scan
            elif type == "ICMP":
                    logger.log(f'ICMP pinging ip = {ip}', 'networkScanner')

                    #                                    -c --> 1 ping, -W --> timeout
                    pingResponse = subprocess.call(['ping', '-c', '1', '-W', '1', ip])
                    if pingResponse == 0:
                        logger.say(f'active device on {ip}')
                        activeIPs.append(ip)
                    elif pingResponse == 2:
                        logger.log(f"no response from {ip}", 'networkScanner')
                    else:
                        logger.log(f"ping to {ip} failed", 'networkScanner')

        if type == "ARP":
            IP = f"{IP}/{netMask}"
            arp = ARP(pdst=IP)
            # first is to create ARP request so that we can move forward
            broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
            arp_request_broadcast = broadcast / arp  # send and recieve the ARP requests

            answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)[0]  # and then extract device information from responses
            logger.log(f'answered_list = {answered_list}', 'networkScanner')


            for element in answered_list:
                device_info = {"ip": element[1].psrc, "mac": element[1].hwsrc}
                activeIPs.append(element[1].psrc)

        logger.log(f'\nactive ips: {activeIPs}', 'networkScanner')

        return 1
