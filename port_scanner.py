import socket

def scan_ports(host, start_port, end_port):
    print(f"\nScanning {host} from port {start_port} to {end_port}...\n")
    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
            open_ports.append(port)
        sock.close()

    if not open_ports:
        print("No open ports found.")
    else:
        print(f"\nOpen ports: {open_ports}")

# Example usage
if __name__ == "__main__":
    target_host = input("Enter target IP or hostname: ")
    scan_ports(target_host, 20, 1024)
