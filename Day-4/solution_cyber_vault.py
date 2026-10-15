# ==============================================================================
# Course: Python Programming (Session 4)
# Lab Activity: CyberVault 2026 — Security Clearance & Lottery Terminal (SOLUTION)
# Instructor / Reference Solution
#
# Description:
#   An automated security clearance gate and lucky vault draw terminal.
#   Integrates core Session 4 concepts:
#   - Logical Operators (and, or, not) & Operator Precedence
#   - Short-Circuit Evaluation (Guarding against ZeroDivisionError)
#   - Case Study: Determining Leap Years (Liang 3.11)
#   - Case Study: 2-Digit Lottery Matcher (Liang 3.12)
#   - Conditional Expressions / Ternary Operator (Liang 3.13)
#   - Math Functions (math.sqrt, math.ceil, math.radians, round)
#   - Characters & ASCII Manipulation (ord(), chr())
# ==============================================================================

import math
import random
import sys

print("=" * 68)
print("     🔐 CYBERVAULT 2026: QUANTUM ACCESS & LOTTERY TERMINAL 🔐")
print("=" * 68)

# ------------------------------------------------------------------------------
# STEP 1: Constants
# ------------------------------------------------------------------------------
PACKET_SIZE = 64              # Maximum bytes per encrypted communication packet
CENTRAL_GRID_X = 0            # Central server X coordinate
CENTRAL_GRID_Y = 0            # Central server Y coordinate
GRAND_PRIZE = 10000.00        # Exact match
SILVER_PRIZE = 3000.00        # All digits match
BRONZE_PRIZE = 1000.00        # One digit matches


# ------------------------------------------------------------------------------
# STEP 2: Collect User & Terminal Inputs
# ------------------------------------------------------------------------------
visitor_name = input("Enter Operative Codename: ").strip()
clearance_level = int(input("Enter Clearance Level (1 to 5): "))
is_security_officer_input = input("Are you a certified security officer? (yes/no): ").strip().lower()
is_blacklisted_input = input("Is this badge flagged on the blacklist? (yes/no): ").strip().lower()

# Convert answers to booleans:
is_security_officer = (is_security_officer_input == "yes")
is_blacklisted = (is_blacklisted_input == "yes")

# Additional parameters for calculations:
badge_year = int(input("Enter Badge Issue Year (e.g. 2024, 2025): "))
terminal_x = float(input("Enter Terminal Grid X coordinate (e.g. 12.0): "))
terminal_y = float(input("Enter Terminal Grid Y coordinate (e.g. 16.0): "))
payload_bytes = int(input("Enter transmission payload size in bytes (e.g. 250): "))
badge_letter = input("Enter single badge initial letter (A-W): ").strip().upper()[0]
user_lottery_guess = int(input("Enter 2-digit Lucky Vault guess (10 to 99): "))


# ------------------------------------------------------------------------------
# STEP 3: Clearance Verification (Logical Operators & Short-Circuit)
#
# Rule:
#   A visitor is granted access IF:
#     (clearance_level >= 3 OR is_security_officer) AND NOT is_blacklisted
#
# Short-Circuit Guard:
#   Token health is valid if total_sessions > 0 and (failed_logins / total_sessions < 0.4)
# ------------------------------------------------------------------------------
total_sessions = 10
failed_logins = 2

# Short-circuit check guards against division by zero if total_sessions == 0:
token_health_ok = (total_sessions > 0) and ((failed_logins / total_sessions) < 0.4)

# Compound access evaluation:
access_granted = (
    (clearance_level >= 3 or is_security_officer)
    and (not is_blacklisted)
    and token_health_ok
)


# ------------------------------------------------------------------------------
# STEP 4: Leap Year Bonus Hours (Liang 3.11 Case Study)
#
# Rule:
#   A year is a leap year if:
#     (badge_year % 4 == 0 and badge_year % 100 != 0) or (badge_year % 400 == 0)
# ------------------------------------------------------------------------------
is_leap_year = (badge_year % 4 == 0 and badge_year % 100 != 0) or (badge_year % 400 == 0)
bonus_hours = 366 if is_leap_year else 365


# ------------------------------------------------------------------------------
# STEP 5: Conditional Expressions (Ternary Operator - Liang 3.13)
#
# Syntax: <value_if_true> if <condition> else <value_if_false>
# ------------------------------------------------------------------------------
status_label = "ACCESS GRANTED" if access_granted else "ACCESS DENIED"
gate_lane = "Priority Quantum Lane" if clearance_level >= 4 else "Standard Security Lane"


# ------------------------------------------------------------------------------
# STEP 6: Math Module Calculations (Distance & Packets - Liang 4.2)
#
# 1. Euclidean distance to central server (0, 0):
#    distance = math.sqrt((x - 0)^2 + (y - 0)^2)
#
# 2. Number of whole packets needed: math.ceil(payload_bytes / PACKET_SIZE)
# ------------------------------------------------------------------------------
distance = math.sqrt((terminal_x - CENTRAL_GRID_X) ** 2 + (terminal_y - CENTRAL_GRID_Y) ** 2)
packets_count = math.ceil(payload_bytes / PACKET_SIZE)


# ------------------------------------------------------------------------------
# STEP 7: Character Cipher Token Generation (Liang 4.3: ord and chr)
#
# Take the badge initial and generate a 3-character security cipher:
# +1, +3, +5 character shifts
# ------------------------------------------------------------------------------
base_ascii = ord(badge_letter)
char1 = chr(base_ascii + 1)
char2 = chr(base_ascii + 3)
char3 = chr(base_ascii + 5)
cipher_key = f"{char1}{char2}{char3}"


# ------------------------------------------------------------------------------
# STEP 8: Two-Digit Lucky Vault Lottery Draw (Liang 3.12 Case Study)
#
# 1. Generate 2-digit vault number (10 to 99):
# 2. Extract digits:
#    d1 = num // 10
#    d2 = num % 10
# 3. Apply Liang 3.12 prize rules:
#    - Exact match -> $10,000
#    - Reverse match (all digits match) -> $3,000
#    - One digit matches -> $1,000
#    - Else -> $0
# ------------------------------------------------------------------------------
vault_code = random.randint(10, 99)

vault_d1 = vault_code // 10
vault_d2 = vault_code % 10

guess_d1 = user_lottery_guess // 10
guess_d2 = user_lottery_guess % 10

if user_lottery_guess == vault_code:
    prize = GRAND_PRIZE
    lottery_outcome = "Grand Jackpot! Exact Match!"
elif (guess_d1 == vault_d2) and (guess_d2 == vault_d1):
    prize = SILVER_PRIZE
    lottery_outcome = "Silver Tier! All Digits Matched!"
elif (guess_d1 == vault_d1 or guess_d1 == vault_d2 or
      guess_d2 == vault_d1 or guess_d2 == vault_d2):
    prize = BRONZE_PRIZE
    lottery_outcome = "Bronze Tier! One Digit Matched!"
else:
    prize = 0.0
    lottery_outcome = "No Match. Better luck next draw!"


# ------------------------------------------------------------------------------
# STEP 9: System Protocol Mode (Python 3.10 match-case with 3.9 compatibility)
# ------------------------------------------------------------------------------
system_mode = "SEC-NORMAL"
mode_description = ""

if sys.version_info >= (3, 10):
    match_code = """
match system_mode:
    case "SEC-NORMAL":
        desc = "Standard surveillance and biometric checks active."
    case "SEC-HIGH-ALERT":
        desc = "Armed perimeter defense; escort required."
    case "SEC-MAINTENANCE":
        desc = "Terminal offline for quantum key distribution."
    case _:
        desc = "Standard protocol fallback."
"""
    local_vars = {"system_mode": system_mode}
    exec(match_code, {}, local_vars)
    mode_description = local_vars["desc"]
else:
    if system_mode == "SEC-NORMAL":
        mode_description = "Standard surveillance and biometric checks active."
    elif system_mode == "SEC-HIGH-ALERT":
        mode_description = "Armed perimeter defense; escort required."
    elif system_mode == "SEC-MAINTENANCE":
        mode_description = "Terminal offline for quantum key distribution."
    else:
        mode_description = "Standard protocol fallback."


# ------------------------------------------------------------------------------
# STEP 10: Print Final Security & Lottery Summary Pass
# ------------------------------------------------------------------------------
print("\n" + "=" * 68)
print("             CYBERVAULT 2026: TERMINAL CLEARANCE REPORT")
print("=" * 68)
print(f"Operative Codename:   {visitor_name}")
print(f"Clearance Level:      Level {clearance_level} ({gate_lane})")
print(f"Badge Security State: {'FLAGGED / BLACKLISTED' if is_blacklisted else 'CLEAN / VERIFIED'}")
print(f"Access Decision:      {status_label}")
print(f"Badge Year {badge_year}:     {'Leap Year Bonus (366 hrs)' if is_leap_year else 'Standard Year (365 hrs)'}")
print("-" * 68)
print(f"Terminal Grid:        ({terminal_x}, {terminal_y})")
print(f"Server Grid Distance: {distance:.2f} meters")
print(f"Payload Size:         {payload_bytes} bytes -> {packets_count} packet(s) required")
print(f"Badge Initial:        '{badge_letter}' -> Cipher Key Token: [{cipher_key}]")
print(f"System Mode Protocol: {mode_description}")
print("-" * 68)
print(f"Vault Lottery Draw:   Target [{vault_code}] | Your Guess [{user_lottery_guess}]")
print(f"Lottery Result:       {lottery_outcome}")
print(f"Cash Payout:          ${prize:,.2f}")
print("=" * 68)
