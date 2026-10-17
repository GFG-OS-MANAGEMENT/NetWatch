# NetWatch

**NetWatch** is a beginner-friendly, lightweight cybersecurity tool designed to monitor and analyze network traffic, identify unusual patterns, and alert users to potential security threats. 

By combining foundational **Data Communication and Networking (DCN)** concepts with rule-based anomaly detection, NetWatch provides straightforward traffic insights without the complexity of enterprise-grade SIEM tools.

---

## Features

* **Real-Time Packet Monitoring:** Capture and inspect live network packets.
* **Rule-Based Anomaly Detection:** Flag suspicious activities such as unusual traffic spikes, repeated failed connection attempts, or unauthorized port scans.
* **DCN-Focused Insights:** Learn and visualize core networking concepts (TCP/IP headers, packet flags, subnet behavior) in action.
* **Customizable Security Rules:** Easily add or modify detection rules via a simple configuration file.
* **Lightweight & Beginner-Friendly:** Built with clean, readable code and minimal dependencies to help students and aspiring security professionals learn network security fundamentals.

---

## Getting Started

### Prerequisites

* Python 3.8+
* `pip` package manager
* Administrator/Root privileges (required for raw socket packet capture on most operating systems)

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/netwatch.git](https://github.com/your-username/netwatch.git)
   cd netwatch

2. Install dependencies:
---Bash
pip install -r requirements.txt

3. Run NetWatch:
---Bash
sudo pytho n3 src/main.py 

4. Usage
Bash
python3 src/main.py --interface eth0 --rules rules/default_rules.json

## Contributing
We welcome contributions from the community! Please read our [CONTRIBUTING.md](./Contributing.md) to learn how you cacn help in building NetWatch.


## CODE_OF_CONDUCT.md

```markdown
# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to 
make participation in our community a harassment-free experience for everyone, regardless of age, body size, visible or invisible disability, ethnicity, sex characteristics, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, race, religion, or sexual identity and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming, diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes, learning from the experience
* Focusing on what is best not just for us as individuals, but for the overall community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or advances of any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of acceptable behavior and will take appropriate and fair corrective action in response to any behavior that they deem inappropriate, threatening, offensive, or harmful.

## Scope

This Code of Conduct applies within all community spaces, and also when an individual is officially representing the community in public spaces.
  
## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported to the community leaders responsible for enforcement at [Insert Contact Email]. All complaints will be reviewed and investigated promptly and fairly.