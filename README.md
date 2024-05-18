# hophunter
A script that tries to detect an internal IP on the second hop of a traceroute, tests connectivity after setting the found IP as gateway, returns if your gateway is cheating you and "hops" the fake gateway.

hophunter detects potential issues with gateway redirection. It analyzes traceroute results to identify internal IPs on the second hop, then tests connectivity after setting the identified IP as the gateway. This helps ensure that your gateway is not maliciously redirecting traffic.

In my early days, when I connected to the library internet, I couldn't access many websites because of a firewall. Interestingly, it was a physical Fortinet firewall that was being redirected to as the supposed gateway. Doing a traceroute, I noticed that the second hop after the supposed gateway was 192.168.1.1. I tried manually setting the gateway to this address, and it completely bypassed the firewall control.

In other public networks, I've also noticed (especially by the page loading times) that a local MITM was taking place. With this tool, similarly, you can bypass the attacking device and connect directly to the gateway.

The script analyzes the network route using traceroute, identifies potential malicious redirections at the second hop, and verifies connectivity after establishing a new gateway, enabling the detection and mitigation of possible MITM attacks, captive portals, and unwanted firewalls.

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
