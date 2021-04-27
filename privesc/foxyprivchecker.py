#!/usr/bin/python3
# Linux PrivEsc Script
# Wrriten By. Jessi
# Version: 0.1
# Github: https://github.com/jessisec
# Twitter: @jessitakes
# Usage: python3 foxyprivchecker.py

import time
import os
import sys
import getpass
from datetime import datetime

# Print Intro
print("""\


                                                                   ,-,
                                                             _.-=;~ /_
                                                          _-~   '     ;.
                                                      _.-~     '   .-~-~`-._
                                                _.--~~:.             --.____88
                              ____.........--~~~. .' .  .        _..-------~~
                     _..--~~~~               .' .'             ,'
                 _.-~                        .       .     ` ,'
               .'                                    :.    ./
             .:     ,/          `                   ::.   ,'
           .:'     ,(            ;.                ::. ,-'
          .'     ./'.`.     . . /:::._______.... _/:.o/
         /     ./'. . .)  . _.,'               `88;?88|
       ,'  . .,/'._,-~ /_.o8P'                  88P ?8b
    _,'' . .,/',-~    d888P'                    88'  88|
 _.'~  . .,:oP'        ?88b              _..--- 88.--'8b.--..__
:     ...' 88o __,------.88o ...__..._.=~- .    `~~   `~~      ~-._ Seal _.
`.;;;:='    ~~            ~~~                ~-    -       -   -""")
print("\n")
print("/***********************************/")
print("Foxy Priv Checker!")
print("A very simple linux privesc script :)")
print("Written by. Jessi <3")
print("Github: https://github.com/jessisec")
print("Twitter: @jessitakes")
print("/***********************************/")
print("\n")

# Disclaimer
print("Note: This script WILL NOT auto exploit OR tell you exactly what to do...")
print("This is for enumeration purposes only!")
print("\n")
time.sleep(6)

# Get start time and begin!
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("/******************************/")
print("Script Start Time: " + current_time+"")
print("/******************************/")
print("\n")

# Check whoami and id
print("/***************************/")
print("Getting current user stats...")
print("/***************************/")
print("\n")
current_user = os.system("whoami; id; groups")
print("\n")

# Check OS and Kernel
print("/***********************/")
print("Checking OS and Kernel...")
print("/***********************/")
print("\n")
os_version = os.system("cat /etc/issue")
kernel = os.system("uname -a")
print("\n")

# Check /etc/passwd
print("/*********************/")
print("Checking /etc/passwd...")
print("/*********************/")
print("\n")
passwd_file = os.system("cat /etc/passwd")
print("\n")

# Check SUIDs
print("/***************/")
print("Checking SUIDs...")
print("/***************/")
print("\n")
suids = os.system("find / -perm -u=s -type f 2>/dev/null")
print("\n")

# Check Crontab
print("/******************/")
print("Checking crontab...")
print("/******************/")
print("\n")
crontab = os.system("cat /etc/crontab")
print("\n")

# Check netstat
print("/******************/")
print("Checking netstat...")
print("/******************/")
print("\n")
netstat = os.system("netstat -an")

# Check for file permissions
user = getpass.getuser()
print("/******************************************/")
print("Checking file permissions for " + user+"...")
print("/******************************************/")
print("\n")
file_perms = os.system("find / -type f -group " + user+" 2>/dev/null")
print("\n")

# Check for files containing current user in /etc
print("/******************************************/")
print("Checking for files containing " + user+"...")
print("/******************************************/")
print("\n")
files_cont = os.system("grep "+ user+" /etc -R 2>/dev/null")
print("\n")

# Check for usernames in /etc
print("/***************************************/")
print("Checking for 'username' string in /etc...")
print("/***************************************/")
print("\n")
users_etc = os.system("grep username /etc -R 2>/dev/null")
print("\n")

# Check for passwords in /etc
print("/***************************************/")
print("Checking for 'password' string in /etc...")
print("/***************************************/")
print("\n")
pass_etc = os.system("grep password /etc -R 2>/dev/null")
print("\n")

# Check for usernames in /var/log
print("/************************************/")
print("Checking for 'username' in /var/log...")
print("/************************************/")
print("\n")
users_log = os.system("grep username /var/log -R 2>/dev/null")
print("\n")

# Check for passwords in /var/log
print("/************************************/")
print("Checking for 'password' in /var/log...")
print("/************************************/")
print("\n")
pass_log = os.system("grep password /var/log -R 2>/dev/null")
print("\n")

# Check for usernames in /var/www
print("/************************************/")
print("Checking for 'username' in /var/www...")
print("/************************************/")
print("\n")
users_www = os.system("grep username /var/www -R 2>/dev/null")
print("\n")

# Check for passwords in /var/www
print("/************************************/")
print("Checking for 'password' in /var/www...")
print("/************************************/")
print("\n")
pass_www = os.system("grep password /var/www -R 2>/dev/null")
print("\n")

# Get End Time
end = datetime.now()
end_time = end.strftime("%H:%M:%S")
print("/**********************/")
print("Done! Happy hacking! :)")
print("Script End Time: " + end_time+"")
print("/**********************/")
