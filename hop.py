import scapy.all as scapy
import os
import subprocess
import time

def traceroute(host, max_hops=3):
    print(f"Tracerouting {host}, please wait...\n")
    second_hop_ip = None
    
    for ttl in range(1, max_hops + 1):
        pkt = scapy.IP(dst=host, ttl=ttl) / scapy.ICMP()
        reply = scapy.sr1(pkt, verbose=False, timeout=2)

        if reply is None:
            print(f"{ttl}\t* * * Request timed out.")
        elif reply.type == 0:   
            print(f"{ttl}\t{reply.src}\tDestination reached.")
            break
        else:
            print(f"{ttl}\t{reply.src}")

        if ttl == 2 and reply is not None:
            second_hop_ip = reply.src
            if is_internal_ip(reply.src):
                print(f"WARNING: The second hop redirects to an internal IP ({reply.src}). Let's try something... ")
                change_gateway(reply.src)
                return

    print("\n Seems normal...")

def is_internal_ip(ip):
    internal_ranges = [
        ('10.0.0.0', '10.255.255.255'),
        ('172.16.0.0', '172.31.255.255'),
        ('192.168.0.0', '192.168.255.255'),
        ('100.64.0.0', '100.127.255.255'), 
        ('169.254.0.0', '169.254.255.255')
    ]
    ip_num = ip_to_num(ip)
    for start, end in internal_ranges:
        if ip_to_num(start) <= ip_num <= ip_to_num(end):
            return True
    return False

def ip_to_num(ip):
    return int(''.join(['{:02x}'.format(int(octet)) for octet in ip.split('.')]), 16)

def get_current_gateway(interface):
    try:
        route_result = subprocess.check_output(f"ip route show dev {interface}", shell=True).decode()
        for line in route_result.splitlines():
            if 'default via' in line:
                return line.split()[2]
    except subprocess.CalledProcessError:
        pass
    return None

def set_gateway(interface, gateway):
    subprocess.run(f"sudo ip route add default via {gateway} dev {interface}", shell=True)

def delete_gateway(interface, gateway):
    subprocess.run(f"sudo ip route delete default via {gateway} dev {interface}", shell=True)

def ping_test():
    try:
        subprocess.check_output(['ping', '-c', '4', '8.8.8.8'], stderr=subprocess.STDOUT)
        return True
    except subprocess.CalledProcessError:
        return False

def change_gateway(new_gateway):
    interface = input("Network adapter name (i.ex. wlan0): ")
    current_gateway = get_current_gateway(interface)
    
    if current_gateway is None:
        print("Can't get current gateway...")
        return

    print(f"Current gateway: {current_gateway}")
    print(f"Changing gateway to: {new_gateway}") 
    delete_gateway(interface, current_gateway)
    set_gateway(interface, new_gateway)
    time.sleep(5)

    if ping_test():
        print(f"Test sucessful. Now your gateway is {new_gateway}.")
        print(f"Yes, it means a lot of things like MITM attacks, firewall, captive portals...")

    else:
        print(f"Test sucessful. Connection via {new_gateway} FAILED. Restoring original gateway..."
        delete_gateway(interface, new_gateway)
        set_gateway(interface, current_gateway)
        print("OK.")

if __name__ == "__main__":
    print("hophunter v.1.0 - github.com/disketteomelette")
    print("creative commons -- attribution, ok to derivatives, included commercial use")
    traceroute('google.com')
