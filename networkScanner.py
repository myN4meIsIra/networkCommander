#
'''

'''

import subprocess


class Scanner:

    def __init__(self):
        return None

    def getOwnIP(self):
        return 1

    def scan(self, type, IP, netMask):

        # tcp scan
        if type == "TCP":
            return 1

        # ping type scan
        elif type == "ICMP":
            hosts_range = (2**(32-(int(netMask)))) - 2


            print(f'netMaskRange = {hosts_range}')
            for i in range(1,hosts_range):

                ip = IP.split('.')
                ip = f"{ip[0]}.{ip[1]}.{ip[2]}.{i}"

                print(f'pinging ip = {ip}')

                pingResponse = subprocess.call(['ping', '-c', '3', ip])
                print(f'pingResponse = {pingResponse}')
                if pingResponse == 0:
                    print("ping to", ip, "OK")
                elif pingResponse == 2:
                    print("no response from", ip)
                else:
                    print("ping to", ip, "failed!")

        return 1

        return 1
