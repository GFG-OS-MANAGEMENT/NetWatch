from scapy.all import sniff, IP, TCP, UDP


class PacketSniffer:
    """Capture packet summaries and report detected alerts."""

    def __init__(
        self,
        analyzer,
        logger,
        interface=None,
        capture_filter="ip",
    ):
        self.analyzer = analyzer
        self.logger = logger
        self.interface = interface
        self.capture_filter = capture_filter

    def process_packet(self, packet):
        """Extract packet metadata and analyze it."""

        if IP not in packet:
            return

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        dst_port = None
        tcp_flags = ""
        protocol = "IP"

        if TCP in packet:
            protocol = "TCP"
            dst_port = int(packet[TCP].dport)
            tcp_flags = str(packet[TCP].flags)
        elif UDP in packet:
            protocol = "UDP"
            dst_port = int(packet[UDP].dport)

        packet_summary = {
            "src_ip": src_ip,
            "dst_ip": dst_ip,
            "dst_port": dst_port,
            "length": len(packet),
            "tcp_flags": tcp_flags,
        }

        print(
            f"{protocol}: {src_ip} -> {dst_ip} "
            f"port={dst_port} length={len(packet)}"
        )

        alerts = self.analyzer.analyze(packet_summary)

        for alert in alerts:
            print(
                f"[ALERT] {alert['severity'].upper()} | "
                f"{alert['type']} | {alert['message']}"
            )
            self.logger.log_alert(alert)

    def start(self):
        """Start live packet capture."""

        print("NetWatch packet monitoring started.")
        print("Press Ctrl+C to stop.")

        sniff(
            iface=self.interface,
            filter=self.capture_filter,
            prn=self.process_packet,
            store=False,
        )