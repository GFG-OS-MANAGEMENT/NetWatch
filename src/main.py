import argparse
from pathlib import Path

import yaml

from src.analyzer import TrafficAnalyzer


def run_demo(analyzer):
    """Test NetWatch with simulated packet summaries."""

    print("NetWatch DEMO mode started.")
    print("Using simulated packets, not live network traffic.\n")

    packets = [
        {
            "src_ip": "192.0.2.10",
            "dst_ip": "198.51.100.20",
            "dst_port": 23,
            "length": 100,
            "tcp_flags": "",
        },
        {
            "src_ip": "192.0.2.11",
            "dst_ip": "198.51.100.20",
            "dst_port": 80,
            "length": 2500,
            "tcp_flags": "",
        },
    ]

    # Simulate a possible port scan.
    for port in range(1000, 1010):
        packets.append({
            "src_ip": "192.0.2.20",
            "dst_ip": "198.51.100.20",
            "dst_port": port,
            "length": 60,
            "tcp_flags": "S",
        })

    for index, packet in enumerate(packets):
        timestamp = 100 + index * 0.2

        print(
            f"Packet: {packet['src_ip']} -> "
            f"{packet['dst_ip']}:{packet['dst_port']} "
            f"(length={packet['length']})"
        )

        alerts = analyzer.analyze(packet, timestamp=timestamp)

        for alert in alerts:
            print(
                f"[ALERT] {alert['severity'].upper()} | "
                f"{alert['type']} | {alert['message']}"
            )

    print("\nNetWatch demo completed.")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--demo",
        action="store_true",
        help="Run using simulated packets",
    )
    args = parser.parse_args()

    with Path("config.yaml").open("r", encoding="utf-8") as file:
        config = yaml.safe_load(file) or {}

    analyzer = TrafficAnalyzer(
        config.get("rules_file", "rules/default_rules.json")
    )

    if args.demo:
        run_demo(analyzer)
        return

    from src.sniffer import PacketSniffer

    sniffer = PacketSniffer(
        analyzer=analyzer,
        interface=config.get("interface"),
        capture_filter=config.get("capture_filter", "ip"),
    )

    try:
        sniffer.start()
    except KeyboardInterrupt:
        print("\nNetWatch monitoring stopped.")
    except Exception as error:
        print(f"NetWatch could not start: {error}")


if __name__ == "__main__":
    main()