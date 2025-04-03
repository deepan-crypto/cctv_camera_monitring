import nmap

def scan_network():
    nm = nmap.PortScanner()
    nm.scan(hosts="192.168.1.0/24", arguments="-p 554,80 --open")
    results = []
    for host in nm.all_hosts():
        results.append({
            "ip": host,
            "hostname": nm[host].hostname(),
            "open_ports": nm[host]["tcp"] if "tcp" in nm[host] else {},
        })
    return results