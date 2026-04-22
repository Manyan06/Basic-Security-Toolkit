# pip install scapy
# or py -m pip install scapy

# Pre-requisites: Download - https://npcap.com/#download

from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw  # type: ignore[import]

def process_packet(packet):
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        protocol = ip_layer.proto

        proto_name = "Other"
        src_port = "-"
        dst_port = "-"

        if TCP in packet:
            proto_name = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport

        elif UDP in packet:
            proto_name = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport

        elif ICMP in packet:
            proto_name = "ICMP"

        print("\n=== Packet Captured ===")
        print(f"Source IP      : {src_ip}")
        print(f"Destination IP : {dst_ip}")
        print(f"Protocol       : {proto_name}")
        print(f"Source Port    : {src_port}")
        print(f"Destination Port: {dst_port}")

        # Payload (if exists)
        if Raw in packet:
            payload = packet[Raw].load
            try:
                decoded = payload.decode(errors="ignore")
                print(f"Payload (preview): {decoded[:100]}")
            except:
                print("Payload: [Non-decodable data]")

def main():
    print("Starting packet sniffer... (Press Ctrl+C to stop)")
    
    sniff(
        prn=process_packet,
        store=False
    )

if __name__ == "__main__":
    main()


# # Output :
# === Packet Captured ===
# Source IP      : 192.168.0.103
# Destination IP : 140.82.112.21
# Protocol       : TCP
# Source Port    : 65516
# Destination Port: 443
# e0|үC7/14X<{c`=^K ޳ujbBA^CnSy,#ޠR<ŝ}\P\e95u[.d~`"Hx:畗n
#                                                        hC}-D#]\V

# === Packet Captured ===
# Source IP      : 140.82.112.21
# Destination IP : 192.168.0.103
# Protocol       : TCP
# Source Port    : 443
# Destination Port: 65516

# === Packet Captured ===
# Source IP      : 140.82.112.21
# Destination IP : 192.168.0.103
# Protocol       : TCP
# Source Port    : 443
# Destination Port: 65516

# === Packet Captured ===
# Source IP      : 140.82.112.21
# Destination IP : 192.168.0.103
# Protocol       : TCP
# Source Port    : 443
# Destination Port: 65516
# Payload (preview): +F5JGt
# FX?Â}v: NޫCj