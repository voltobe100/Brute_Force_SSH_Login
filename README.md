# Brute Force SSH Login – Automate SSH Login Attempts using Paramiko

## Overview

This project is a Python-based brute-force SSH login tool that attempts to gain access to a target machine by trying multiple username-password combinations. This tool is built using the `paramiko` library for SSH connections and can be used for educational or penetration testing purposes.

## Features

- Automate SSH login attempts.
- Load username and password combinations from a file.
- Detect successful login attempts.
- Display login attempt logs.
- Export results to a log file.

## Disclaimer

This tool is strictly for educational purposes or authorized penetration testing only. Unauthorized access to systems is illegal.

## Installation

Ensure Python is installed, then install the `paramiko` package:

```bash
pip install paramiko
```

## Usage

Run the script using the command:

```bash
python ssh_bruteforce.py --host <target_ip> --userlist users.txt --passlist passwords.txt
```

### Example

```bash
python ssh_bruteforce.py --host 192.168.1.100 --userlist users.txt --passlist passwords.txt
```

## Files Required

- `users.txt`: List of potential usernames.
- `passwords.txt`: List of potential passwords.

## Example Output

```bash
[+] Trying: admin:123456
[-] Failed
[+] Trying: root:toor
[+] Successful login: root:toor
```

## Logging Feature

The tool saves all successful logins in `ssh_bruteforce.log`.

## Legal Disclaimer

The use of this tool for attacking systems without prior consent is illegal. The creator is not responsible for any misuse or damage caused by this tool.
