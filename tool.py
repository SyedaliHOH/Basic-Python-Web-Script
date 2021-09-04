
#Importing Libaries:

import sys, nmap, socket, argparse, re
import requests, requests.exceptions
from requests.exceptions import MissingSchema
from termcolor import colored, cprint

#Defining basic-info:

wrong_sc = 401, 402, 403, 404, 405, 406, 500, 501, 502, 503, 504, 505

exit = colored('[-]Exiting...', 'red', attrs=['bold'])
pos = colored("[+] ","green", attrs=['bold'])
neg = colored("[-] ","red", attrs=['bold'])

info = colored('[INFO]','white')
warn = colored('[WARNING] ', 'yellow')
error = colored('[ERROR] ', 'red')
success = colored('[SUCCESS] ', 'green')


#Taking Main input and args

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="URL here, https://example.com", required=True)
# parser.add_argument("-p", action='store_true', help="Do Port Scan, REMEMBER while using this dont include port: https://example.com:4000")

args = parser.parse_args()
target = args.url

#Validating URL:

try:
    response = requests.get(target, timeout=10)
    status_code = response.status_code

    if status_code in wrong_sc:
        print(f"{warn}Response Code is {status_code}, its in 4xx/5xx(error).")
        invalid_sc = input("Are u sure you want to continue (y,n)? ")

        if invalid_sc == "y":
            pass
        else:
            raise SystemExit

except MissingSchema:
    print(f"URL is in bad format, perphaps you mean: http://{target}")
    print(exit)
    raise SystemExit

except requests.exceptions.RequestException as e:
    print("Connection Error:")
    raise SystemExit(e)
    print(exit)

except KeyboardInterrupt:
    print(colored("\n[-]User Interrepted","red", attrs=['bold']))
    raise SystemExit

except:
    print(exit)
    raise SystemExit


#Basic Result:

targ = re.sub(r'https://www\.|http://www\.|https://www|http://|https://|www\.', "", target).strip('/')
print(targ)

host = socket.gethostbyname(targ)
scanner = nmap.PortScanner()

port = 0

result = socket.getaddrinfo("example.org", socket.IPPROTO_TCP)

def basic_info(host):

    scanner.scan(targ, '1')

    IPV6 = socket.getaddrinfo(targ, port, socket.AF_INET6)
    protocols = ', '.join(map(str, scanner[host].all_protocols()))

    print("\nStatus:\t\t "+ colored(scanner[host].state().upper(), "green"))
    print("Hostname:\t", scanner[host].hostname())
    print("IP:\t\t", host)
    print("IPV6:\t\t", IPV6[0][4][0])
    print("Protocols:\t", protocols)
    print("Status Code:\t", colored(response.status_code, "green"))

print(f"{pos}Retriving Basic Info")

basic_info(host)

