# SSRF Internal Port Scanner

A Python tool that exploits a Server-Side Request Forgery (SSRF) vulnerability to perform internal network port scanning, enumerating open ports on internal hosts (e.g., `127.0.0.1`) that are otherwise unreachable from the external network.

---

## How it works

The script sends POST requests to a vulnerable SSRF endpoint, embedding a crafted internal URL (`http://127.0.0.1:<port>`) in the JSON payload. It then analyzes the server's JSON response to infer whether the target port is open, based on the `status` and `message` fields returned. A persistent `requests.Session` is reused across all requests for efficiency.

---

## Configuration

Before running the script, update the following variables at the top of the file:

| Variable | Description |
|----------|-------------|
| `URL` | Full URL of the vulnerable SSRF endpoint |
| `TOKEN` | Admin token required by the API |
| `TARGET` | Internal host to scan (default: `http://127.0.0.1`) |
| `PORTS` | List of ports to probe |

---

## Requirements

```bash
pip install requests
```

---

## Usage

```bash
python3 SSRF_API_Port_Scanning.py
```

Example output:

```
[*] SSRF port scan on http://127.0.0.1

Port    22 | OPEN ✓ | message preview: SSH-2.0-OpenSSH_8.9p1
Port    80 | OPEN ✓ | message preview: <html>...
Port   443 | closed
Port  3306 | closed
...

[+] Open ports found: 2
 -> 22 | content length: 30 chars
 -> 80 | content length: 512 chars
```

**Disclaimer:** This tool is intended for **authorized security testing only**. Unauthorized use against systems you do not own or have explicit written permission to test is illegal and unethical.
