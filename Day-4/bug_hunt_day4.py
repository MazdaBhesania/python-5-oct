# ==============================================================================
# Day 4: In-Class Activity — Advanced Selections & Math Bug Hunt
# Topics:
#   - Logical Operators (and, or, not) & Operator Precedence
#   - Short-Circuit Evaluation & ZeroDivisionError Prevention
#   - Conditional Expressions (Ternary Operator)
#   - Math Module & Trigonometry (Degrees vs Radians)
#   - Character Codes & ASCII Shifting (ord(), chr())
#
# Instructions:
# 1. Read through each challenge below.
# 2. Uncomment the buggy line(s) under "UNCOMMENT TO TEST".
# 3. Run the file: python3 Day-4/bug_hunt_day4.py
# 4. Observe the error message or faulty output.
# 5. Fix the bug so that all 5 challenges produce the expected output!
# ==============================================================================

import math

print("=" * 65)
print("             DAY 4 BUG HUNT: 5 CODING CHALLENGES")
print("=" * 65)


# ------------------------------------------------------------------------------
# CHALLENGE 1: Operator Precedence Trap ('and' binds tighter than 'or')
# Goal: Allow entry to a secure facility if the person is an (admin OR employee)
#       AND they possess a valid keycard.
# Problem: In Python, 'and' has higher precedence than 'or'. Without parentheses,
#          'is_admin or is_employee and has_keycard' evaluates as:
#          'is_admin or (is_employee and has_keycard)'.
#          This mistakenly grants access to ANY admin even if they have NO keycard!
# Fix: Wrap the 'or' condition in parentheses: (is_admin or is_employee) and has_keycard
# ------------------------------------------------------------------------------
print("\n[Challenge 1: Logical Operator Precedence]")
is_admin = True
is_employee = False
has_keycard = False  # Should NOT be allowed entry without a keycard!

# BUGGY VERSION (Uncomment to test):
# access_allowed = is_admin or is_employee and has_keycard
# print(f"Access allowed without keycard? {access_allowed} (BUG: should be False!)")

# FIXED VERSION:
access_allowed = (is_admin or is_employee) and has_keycard
print(f"Access allowed without keycard: {access_allowed} (Correct: False)")


# ------------------------------------------------------------------------------
# CHALLENGE 2: Short-Circuit Order & ZeroDivisionError
# Goal: Compute average packet size and check if it exceeds 50 KB.
# Problem: When 'packet_count' is 0, placing the division first causes Python
#          to crash with ZeroDivisionError before it ever reaches 'packet_count > 0'.
# Fix: Take advantage of SHORT-CIRCUIT evaluation! Place the guard check
#      'packet_count > 0' FIRST so Python stops immediately if count is 0.
# ------------------------------------------------------------------------------
print("\n[Challenge 2: Short-Circuit Evaluation]")
total_bytes = 1000
packet_count = 0

# BUGGY VERSION (Uncomment to test):
# if (total_bytes / packet_count > 50) and (packet_count > 0):
#     print("High traffic detected.")
# else:
#     print("No packets or normal traffic.")

# FIXED VERSION:
if packet_count > 0 and (total_bytes / packet_count > 50):
    print("High traffic detected.")
else:
    print("Safely handled 0 packets without crashing! (Short-circuit success)")


# ------------------------------------------------------------------------------
# CHALLENGE 3: Conditional Expression (Ternary Operator) Syntax
# Goal: Assign "High Priority" if score is >= 90, otherwise "Standard Priority".
# Problem: Programmers coming from other languages often write:
#          'status = if score >= 90 "High" else "Standard"'
#          Python's ternary syntax requires:
#          <value_if_true> if <condition> else <value_if_false>
# Fix: Write: "High Priority" if score >= 90 else "Standard Priority"
# ------------------------------------------------------------------------------
print("\n[Challenge 3: Ternary Operator Syntax]")
server_load = 94

# BUGGY VERSION (Uncomment to test):
# priority = if server_load >= 90 "High Priority" else "Standard Priority"

# FIXED VERSION:
priority = "High Priority" if server_load >= 90 else "Standard Priority"
print(f"Server load {server_load}% -> Priority: {priority}")


# ------------------------------------------------------------------------------
# CHALLENGE 4: Math Trigonometry (Degrees vs Radians)
# Goal: Compute the vertical height of a 10-meter solar panel tilted at 30 degrees.
#       Formula: height = length * sin(angle)
#       Expected result: 10 * sin(30 deg) = 10 * 0.5 = 5.0 meters.
# Problem: Python's math.sin() expects radians, not degrees!
#          math.sin(30) treats 30 as radians, resulting in -9.88 meters (negative height!).
# Fix: Convert degrees to radians first using math.radians(angle_degrees).
# ------------------------------------------------------------------------------
print("\n[Challenge 4: Math Module Radians vs Degrees]")
panel_length = 10.0
tilt_degrees = 30

# BUGGY VERSION (Uncomment to test):
# buggy_height = panel_length * math.sin(tilt_degrees)
# print(f"Buggy height: {buggy_height:.2f} m (Negative number!)")

# FIXED VERSION:
tilt_radians = math.radians(tilt_degrees)
correct_height = panel_length * math.sin(tilt_radians)
print(f"Correct height at {tilt_degrees} degrees: {correct_height:.2f} meters (Expected: 5.00 m)")


# ------------------------------------------------------------------------------
# CHALLENGE 5: Character Code Manipulation (ord() and chr())
# Goal: Shift the character 'A' forward by 4 positions in the alphabet to get 'E'.
# Problem: In Python, you cannot directly add an integer to a string:
#          'A' + 4 raises 'TypeError: can only concatenate str (not "int") to str'.
# Fix: Convert character to ASCII code using ord('A'), add 4, then convert
#      back to character using chr().
# ------------------------------------------------------------------------------
print("\n[Challenge 5: Character Arithmetic with ord() and chr()]")
base_letter = "A"
shift_amount = 4

# BUGGY VERSION (Uncomment to test):
# shifted_letter = base_letter + shift_amount

# FIXED VERSION:
shifted_letter = chr(ord(base_letter) + shift_amount)
print(f"Letter '{base_letter}' (ASCII {ord(base_letter)}) shifted by +{shift_amount} -> '{shifted_letter}' (ASCII {ord(shifted_letter)})")

print("\n" + "=" * 65)
print("             ALL BUG HUNT CHALLENGES RESOLVED!")
print("=" * 65)
