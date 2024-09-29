# hophunter
A script that tries to detect an internal IP on the second hop of a traceroute, tests connectivity after setting the found IP as gateway, returns if your gateway is cheating you and "hops" the fake gateway. The script analyzes the network route using traceroute, identifies potential malicious redirections at the second hop, and verifies connectivity after establishing a new gateway, enabling the detection and mitigation of possible MITM attacks, captive portals, and unwanted firewalls.

### Note

It is entirely possible that with a well-configured network, the chances of hophunter operating reduce to zero. However, there are many poorly configured networks out there. Keep in mind that this is an update of an old program and may not always work.

### Features:
- Detects internal IPs on the second hop of traceroute.
- Tests connectivity after setting the identified IP as the gateway.
- Alerts if the gateway is potentially misdirecting traffic.
- "Jumps" the fake gateway.

### Requirements:
- Python 3.x
- Scapy library (`pip install scapy`)

### Usage:
1. Run the script.
2. Follow the prompts to enter the network adapter name if necessary.
3. hophunter will perform traceroute and test connectivity, alerting you if any issues are detected.
