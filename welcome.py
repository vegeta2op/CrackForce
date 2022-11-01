from ast import For
import imp
from colorama import Fore, Back, Style

import os
from time import sleep
f = open('hac.txt', 'r')
file_contents = f.read()

while True:
    print(Fore.RED+"\t\t\t\t\tWELCOME TO CRACKFROCER")
    print(Fore.GREEN+file_contents)
    print("Choose options\n")
    print(Fore.LIGHTRED_EX+Style.DIM+"1.md5 cracker\n"+Fore.GREEN+Style.DIM+"2.SHA1 Cracker\n"+Fore.LIGHTMAGENTA_EX+Style.DIM+"3.SSH Bruteforce\n"+Fore.LIGHTYELLOW_EX+Style.DIM+"4.FTP Bruteforce\n"+Fore.LIGHTBLUE_EX+Style.DIM+"5.Exit")
    choice= int(input(Style.BRIGHT+Fore.MAGENTA+"ENTER THE CHOICE:"))
    match choice:
        case 1:
            os.system('python md5crack.py')
            i=input(Style.NORMAL+"\nDo you want to exit?(y/N)")
            if i=='y' or i=='Y':
                print(Fore.WHITE+"Thank you")
                os.system('clear')
                exit()
            else:
                os.system('clear')
                
        case 2:
            os.system('python sha1crack.py')
            i=input("\nDo you want to exit?(y/N)")
            if i=='y' or i=='Y':
                print(Fore.WHITE+"Thank you")
                os.system('clear')
                exit()
            else:
                os.system('clear')
        case 3:
            os.system('python sshbrtf.py')
            i=input("\nDo you want to exit?(y/N)")
            if i=='y' or i=='Y':
                print(Fore.WHITE+"Thank you")
                os.system('clear')
                exit()
            else:
                os.system('clear')
        case 4:
            os.system('python bruteftp.py')
            i=input("\nDo you want to exit?(y/N)")
            if i=='y' or i=='Y':
                print(Fore.WHITE+"Thank you")
                os.system('clear')
                exit()
            else:
                os.system('clear')
        case 5:
            exit()
    