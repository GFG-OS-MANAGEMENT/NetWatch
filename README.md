# NetWatch

**NetWatch** is an open-source, student-friendly cybersecurity project focused on network traffic monitoring and basic rule-based anomaly detection.

Built around foundational Data Communication and Networking (DCN) concepts, NetWatch helps students explore packet metadata, identify traffic patterns that match configurable detection rules, and review generated security alerts.

The project is designed as a collaborative learning platform where students can contribute to Python development, networking, cybersecurity research, testing, and documentation.

## Features

- **Live Packet Monitoring:** Capture and inspect network packet metadata using Scapy.
- **Rule-Based Detection:** Flag packets that exceed a configured size threshold, traffic to watched destination ports, and possible TCP SYN port scans.
- **Demo Mode:** Run simulated packet scenarios without requiring live packet capture.
- **Alert Logging:** Record detected alerts with timestamps, severity, source addresses, and descriptive messages.
- **Automated Tests:** Test core detection logic using Python's `unittest` framework.
- **Student Contributions:** Encourage collaborative development through issues, branches, and pull requests.

> **Current project status:** NetWatch is an early-stage educational prototype. Detection rules are basic indicators, and alerts do not prove that malicious activity has occurred. Advanced detection capabilities and a graphical dashboard may be considered for future development.

## Technology Stack

- Python
- Scapy
- PyYAML
- Git and GitHub
- Npcap for live packet capture on Windows

## Project Structure

```text
NetWatch/
├── README.md
├── CONTRIBUTING.md
├── requirements.txt
├── config.yaml
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── sniffer.py
│   ├── analyzer.py
│   └── logger.py
├── tests/
│   ├── __init__.py
│   └── test_analyzer.py
├── rules/
│   └── default_rules.json
└── logs/
```

The `venv/` directory is created locally during setup and should not be committed to Git.

## Getting Started

### Prerequisites

- Python 3
- Git
- A code editor such as Visual Studio Code
- Npcap on Windows for live packet capture

### 1. Clone the Repository

```bash
git clone https://github.com/GFG-OS-MANAGEMENT/NetWatch.git
cd NetWatch
```

### 2. Create a Virtual Environment

On Windows PowerShell:

```powershell
py -m venv venv
```

### 3. Install Dependencies

```powershell
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 4. Run Demo Mode

Demo mode uses simulated packet summaries and does not require live packet capture.

```powershell
.\venv\Scripts\python.exe -m src.main --demo
```

The demonstration exercises the watched-port, large-packet, and possible-port-scan detection rules.

### 5. Run the Automated Tests

```powershell
.\venv\Scripts\python.exe -m unittest discover -s tests -v
```

The tests validate the implemented analyzer scenarios.

### 6. Start Live Packet Monitoring

After installing Npcap and completing any required Windows permissions setup, run:

```powershell
.\venv\Scripts\python.exe -m src.main
```

Press `Ctrl + C` to stop monitoring.

Live packet capture can require administrator privileges depending on your system configuration. Only monitor devices and networks you own or are authorized to inspect.

## Alert Logging

NetWatch records generated alerts in:

```text
logs/netwatch.log
```

The log includes timestamps, alert severity, alert type, source address, destination port when applicable, and the alert description.

Log files are generated locally and should not be committed to the repository.

## Contributing

NetWatch welcomes contributions from students and developers interested in Python, computer networks, cybersecurity, testing, and documentation.

You can help by:

- Fixing bugs and improving existing code.
- Adding automated tests.
- Improving detection rules and documenting their limitations.
- Improving setup instructions and technical documentation.
- Proposing future features through GitHub issues.

Before contributing, read the [Contribution Guidelines](CONTRIBUTING.md).

## Roadmap

Potential areas for future contributions include:

- More robust detection rules and false-positive evaluation.
- Improved configuration validation and error handling.
- Additional automated tests.
- Better alert filtering and reporting.
- A graphical dashboard for reviewing network activity.
- Cross-platform setup and testing improvements.

These are proposed improvements, not currently completed features.

## Responsible Use

NetWatch is intended for cybersecurity education and authorized network monitoring.

Detection alerts are indicators for investigation, not proof of an attack. Do not use the project to monitor networks without permission, collect sensitive information unnecessarily, or perform unauthorized security activities.

## License

A license has not yet been specified. Licensing information will be added once the project maintainers select and commit an open-source license.

## Acknowledgements

NetWatch is a collaborative learning initiative intended to help students strengthen their understanding of Python, computer networks, and cybersecurity through practical development.
