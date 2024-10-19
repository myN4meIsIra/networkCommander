#
'''

'''

import subprocess
import socket
import os

# logging
from logger import DataLogging
logger = DataLogging(True)


class Scanner:

    def __init__(self):
        return None


    # get your own IP address
    def getOwnIP(self):
        IP = ''
        ifconfig_os = os.system('ifconfig')
        ifconfig_subP = subprocess.call(['ifconfig'])
        logger.log(f'ifconfig_os --> {ifconfig_os}', "networkScanner")
        logger.log(f'ifconfig_subP --> {ifconfig_subP}', "networkScanner")

        return IP


    # scan the network for devices
    def scan(self, type, IP, netMask):

        # tcp scan
        if type == "TCP":
            return 1


        # ping type scan
        elif type == "ICMP":
            # #of hosts = 2^bits - 2 -- I have -1 because the range starts at 1, so the first -1 wouldn't be needed
            hosts_range = (2**(32-(int(netMask)))) - 1

            logger.log(f'netMaskRange = {hosts_range}', 'networkScanner')
            activeIPs = []
            for i in range(1,hosts_range):

                ip = IP.split('.')
                ip = f"{ip[0]}.{ip[1]}.{ip[2]}.{i}"

                logger.log(f'ICMP pinging ip = {ip}', 'networkScanner')

                pingResponse = subprocess.call(['ping', '-c', '1', ip])
                if pingResponse == 0:
                    logger.say(f'active device on {ip}')
                    activeIPs.append(ip)
                elif pingResponse == 2:
                    logger.log(f"no response from {ip}", 'networkScanner')
                else:
                    logger.log(f"ping to {ip} failed", 'networkScanner')

            logger.log(f'\nactive ips: {activeIPs}', 'networkScanner')

        return 1
