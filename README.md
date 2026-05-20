# BreakNS
This tool creates and sends deauthentication packets to disconnect all devices from a specific WiFi access point. It uses channel hopping to maximize effectiveness across different WiFi channels and sends multiple deauthentication packets with different reason codes to ensure successful disconnection.

# Features:
- Automated channel hopping across common WiFi channels (1-11)
- Sends deauthentication packets with multiple reason codes (1, 4, 7)
- Real-time packet counter
- Clean interface setup and teardown

## Hardware Requirements

This tool requires a **wireless adapter with monitor mode support**.

Recommended setup:

- External USB Wi-Fi adapter
- Monitor mode support
- Linux-compatible chipset

Default interface used in the script:

```txt
wlan1
```

If your wireless interface name is different (for example `wlan0` or `wlp2s0`), edit this line inside the script:

```python
INTERFACE = "wlan1"
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
