import socket
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


def scan_list_port():
    host = input("host:")
    print(colored("Enter a list elements separated by space", 'yellow'))
    # port = []
    # Create list ports
    port = [int(item) for item in input('Port:').split()]
    # port = [89000, 20, 22, 23, 21, 666, 45, 6942]
    # Проходим в цикле по списку портов

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


while True:
    print(colored(r"""
     _____   _____   ____   ___ __  _____   ___   ______  ______
    / ____) /  ___) /  __\ (   (  \(  __ \ /   \ (   __ \(__  __)
    \____ \(  (___ /      \/      / )  __/(  O  ) )     /   )(
    (_____/ \_____)\__/\__/\__)___)(___)   \___/ (___\__)  (__)
             """, 'green'))
    print(colored(("*" * 50), 'blue'))
    print(colored("Select [1] to scan the IPv4 port TCP type", 'green'))
    print(colored("Select [2] to scan the IPv4 port list TCP type", 'green'))
    print(colored("Select [3] to exit", 'green'))
    print(colored(("*" * 50), 'blue'))
    text_a = input("[Scan]:")
    if text_a == "1":
        scan_list_port()
        continue
    elif text_a == "2":
        scan_not_list_port()
        continue
    elif text_a == "3":
        exit()
    else:
        print(colored("You entered a nonexistent line item", 'red'))
