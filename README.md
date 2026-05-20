# BreakNS
This tool creates and sends deauthentication packets to disconnect all devices from a specific WiFi access point. It uses channel hopping to maximize effectiveness across different WiFi channels and sends multiple deauthentication packets with different reason codes to ensure successful disconnection.

Features
- Automated channel hopping across common WiFi channels (1-11)
- Sends deauthentication packets with multiple reason codes (1, 4, 7)
- Real-time packet counter
- Clean interface setup and teardown

Requirements : 
1. Scapy library
2. WiFi adapter with monitor mode and packet injection capabilities
3. Root/sudo privileges
