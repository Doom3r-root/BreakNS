# BreakNS
This tool creates and sends deauthentication packets to disconnect all devices from a specific WiFi access point. It uses channel hopping to maximize effectiveness across different WiFi channels and sends multiple deauthentication packets with different reason codes to ensure successful disconnection.

# Features:
- Automated channel hopping across common WiFi channels (1-13)
- Interactive interface selection
- Multiple operating modes
- Real-time packet counter

## Hardware Requirements

This tool requires a **wireless adapter with monitor mode support**.

Recommended setup:

- External USB Wi-Fi adapter
- Monitor mode support
- Linux-compatible chipset

Example interface names:

```txt
wlan1
wlan0
wlp2s0
```

Check your interface name:

```bash
iw dev
```

# Requirements : 
- Scapy library
- WiFi adapter with monitor mode and packet injection capabilities
- Root/sudo privileges

## Running

Run the script with root privileges:

```bash
sudo python3 breakns.py
```
