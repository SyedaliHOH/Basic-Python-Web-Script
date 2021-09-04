import os

print("Installing Dependencies: ")

try:

    os.system('sudo apt install python3-pip -y')
    os.system('pip3 install requests')
    os.system('pip3 install nmap')
    os.system('pip3 install --user python-nmap')
    os.system('pip3 install termcolor')

    print("\033[1;32;49mAll Dependencies Installed\033[0m")

except Exception as e:
    print("Error Occured:")
    print(e)

# Default Libaries:
# https://docs.python.org/3/library/
