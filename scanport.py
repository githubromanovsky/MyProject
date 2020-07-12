import socket
import dns.resolver
from termcolor import colored


def scan_not_list_port():
    """Create socket for connect to host and port"""
    host = input("Host:")
    port = int(input("Port:"))
    # Create object socket
    scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Catch exceptions
    try:
        # Connected host and port
        scan.connect((host, port))
    except ConnectionRefusedError:
        print("_" * 30, "\n", "PORT", port, "[CLOSED]")
    except socket.gaierror:
        print(colored("You entered wrong host", host, 'red'))
    except OverflowError:
        print(colored("OverflowError: port must be 0-65535", port, 'red'))
    except OSError:
        print(colored("Your Network is unreachable", 'red'))
    else:
        print("_" * 30, "PORT", port, "[OPEN]", "\n")
    scan.close()


def scan_list_port():
    """Create socket for connect to host and port"""
    host = input("host:")
    print(colored("Enter a list elements separated by space", 'yellow'))
    # Create list ports
    port = [int(item) for item in input('Port:').split()]

    # Loop through the list of ports
    for i in port:
        scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Catch exceptions
        try:
            # for quick scan
            scan.settimeout(0.5)
            # Connected host and port
            scan.connect((host, i))
        except ConnectionRefusedError:
            print("_" * 30, "\n", "PORT", i, "[CLOSED]")
        except socket.gaierror:
            print(colored("You entered nonexistent host", 'red'))
        except OverflowError:
            print("OverflowError: port must be 0-65535", "Port:", i)
        else:
            print("_" * 30, "PORT", i, "[OPEN]")
        scan.close()


def dns_resolve():
    """DNS resolve A record"""
    try:
        name_site = input('Input site name:')
        result = dns.resolver.query(name_site, 'A')
    except dns.resolver.NoNameservers:
        print("Error dns resolver, server no name")
    except dns.resolver.NXDOMAIN:
        print("None of DNS query names exist")
    else:
        for ip in result:
            print('IP', ip.to_text())


while True:
    print(colored(r"""
     _____   _____   ____   ___ __  _____   ___   ______  ______
    / ____) /  ___) /  __\ (   (  \(  __ \ /   \ (   __ \(__  __)
    \____ \(  (___ /      \/      / )  __/(  O  ) )     /   )(
    (_____/ \_____)\__/\__/\__)___)(___)   \___/ (___\__)  (__)
             """, 'green'))
    print(colored(("*" * 50), 'blue'))
    print(colored("Select [1] to resolve A record DNS", 'green'))
    print(colored("Select [2] to scan the IPv4 port TCP type", 'green'))
    print(colored("Select [3] to scan the IPv4 port list TCP type", 'green'))
    print(colored("Select [4] to exit", 'green'))
    print(colored(("*" * 50), 'blue'))
    select = input("[Scan]:")
    if select == "1":
        dns_resolve()
        continue
    elif select == "2":
        scan_not_list_port()
        continue
    elif select == "3":
        scan_list_port()
        continue
    elif select == "4":
        exit()
    else:
        print(colored("You entered a nonexistent line item", 'red'))
