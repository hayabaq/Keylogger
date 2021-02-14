#!/usr/bin/env python
import scapy.all as scapy 

def scan(ip):
    #
    arp_req= scapy.ARP(pdst=ip)
    #print summary
    #print(arp_req.summary())
    #list attributes and their values
    #scapy.ls(scapy.ARP())
    #Send broadcast packet
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether())
    #print(broadcast.summary())
    req_broadcast=broadcast/arp_req
    #print(req_broadcast.summary())
    #req_broadcast.show()
    scapy.srp(req_broadcast, timeout=1)
    ans , unans= scapy.srp(req_broadcast, timeout=1)
    print(ans.summary())
    print(unans.summary())
scan('10.0.2.1/24')