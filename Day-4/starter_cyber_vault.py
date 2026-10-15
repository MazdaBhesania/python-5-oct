# ==============================================================================
# Course: Python Programming (Session 4)
# Lab Activity: CyberVault 2026 — Security Clearance & Lottery Terminal
# Student Name: [YOUR NAME HERE]
# Date: [TODAY'S DATE]
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
#   Additionally, verify authentication token health:
#   Suppose we track total_sessions and failed_logins:
#     total_sessions = 10
#     failed_logins = 2
#   The token is valid if:
#     total_sessions > 0 and (failed_logins / total_sessions < 0.4)
#   Combine this with access permissions using 'and'.
# ------------------------------------------------------------------------------
total_sessions = 10
failed_logins = 2

# TODO: Write the compound boolean expression to determine 'access_granted'
# YOUR CODE HERE:
access_granted = False  # Replace with your logical expression!


# ------------------------------------------------------------------------------
# STEP 4: Leap Year Bonus Hours (Liang 3.11 Case Study)
#
# Rule:
#   A year is a leap year if:
#     (badge_year % 4 == 0 and badge_year % 100 != 0) or (badge_year % 400 == 0)
#
# If it is a leap year, the badge receives 366 bonus access hours.
# Otherwise, it receives 365 bonus access hours.
# ------------------------------------------------------------------------------
# TODO: Calculate 'is_leap_year' (bool) and 'bonus_hours' (int)
# YOUR CODE HERE:
is_leap_year = False
bonus_hours = 365


# ------------------------------------------------------------------------------
# STEP 5: Conditional Expressions (Ternary Operator - Liang 3.13)
#
# 1. Set 'status_label':
#    If access_granted is True -> "ACCESS GRANTED"
#    Otherwise -> "ACCESS DENIED"
#
# 2. Set 'gate_lane':
#    If clearance_level >= 4 -> "Priority Quantum Lane"
#    Otherwise -> "Standard Security Lane"
#
# Syntax reminder: <value_if_true> if <condition> else <value_if_false>
# ------------------------------------------------------------------------------
# TODO: Use Python ternary operators to assign 'status_label' and 'gate_lane'
# YOUR CODE HERE:
status_label = ""
gate_lane = ""


# ------------------------------------------------------------------------------
# STEP 6: Math Module Calculations (Distance & Packets - Liang 4.2)
#
# 1. Calculate Euclidean distance from terminal (terminal_x, terminal_y) to
#    central server (0, 0):
#    distance = math.sqrt((terminal_x - 0)**2 + (terminal_y - 0)**2)
#
# 2. Calculate the number of transmission packets needed to transfer payload_bytes:
#    packets_count = math.ceil(payload_bytes / PACKET_SIZE)
# ------------------------------------------------------------------------------
# TODO: Compute 'distance' and 'packets_count' using the math module
# YOUR CODE HERE:
distance = 0.0
packets_count = 0


# ------------------------------------------------------------------------------
# STEP 7: Character Cipher Token Generation (Liang 4.3: ord and chr)
#
# Generate a 3-character security cipher key derived from 'badge_letter':
# - Character 1: badge_letter shifted by +1
# - Character 2: badge_letter shifted by +3
# - Character 3: badge_letter shifted by +5
# Combine them into a string: cipher_key = f"{char1}{char2}{char3}"
# ------------------------------------------------------------------------------
# TODO: Compute char1, char2, char3 using chr() and ord(), then form cipher_key
# YOUR CODE HERE:
cipher_key = "AAA"


# ------------------------------------------------------------------------------
# STEP 8: Two-Digit Lucky Vault Lottery Draw (Liang 3.12 Case Study)
#
# 1. Generate a random 2-digit vault number between 10 and 99 (inclusive).
#    (For predictable testing, you can temporarily fix vault_code = 48)
#    vault_code = random.randint(10, 99)
#
# 2. Extract digits of both vault_code and user_lottery_guess:
#    vault_d1 = vault_code // 10
#    vault_d2 = vault_code % 10
#    guess_d1 = user_lottery_guess // 10
#    guess_d2 = user_lottery_guess % 10
#
# 3. Determine award:
#    - Exact match (user_lottery_guess == vault_code):
#        Prize = GRAND_PRIZE ($10,000.00), Outcome = "Grand Jackpot! Exact Match!"
#    - Reverse match (guess_d1 == vault_d2 and guess_d2 == vault_d1):
#        Prize = SILVER_PRIZE ($3,000.00), Outcome = "Silver Tier! All Digits Matched!"
#    - One digit matches (guess_d1 in [vault_d1, vault_d2] or guess_d2 in [vault_d1, vault_d2]):
#        Prize = BRONZE_PRIZE ($1,000.00), Outcome = "Bronze Tier! One Digit Matched!"
#    - Else:
#        Prize = 0.0, Outcome = "No Match. Better luck next draw!"
# ------------------------------------------------------------------------------
vault_code = random.randint(10, 99)

# TODO: Extract digits, compare using logical operators, and set 'prize' and 'lottery_outcome'
# YOUR CODE HERE:
prize = 0.0
lottery_outcome = "No Match."


# ------------------------------------------------------------------------------
# STEP 9: System Protocol Mode (Python 3.10 match-case with 3.9 compatibility)
#
# System operational mode code: "SEC-NORMAL"
# Modes:
#   - "SEC-NORMAL"      -> "Standard surveillance and biometric checks active."
#   - "SEC-HIGH-ALERT"  -> "Armed perimeter defense; escort required."
#   - "SEC-MAINTENANCE" -> "Terminal offline for quantum key distribution."
#   - default / _       -> "Standard protocol fallback."
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
