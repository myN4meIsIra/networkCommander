#
'''

'''

import subprocess
import socket

# logging
from logging import Logging
logging = Logging(True)


class Scanner:

    def __init__(self):
        return None


    # get your own IP address
    def getOwnIP(self):
        IP = socket.gethostbyname(socket.gethostname())
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

            logging.log(f'netMaskRange = {hosts_range}', 'networkScanner')
            activeIPs = []
            for i in range(1,hosts_range):

                ip = IP.split('.')
                ip = f"{ip[0]}.{ip[1]}.{ip[2]}.{i}"

                logging.log(f'ICMP pinging ip = {ip}', 'networkScanner')

                pingResponse = subprocess.call(['ping', '-c', '1', ip])
                if pingResponse == 0:
                    logging.say(f'active device on {ip}', 'networkScanner')
                    activeIPs.append(ip)
                elif pingResponse == 2:
                    logging.log(f"no response from {ip}", 'networkScanner')
                else:
                    logging.log(f"ping to {ip} failed!", 'networkScanner')

            logging.log(f'\nactive ips: {activeIPs}', 'networkScanner')

        return 1
