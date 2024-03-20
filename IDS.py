from scapy.all import *

def packet_callback(packet):
    try:
        if packet.haslayer(DNSQR):  # Corrected from DDNSQR to DNSQR
            # Extract information from the packet
            ip_src = packet[IP].src
            ip_dst = packet[IP].dst
            dns_query_name = packet[DNSQR].qname  # Corrected part

            # Log detected DNS requests
            print(f"[!] Detected DNS request from {ip_src} to {ip_dst}, Query: {dns_query_name.decode()}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Start sniffing the network
print("Starting IDS...")
sniff(prn=packet_callback, store=0)
