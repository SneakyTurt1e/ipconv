# Introduction
- A script to convert Dot-decimal IP addresses to Hex Binary or Octal[Based on Python3].

# Features
```
  -h, --help            show this help message and exit
  -i ip, --ip ip        IP Address[Do not support IPV6]
  -t type, --type type  Convert type:bin oct hex
 ```

#  Usage
```bash
python ipconv.py -i IP -t TYPE
```

# Example
```
root@kali:~# python3 ipconv.py -i 127.0.0.1 -t hex
Origin IP:127.0.0.1
Convert IP:0x7f000001
root@kali:~# python3 ipconv.py -i 127.0.0.1 -t bin
Origin IP:127.0.0.1
Convert IP:2130706433
root@kali:~# python3 ipconv.py -i 127.0.0.1 -t oct
Origin IP:127.0.0.1
Convert IP:017700000001
```
