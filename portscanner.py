import socket
import termcolor


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Port Opened " + str(port))
        sock.close()
    except:
        # print("[-] Port Closed " + str(port))
        pass


def scan(target, ports):
    print("\n Starting scan for {0}".format(target))
    for port in range(1, ports):
        scan_port(target, port)


targets = input("[*] Enter targets to scan (split them by ,): ")
ports = int(input("[*] Enter how many ports you want to scan: "))

if "," in targets:
    print(termcolor.colored("[*] Scanning multiple targets", 'green'))
    for ip_address in targets.split(","):
        scan(ip_address.strip(" "), ports)
else:
    print(termcolor.colored("[*] Scanning single target", 'green'))
    scan(targets.strip(" "), ports)
