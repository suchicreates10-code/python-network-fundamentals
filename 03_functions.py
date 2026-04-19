"""
03_functions.py
---------------
NetworkKings | Python for Network Automation
Lecture 3 — Python Fundamentals | Silver + Gold Level exercises

Topic  : Functions — def, return, default arguments, error handling
Author : Sucharita Chakraborty

WHAT IS A FUNCTION?
  A function is a reusable block of code with a name.
  Instead of copying the same logic everywhere,
  you write it once and call it by name whenever you need it.

  def my_function(input):    ← define it once
      result = do_something(input)
      return result

  my_function("hello")       ← call it anywhere

Run it : python 03_functions.py
"""

print("=" * 60)
print("LESSON 3 — Functions for Network Data Processing")
print("=" * 60)


# ==============================================================
# SILVER 1 — safe_float() function
#
# PROBLEM: Network devices (SNMP, RESTCONF, CLI scraping) give
#          you values as strings — and some are invalid:
#            "74.5"  → should become 74.5  (float)
#            ""      → invalid, use default
#            "N/A"   → invalid, use default
#            None    → invalid, use default
#            "1e3"   → scientific notation = 1000.0 (float handles this!)
#
# CONCEPT: try / except — attempt something risky.
#          If it fails (raises an error), catch it and do
#          something safe instead. This prevents your script
#          from crashing on bad data.
# ==============================================================

print("\n--- SILVER 1: safe_float() function ---\n")

def safe_float(value, default=0.0):
    """
    Convert a string to float. Return default if conversion fails.

    Args:
        value   : the string to convert (can be anything)
        default : what to return if conversion fails (default: 0.0)

    Returns:
        float if conversion succeeds, otherwise default
    """
    try:
        return float(value)          # attempt the conversion
    except (ValueError, TypeError):  # catches bad value OR None
        return default               # return the safe fallback


# --- Test it with the values from the exercise ---

test_values = ["74.5", "", "N/A", None, "1e3"]

print(f"  {'Input':<12}  {'Result':<10}  {'Type'}")
print(f"  {'-'*12}  {'-'*10}  {'-'*8}")

for val in test_values:
    result = safe_float(val)
    print(f"  {str(val)!r:<12}  {result:<10}  {type(result).__name__}")

# ------ What you just learned --------------------------------
# def name(param, param=default):  → define a function
# return value                      → sends value back to caller
# try: ... except ErrorType:        → safely attempt risky code
# ValueError  → raised when float("N/A") fails (bad value)
# TypeError   → raised when float(None) fails (wrong type)
# default=0.0 → default argument (used if caller doesn't pass one)
# -------------------------------------------------------------


# ==============================================================
# SILVER 2 — Process SNMP MTU values using safe_float()
#
# PROBLEM: SNMP gives you a list of raw strings.
#          Some are invalid. You want only the valid MTU values
#          (and skip any that default to 0).
# ==============================================================

print("\n--- SILVER 2: Filter valid MTU values from SNMP data ---\n")

snmp_raw = ["1500", "9000", "N/A", "1500", ""]

valid_mtus = []

for raw_value in snmp_raw:
    mtu = safe_float(raw_value)     # convert safely
    if mtu != 0:                    # skip defaults (failed conversions)
        valid_mtus.append(int(mtu)) # store as int (MTU is always whole)

print(f"  SNMP raw data  : {snmp_raw}")
print(f"  Valid MTU list : {valid_mtus}")

# ------ What you just learned --------------------------------
# Reusing safe_float() here — write once, use everywhere
# int(mtu) converts float → int (1500.0 → 1500)
# Combining a function with a loop + condition = real automation
# -------------------------------------------------------------


# ==============================================================
# GOLD — build_device_record() function
#
# PROBLEM: Network monitoring systems (SNMP, RESTCONF, APIs)
#          return ALL values as raw strings in a dictionary.
#          You need to convert each field to its correct type
#          before you can use it in logic (e.g. if cpu > 80).
#
# Input dict (raw strings from device):
#   {
#     "hostname"       : "CORE-RTR-01",
#     "ip"             : "10.10.10.1",
#     "bgp_as"         : "65100",
#     "cpu"            : "87.3",
#     "mtu"            : "9000",
#     "interface_count": "24"
#   }
#
# Output dict (correct Python types):
#   {
#     "hostname"       : "CORE-RTR-01"  ← str  (already correct)
#     "ip"             : "10.10.10.1"   ← str  (IPs stay as strings)
#     "bgp_as"         : 65100          ← int
#     "cpu"            : 87.3           ← float
#     "mtu"            : 9000           ← int
#     "interface_count": 24             ← int
#     "is_high_cpu"    : True           ← bool (cpu > 80.0)
#   }
# ==============================================================

print("\n--- GOLD: build_device_record() function ---\n")

def build_device_record(raw_dict):
    """
    Convert a raw dictionary of string values (from SNMP / API)
    into a properly typed device record.

    Handles conversion failures gracefully — bad values become
    safe defaults instead of crashing the script.

    Args:
        raw_dict : dict with string values from network device

    Returns:
        dict with correct Python types + is_high_cpu flag
    """

    # Extract each field with a safe fallback if the key is missing
    hostname        = raw_dict.get("hostname", "UNKNOWN")
    ip              = raw_dict.get("ip",       "0.0.0.0")
    bgp_as          = safe_float(raw_dict.get("bgp_as", "0"), default=0)
    cpu             = safe_float(raw_dict.get("cpu",    "0"), default=0.0)
    mtu             = safe_float(raw_dict.get("mtu",    "0"), default=0)
    interface_count = safe_float(raw_dict.get("interface_count", "0"), default=0)

    # Build and return the clean, typed dictionary
    return {
        "hostname"        : str(hostname),
        "ip"              : str(ip),
        "bgp_as"          : int(bgp_as),
        "cpu"             : float(cpu),
        "mtu"             : int(mtu),
        "interface_count" : int(interface_count),
        "is_high_cpu"     : cpu > 80.0,   # bool: True if cpu over 80%
    }


# --- Test with a realistic raw device dict ---

raw_input = {
    "hostname"        : "CORE-RTR-01",
    "ip"              : "10.10.10.1",
    "bgp_as"          : "65100",
    "cpu"             : "87.3",
    "mtu"             : "9000",
    "interface_count" : "24",
}

print("  Input (raw strings from device):")
for key, val in raw_input.items():
    print(f"    {key:<20} = {val!r:<12}  ({type(val).__name__})")

record = build_device_record(raw_input)

print("\n  Output (after build_device_record):")
for key, val in record.items():
    print(f"    {key:<20} = {val!r:<12}  ({type(val).__name__})")


# --- Test with bad/missing data to prove it handles failures ---

print("\n--- Testing with bad/missing data ---\n")

bad_input = {
    "hostname"        : "BROKEN-SW-01",
    "ip"              : "10.10.10.2",
    "bgp_as"          : "N/A",      # invalid
    "cpu"             : "",          # empty
    "mtu"             : None,        # None
    # interface_count missing entirely
}

bad_record = build_device_record(bad_input)

print("  Output with bad input (no crash!):")
for key, val in bad_record.items():
    print(f"    {key:<20} = {val!r:<12}  ({type(val).__name__})")


# --- Real automation logic using the clean record ---

print("\n--- Using the record in real automation logic ---\n")

for device_raw in [raw_input, bad_input]:
    device = build_device_record(device_raw)

    if device["is_high_cpu"]:
        print(f"  ALERT: {device['hostname']} — CPU at {device['cpu']}% (threshold: 80%)")
    else:
        print(f"  OK   : {device['hostname']} — CPU at {device['cpu']}%")

# ------ What you just learned --------------------------------
# dict.get(key, default) → safely get value, return default if missing
# cpu > 80.0             → comparison returns True or False directly
# Combining safe_float() inside build_device_record() shows
# how functions CALL other functions — this is real code structure
# -------------------------------------------------------------


print("\n" + "=" * 60)
print("All 3 lessons complete!")
print("Next: push this folder to GitHub as your first learning repo.")
print("=" * 60)
