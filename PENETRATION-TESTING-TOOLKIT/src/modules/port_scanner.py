class PortScanner:
    def __init__(self):
        self.open_ports = []

    def scan(self, target):
        import socket
        for port in range(1, 65536):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                self.open_ports.append(port)
            sock.close()

    def get_open_ports(self):
        return self.open_ports