# Class to store node information and neighbors
import socket


class node:
    def __init__(self, ip, domain, links):
        self.ip_addr = ip
        self.domain = domain
        self.links = {}
        self.links = links
        self.spf = {}
        self.spf[self.ip_addr] = {self.ip_addr: 0}
        for l in links:
            ip = l.split(':')[0]
            self.spf[self.ip_addr][ip + ':13800'] = int(l.split(':')[1])

    def get_links(self):
        return self.links

    def get_spf(self):
        return self.spf
    
    def get_ip(self):
        return self.ip_addr
