# Contributing to NetWatch

Thank you for your interest in contributing to NetWatch!

NetWatch is a student-friendly cybersecurity project focused on network traffic monitoring, rule-based anomaly detection, and alert logging. Contributions from students and developers of all experience levels are welcome.

## What Can You Contribute?

You can contribute in several ways:

- **Python development:** Improve the analyzer, packet sniffer, logger, or configuration handling.
- **Cybersecurity and networking:** Suggest and implement detection rules.
- **Testing:** Add unit tests and test edge cases.
- **Documentation:** Improve the README, installation instructions, and technical explanations.
- **Bug fixes:** Investigate reported issues and submit fixes.
- **User interface:** Explore future ideas for displaying alerts and network activity.

Beginners are welcome. Documentation and testing are good places to start.

## Getting Started

### Prerequisites

- Python 3
- Git
- Visual Studio Code or another code editor

Npcap is required for live packet capture on Windows. The demo mode and automated tests do not require live packet capture.

### Set Up the Project on Windows

Clone the repository using its public GitHub URL:

```bash
git clone <repository-url>
cd NetWatch
```

Create a virtual environment:

```powershell
py -m venv venv
```

Install the dependencies:

```powershell
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

Run the demo:

```powershell
.\venv\Scripts\python.exe -m src.main --demo
```

Run the automated tests:

```powershell
.\venv\Scripts\python.exe -m unittest discover -s tests -v
```

Replace `<repository-url>` with the actual repository URL before using these instructions.

## Before You Start Contributing

1. Check existing issues to avoid duplicating work.
2. For larger changes, open an issue to discuss your proposed solution.
3. Choose a clearly defined task and agree on its scope before implementation.

## Making Changes

Create a separate branch for your contribution rather than working directly on `main`.

Example:

```bash
git switch -c feature/short-description
```

Make focused changes and follow the existing Python coding style.

When changing detection logic, include tests where appropriate. Document possible false positives and limitations of new rules.

Run the automated tests before submitting your changes.

## Commit and Submit Your Contribution

Stage the files you changed:

```bash
git add <files-you-changed>
```

Commit your work:

```bash
git commit -m "Describe your change"
```

Push your branch to your GitHub repository:

```bash
git push -u origin feature/short-description
```

If you are contributing through a fork, make sure you push the branch to your fork.

Open a pull request against the main NetWatch repository. Explain what you changed, why the change is useful, and which tests you ran. Include screenshots or example output when helpful.

Maintainers may request changes before accepting a contribution.

## Responsible Use

NetWatch is an educational project. Only monitor devices and networks that you own or have explicit permission to inspect.

Never commit credentials, API keys, private packet captures, or logs containing sensitive information. Do not contribute features intended for unauthorized access, covert surveillance, or credential theft.

Detection alerts are indicators for investigation, not proof of malicious activity.

## Thank You

Every useful contribution helps improve NetWatch and makes cybersecurity learning more accessible to students.

Thank you for being part of the project!