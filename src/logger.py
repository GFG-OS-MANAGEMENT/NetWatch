import logging
from pathlib import Path


class NetWatchLogger:
    """Save NetWatch alerts to a log file."""

    def __init__(self, log_file="logs/netwatch.log", level="INFO"):
        self.log_path = Path(log_file)
        self.log_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        logger_name = f"netwatch.{self.log_path.resolve()}"
        self.logger = logging.getLogger(logger_name)

        log_level = getattr(
            logging,
            level.upper(),
            logging.INFO
        )
        self.logger.setLevel(log_level)
        self.logger.propagate = False

        if not self.logger.handlers:
            handler = logging.FileHandler(
                self.log_path,
                encoding="utf-8"
            )

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s"
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def log_alert(self, alert):
        """Write a detected alert to the log file."""

        self.logger.info(
            "ALERT | severity=%s | type=%s | source=%s | "
            "destination_port=%s | %s",
            alert.get("severity", "unknown"),
            alert.get("type", "unknown"),
            alert.get("src_ip", "unknown"),
            alert.get("dst_port", "N/A"),
            alert.get("message", "")
        )