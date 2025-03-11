# Nuclei Installer for Kali Linux
![image](https://github.com/user-attachments/assets/c91c24e5-8f50-4f9d-9289-5e5d09f680a1)

## Overview
This Python script automates the installation and setup of **Nuclei**, a fast and customizable vulnerability scanner, on **Kali Linux**. The script ensures that your system is updated, installs **Golang**, installs **Nuclei**, and updates its templates.

## Features
- **Automated installation** of Nuclei and its dependencies.
- **Ensures the latest version** of Golang is installed.
- **Updates Nuclei templates** to have the latest security checks.
- **Error handling** to ensure smooth execution.

## Prerequisites
Make sure you have **Kali Linux** installed and have `sudo` privileges before running the script.

## Installation & Usage
1. Clone the repository:
   ```bash
   https://github.com/vivekbhatt3011/NucleiInstallationScript.git
   cd nuclei-installer
   ```

2. Run the script:
   ```bash
   python3 install_nuclei.py
   ```

## How It Works
The script performs the following tasks:
1. **Updates your system** using `apt update && apt upgrade -y`.
2. **Installs Golang**, a requirement for running Nuclei.
3. **Installs Nuclei** using Go's package manager.
4. **Moves Nuclei to a system-wide location** for easier access.
5. **Updates Nuclei templates** to ensure the latest security checks are available.

## Verification
After installation, you can verify Nuclei is working by running:
```bash
nuclei -version
```
