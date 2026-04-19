"""
02_string_parsing.py
---------------------
NetworkKings | Python for Network Automation
Lecture 3 — Python Fundamentals | Practice Task 1

Topic  : String methods — split(), f-strings, column alignment
Author : Sucharita Chakraborty

Real world use: Routers and switches output everything as raw text.
To automate tasks, you must PARSE that text to extract just the
fields you need (IP, MAC, interface, etc.)

Run it : python 02_string_parsing.py
"""

print("=" * 60)
print("LESSON 2 — Parsing ARP Table Output from a Router")
print("=" * 60)


# ==============================================================
# THE PROBLEM
#
# When you run "show arp" on a Cisco router, you get raw text
# like this. Each line is one long string — you need to extract
# just the IP address and MAC address from it.
# ==============================================================

print("\n--- Raw ARP table output (as it comes from the router) ---\n")

mac1 = "Internet  10.220.88.29          94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30           3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32         231   5254.abc7.26aa  ARPA   FastEthernet4"

print(f"  mac1: {mac1}")
print(f"  mac2: {mac2}")
print(f"  mac3: {mac3}")


# ==============================================================
# STEP 1 — Understand split()
#
# CONCEPT: .split() breaks a string into a LIST of words,
#          splitting wherever there's whitespace (spaces, tabs).
#
# "Internet  10.220.88.29   94   5254.abbe.5b7b  ARPA  Fa4"
#  [0]        [1]           [2]  [3]              [4]   [5]
#
# fields[1] = the IP address
# fields[3] = the MAC address
# ==============================================================

print("\n--- STEP 1: How split() works ---\n")

example = mac1
fields  = example.split()           # splits on any whitespace

print(f"  split() gives us a list with {len(fields)} items:")
for index, value in enumerate(fields):
    print(f"    fields[{index}] = {value!r}")


# ==============================================================
# STEP 2 — Extract IP and MAC from all three lines
#
# CONCEPT: Once we know the index positions, we extract
#          exactly what we need using list indexing.
# ==============================================================

print("\n--- STEP 2: Extract IP and MAC from each line ---\n")

# Parse mac1
fields1  = mac1.split()
ip_addr1 = fields1[1]               # index 1 = IP address
mac_addr1 = fields1[3]              # index 3 = MAC address

# Parse mac2
fields2  = mac2.split()
ip_addr2 = fields2[1]
mac_addr2 = fields2[3]

# Parse mac3
fields3  = mac3.split()
ip_addr3 = fields3[1]
mac_addr3 = fields3[3]

print(f"  Extracted from mac1 → IP: {ip_addr1}   MAC: {mac_addr1}")
print(f"  Extracted from mac2 → IP: {ip_addr2}   MAC: {mac_addr2}")
print(f"  Extracted from mac3 → IP: {ip_addr3}   MAC: {mac_addr3}")


# ==============================================================
# STEP 3 — Print a clean formatted table
#
# CONCEPT: f-string alignment
#   {value:>20}  → right-align in a 20-character column
#   {value:<20}  → left-align  in a 20-character column
#   {value:^20}  → center      in a 20-character column
#
# This is how you make output look neat and professional.
# ==============================================================

print("\n--- STEP 3: Print a formatted IP → MAC table ---\n")

# Header row
print(f"  {'IP ADDR':>20}  {'MAC ADDRESS':>20}")
print(f"  {'-' * 20}  {'-' * 20}")

# Data rows — right-aligned in 20-character columns
print(f"  {ip_addr1:>20}  {mac_addr1:>20}")
print(f"  {ip_addr2:>20}  {mac_addr2:>20}")
print(f"  {ip_addr3:>20}  {mac_addr3:>20}")


# ==============================================================
# BONUS — The better way: use a list + for loop
#
# CONCEPT: Instead of mac1, mac2, mac3 as separate variables,
#          put them in a LIST and loop through with for.
#          This scales to 100 ARP entries with no extra code.
# ==============================================================

print("\n--- BONUS: Same result with a list + for loop ---\n")

arp_entries = [mac1, mac2, mac3]    # put all entries in a list

# Build a results list by parsing each entry
parsed = []
for entry in arp_entries:
    fields = entry.split()
    ip     = fields[1]
    mac    = fields[3]
    parsed.append((ip, mac))        # store as a tuple (ip, mac)

# Print the table
print(f"  {'IP ADDR':>20}  {'MAC ADDRESS':>20}")
print(f"  {'-' * 20}  {'-' * 20}")
for ip, mac in parsed:             # unpack each (ip, mac) tuple
    print(f"  {ip:>20}  {mac:>20}")

# ------ What you just learned --------------------------------
# .split()          → breaks string into list on whitespace
# list[index]       → access item at position (starts at 0)
# f"{val:>20}"      → right-align in 20-char column
# f"{val:<20}"      → left-align in 20-char column
# list.append(item) → add item to end of list
# for a, b in list  → unpack tuple into two variables
# -------------------------------------------------------------


print("\n" + "=" * 60)
print("Lesson 2 complete! Move on to 03_functions.py")
print("=" * 60)
