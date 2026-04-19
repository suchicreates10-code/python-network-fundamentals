"""
01_variables_and_types.py
--------------------------
| Python for Network Automation
Lecture 3 — Python Fundamentals | Exercises

Topic  : Variables, Data Types, type(), dynamic typing, type conversion

Run it : python 01_variables_and_types.py
"""

print("=" * 60)
print("LESSON 1 — Variables and Data Types in Network Automation")
print("=" * 60)


# ==============================================================
# Create variables for a network device
#
# CONCEPT: Python has 4 basic data types you use constantly:
#   str   → text         e.g. "CORE-SW-01"
#   int   → whole number e.g. 24
#   float → decimal      e.g. 87.5
#   bool  → True / False e.g. True
#
# type() tells you what type a variable is.
# ==============================================================

print("\n--- 1: Network device variables ---\n")

hostname        = "CORE-SW-01"       # str  — text in quotes
mgmt_ip         = "10.10.10.1"       # str  — IPs are strings, not numbers
vlan_count      = 48                 # int  — whole number
cpu_util        = 34.7               # float — has a decimal point
is_backup_router = False             # bool — only True or False (capital T/F)

# Print each variable AND its type
print(f"  hostname         = {hostname!r:<20}  type: {type(hostname).__name__}")
print(f"  mgmt_ip          = {mgmt_ip!r:<20}  type: {type(mgmt_ip).__name__}")
print(f"  vlan_count       = {vlan_count!r:<20}  type: {type(vlan_count).__name__}")
print(f"  cpu_util         = {cpu_util!r:<20}  type: {type(cpu_util).__name__}")
print(f"  is_backup_router = {is_backup_router!r:<20}  type: {type(is_backup_router).__name__}")

# ------ What you just learned --------------------------------
# !r  inside f-string adds quotes around strings (repr format)
# :<20 pads the value to 20 characters wide (left aligned)
# type(x).__name__ gives the type name as a plain word
# -------------------------------------------------------------


# ==============================================================
# 2 — BGP AS number conversion
#
# CONCEPT: Data from routers often comes as a STRING even if
#          it looks like a number. You must convert it with int()
#          before you can do math on it.
#
#   str  → "65100"   (can't add to this)
#   int  → 65100     (can add to this)
# ==============================================================

print("\n--- 2: BGP AS number conversion ---\n")

bgp_as_raw = "65100"                 # comes as string from CLI output

print(f"  bgp_as_raw is type: {type(bgp_as_raw).__name__!r} — value: {bgp_as_raw}")

bgp_as_int  = int(bgp_as_raw)       # convert string → integer
next_as      = bgp_as_int + 1       # now we can do math on it

print(f"  After int():  type: {type(bgp_as_int).__name__!r} — value: {bgp_as_int}")
print(f"  Next AS number: {next_as}")
print(f"  Formatted string: 'Next AS number: {next_as}'")

# ------ What you just learned --------------------------------
# int("65100")  → converts a string to an integer
# str(65101)    → converts an integer back to a string
# You CANNOT do math on a string — "65100" + 1 gives an error
# -------------------------------------------------------------


# ==============================================================
#  3 — Dynamic typing
#
# CONCEPT: In Python, a variable can change its type at any time.
#          This is called "dynamic typing". JavaScript and Python
#          do this; Java and C do NOT.
# ==============================================================

print("\n--- 3: Dynamic typing demonstration ---\n")

status = 1                           # starts as int
print(f"  status = {status!r}   type: {type(status).__name__}")

status = "up"                        # reassigned to str — perfectly valid
print(f"  status = {status!r}    type: {type(status).__name__}")

# ------ What you just learned --------------------------------
# Python doesn't force you to declare a type upfront
# The variable takes whatever type you assign to it
# This is flexible but can cause bugs — always be aware of types
# -------------------------------------------------------------


# ==============================================================
# 4 — MAC address format conversion
#
# CONCEPT: .replace() swaps one character for another inside a string.
#          Network gear uses different MAC formats:
#            Cisco IOS:   XXXX.XXXX.XXXX
#            Linux/Wireshark: XX:XX:XX:XX:XX:XX
#            Windows:     XX-XX-XX-XX-XX-XX
#
# Task: Convert AAAA:BBBB:CCCC → AAAA.BBBB.CCCC
# ==============================================================

print("\n--- 4: MAC address format conversion ---\n")

mac = "AAAA:BBBB:CCCC"
print(f"  Original  : {mac}")

# .replace(old_char, new_char) — replaces ALL occurrences
mac_cisco = mac.replace(":", ".")
print(f"  Cisco fmt : {mac_cisco}")

# Bonus: also show how to go to Linux format (XX:XX:XX:XX:XX:XX)
# First remove the colons, then insert colons every 2 characters
mac_no_sep   = mac.replace(":", "")              # "AAAABBBBCCCC"
mac_linux    = ":".join(                         # joins with ":"
    mac_no_sep[i:i+2]                            # grab 2 chars at a time
    for i in range(0, len(mac_no_sep), 2)        # step by 2
)
print(f"  Linux fmt : {mac_linux}")

# ------ What you just learned --------------------------------
# .replace(old, new)     → replaces characters in a string
# "sep".join(list)       → joins list items with a separator
# range(0, 12, 2)        → 0, 2, 4, 6, 8, 10 (step of 2)
# string[i:i+2]          → slice: grab 2 chars starting at i
# -------------------------------------------------------------


print("\n" + "=" * 60)
print("Lesson 1 complete! Move on to 02_string_parsing.py")
print("=" * 60)
