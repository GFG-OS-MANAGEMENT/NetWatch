import unittest

from src.analyzer import TrafficAnalyzer


class TestTrafficAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = TrafficAnalyzer()

    def test_watched_port(self):
        packet = {
            "src_ip": "192.0.2.10",
            "dst_port": 23,
            "length": 100,
            "tcp_flags": ""
        }

        alerts = self.analyzer.analyze(packet, timestamp=100)

        self.assertTrue(
            any(alert["type"] == "watched_port" for alert in alerts)
        )

    def test_large_packet(self):
        packet = {
            "src_ip": "192.0.2.10",
            "dst_port": 80,
            "length": 2500,
            "tcp_flags": ""
        }

        alerts = self.analyzer.analyze(packet, timestamp=100)

        self.assertTrue(
            any(alert["type"] == "large_packet" for alert in alerts)
        )

    def test_possible_port_scan(self):
        alerts = []

        for port in range(1000, 1010):
            packet = {
                "src_ip": "192.0.2.20",
                "dst_port": port,
                "length": 60,
                "tcp_flags": "S"
            }

            alerts.extend(
                self.analyzer.analyze(
                    packet,
                    timestamp=100 + (port - 1000) * 0.2
                )
            )

        self.assertTrue(
            any(
                alert["type"] == "possible_port_scan"
                for alert in alerts
            )
        )


if __name__ == "__main__":
    unittest.main()