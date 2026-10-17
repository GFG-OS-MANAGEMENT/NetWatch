import json
import time
from collections import defaultdict, deque
from pathlib import Path


class TrafficAnalyzer:
    """Apply configurable rules to network packet summaries."""

    def __init__(self, rules_path="rules/default_rules.json"):
        path = Path(rules_path)

        with path.open("r", encoding="utf-8") as file:
            self.rules = json.load(file)

        self.recent_syns = defaultdict(deque)
        self.alerted_sources = set()

    def analyze(self, packet, timestamp=None):
        """
        Analyze a packet summary and return any alerts.

        Expected fields:
        src_ip, dst_port, length, tcp_flags
        """
        alerts = []

        now = time.time() if timestamp is None else float(timestamp)
        src_ip = str(packet.get("src_ip", "unknown"))
        dst_port = packet.get("dst_port")
        tcp_flags = str(packet.get("tcp_flags", "")).upper()

        try:
            length = int(packet.get("length", 0))
        except (TypeError, ValueError):
            length = 0

        try:
            dst_port = int(dst_port) if dst_port is not None else None
        except (TypeError, ValueError):
            dst_port = None

        # Rule 1: Flag packets exceeding the configured size.
        max_size = self.rules.get("max_packet_size_bytes", 2000)

        if length > max_size:
            alerts.append({
                "type": "large_packet",
                "severity": "low",
                "src_ip": src_ip,
                "message": (
                    f"Packet size {length} bytes exceeds "
                    f"the configured threshold of {max_size} bytes."
                )
            })

        # Rule 2: Report traffic to configured watched ports.
        watched_ports = self.rules.get(
            "watched_destination_ports", []
        )

        if dst_port in watched_ports:
            alerts.append({
                "type": "watched_port",
                "severity": "info",
                "src_ip": src_ip,
                "dst_port": dst_port,
                "message": (
                    f"Traffic observed on watched destination "
                    f"port {dst_port}."
                )
            })

        # Remove expired SYN events from this source's time window.
        window = self.rules.get("port_scan_window_seconds", 10)
        events = self.recent_syns[src_ip]

        while events and now - events[0][0] > window:
            events.popleft()

        # Count distinct destination ports receiving TCP SYN packets.
        if tcp_flags in ("S", "SYN") and dst_port is not None:
            events.append((now, dst_port))

        unique_ports = {port for _, port in events}
        threshold = self.rules.get(
            "port_scan_unique_ports_threshold", 10
        )

        if len(unique_ports) >= threshold:
            if src_ip not in self.alerted_sources:
                alerts.append({
                    "type": "possible_port_scan",
                    "severity": "medium",
                    "src_ip": src_ip,
                    "message": (
                        f"Source contacted {len(unique_ports)} "
                        f"unique destination ports within "
                        f"{window} seconds using TCP SYN packets."
                    )
                })
                self.alerted_sources.add(src_ip)
        else:
            self.alerted_sources.discard(src_ip)

        return alerts