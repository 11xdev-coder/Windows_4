import scapy.all as scapy
request = scapy.ARP()
request.pdst = '192.168.254.1/24'
broadcast = scapy.Ether()
broadcast.hwdst = 'ff:ff:ff:ff:ff:ff'
packet = request/broadcast
client = scapy.srp(packet, timeout=3, verbose=0)
print("Ip" + " " * 18 + "Mac")
for sent, received in client:
    print(f"{received.psrc}" + " " * 18+f"{received.hwsrc}")
