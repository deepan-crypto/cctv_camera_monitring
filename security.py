import os
import platform

def block_ip(ip_address):
    if platform.system() == "Linux":
        os.system(f"sudo iptables -A INPUT -s {ip_address} -j DROP")
    else:
        print("This function is only supported on Linux systems.")
