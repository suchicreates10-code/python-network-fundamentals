# Python Network Automation — Fundamentals

My learning journal as I start Python for network automation.  
Course: **NetworkKings — Python for Network Automation**  
Author: Sucharita Chakraborty | Senior Engineering Consultant.

---

## What this repo is

This is where I document my Python learning from scratch — with every exercise written around **real networking scenarios**: ARP tables, BGP AS numbers, SNMP data, MAC addresses, MTU values, and device records.

Every file has detailed comments explaining not just *what* the code does, but *why* — so future-me (and anyone reading this) can follow the thinking.

---

## Files in this repo

| File | Topic | Concepts covered |
|---|---|---|
| `01_variables_and_types.py` | Variables & data types | `str`, `int`, `float`, `bool`, `type()`, `.replace()` |
| `02_string_parsing.py` | ARP table parsing | `.split()`, list indexing, f-string alignment |
| `03_functions.py` | Functions | `def`, `return`, `try/except`, default args, `dict.get()` |

---

## How to run any file

No installs needed — uses only built-in Python.

```bash
python 01_variables_and_types.py
python 02_string_parsing.py
python 03_functions.py
```

---

## Sample output — ARP table parser

```
Raw input from router:
  Internet  10.220.88.29    94  5254.abbe.5b7b  ARPA  FastEthernet4

Parsed output:
             IP ADDR           MAC ADDRESS
  --------------------  --------------------
         10.220.88.29          5254.abbe.5b7b
         10.220.88.30          5254.ab71.e119
         10.220.88.32          5254.abc7.26aa
```

---

## Sample output — Device record builder

```
Input  (raw strings): cpu = '87.3'   bgp_as = '65100'   mtu = '9000'
Output (typed):       cpu = 87.3     bgp_as = 65100      mtu = 9000

  ALERT: CORE-RTR-01 — CPU at 87.3% (threshold: 80%)
```

---

## My learning path

- [x] Lecture 3 — Variables, strings, type conversion, functions
- [ ] Lecture 4 — Lists, sets, dictionaries
- [ ] Lecture 5 — Loops (for, while) + conditionals
- [ ] Lecture 6 — File I/O + JSON parsing
- [ ] Lecture 7 — Netmiko — SSH into real devices
- [ ] Lecture 8 — Ansible basics

---

## About me

15+ years in enterprise IT. Currently doing datacenter network implementation at Verizon India (Cisco Nexus, NX-OS, ACI). Building automation skills to complement hands-on DC work.

Certifications: CCNA | CompTIA Security+ | ITIL | Cisco AITECH  
Studying: CCNP DataCenter (350-601) | AUTOCOR (350-901)
