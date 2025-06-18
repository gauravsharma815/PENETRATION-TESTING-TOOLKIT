import argparse
from modules.port_scanner import PortScanner
from modules.brute_forcer import BruteForcer
from utils.helpers import print_results, log_activity

def main():
    parser = argparse.ArgumentParser(description='Penetration Testing Toolkit')
    subparsers = parser.add_subparsers(dest='command')

    # Port Scanner
    port_parser = subparsers.add_parser('scan', help='Scan for open ports on a target')
    port_parser.add_argument('target', type=str, help='Target IP address or hostname')

    # Brute Forcer
    brute_parser = subparsers.add_parser('brute', help='Attempt to brute force login')
    brute_parser.add_argument('target', type=str, help='Target URL for login')
    brute_parser.add_argument('username', type=str, help='Username for login')
    brute_parser.add_argument('password_list', type=str, help='Path to password list file')

    args = parser.parse_args()

    if args.command == 'scan':
        scanner = PortScanner()
        scanner.scan(args.target)
        open_ports = scanner.get_open_ports()
        print_results(open_ports)
        log_activity(f'Scanned {args.target} for open ports.')

    elif args.command == 'brute':
        with open(args.password_list, 'r') as file:
            passwords = file.read().splitlines()
        
        for password in passwords:
            response = BruteForcer().attempt_login(args.target, args.username, password)
            if BruteForcer().is_successful(response):
                print(f'Successful login with password: {password}')
                log_activity(f'Successful login on {args.target} with password: {password}')
                break
        else:
            print('No successful login found.')
            log_activity(f'Failed to login on {args.target} with provided password list.')

if __name__ == '__main__':
    main()