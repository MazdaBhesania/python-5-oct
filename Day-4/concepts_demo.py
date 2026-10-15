# ==============================================================================
# Course: Python Programming (Session 4)
# Topic: Logical Operators, Advanced Selections, Math Functions & Characters
# Textbook Sections:
#   - 3.10: Logical Operators (and, or, not, Short-Circuit Evaluation)
#   - 3.11: Case Study: Determining Leap Years
#   - 3.12: Case Study: Lottery Number Matcher
#   - 3.13: Conditional Expressions (Ternary Operator)
#   - 3.14: Python 3.10 match-case Statements
#   - 4.1 – 4.2: Built-in Math Functions (abs, max, min, pow, round) & math module
#   - 4.3: Strings and Characters (ASCII / Unicode, ord(), chr())
# ==============================================================================

import math
import random

print("=" * 70)
print("     DAY 4: ADVANCED SELECTIONS, MATH FUNCTIONS & CHARACTERS")
print("=" * 70)

# ------------------------------------------------------------------------------
# 3.10: Logical Operators (and, or, not) & Short-Circuit Evaluation
# ------------------------------------------------------------------------------
print("\n--- 3.10: Logical Operators (and, or, not) ---")
# 'and': True only if BOTH operands are True
# 'or' : True if AT LEAST ONE operand is True
# 'not': Inverts the boolean value (True becomes False, False becomes True)

age = 22
has_id = True
gpa = 3.8

print(f"age = {age}, has_id = {has_id}, gpa = {gpa}")
print("Can enter club (age >= 21 and has_id):     ", age >= 21 and has_id)
print("Qualifies for grant (gpa > 3.9 or age < 25):", gpa > 3.9 or age < 25)
print("not has_id:                                 ", not has_id)

# Pythonic Range Chaining:
# In Python, '18 <= age <= 65' is equivalent to '(18 <= age) and (age <= 65)'
print("Working age (18 <= age <= 65):             ", 18 <= age <= 65)

# SHORT-CIRCUIT EVALUATION:
# Python stops evaluating as soon as the result is determined!
# For 'and': if the 1st operand is False, the 2nd is NEVER evaluated.
# For 'or' : if the 1st operand is True,  the 2nd is NEVER evaluated.
# This prevents runtime errors like ZeroDivisionError:
count = 0
total = 100
# count != 0 is False, so total / count is NEVER evaluated:
if count != 0 and (total / count > 10):
    print("Average is high")
else:
    print("Safely avoided division by zero via short-circuit evaluation!")


# ------------------------------------------------------------------------------
# 3.11: Case Study: Determining Leap Years
# ------------------------------------------------------------------------------
print("\n--- 3.11: Case Study — Leap Year Determination ---")
# A year is a leap year if:
# 1. It is divisible by 4 AND NOT divisible by 100, OR
# 2. It is divisible by 400.
year = 2024
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(f"Is {year} a leap year? {is_leap}")

year_century = 1900  # Divisible by 4 and 100, but not 400 -> False!
is_century_leap = (year_century % 4 == 0 and year_century % 100 != 0) or (year_century % 400 == 0)
print(f"Is {year_century} a leap year? {is_century_leap}")


# ------------------------------------------------------------------------------
# 3.12: Case Study: Lottery Number Matcher
# ------------------------------------------------------------------------------
print("\n--- 3.12: Case Study — Lottery Number Matcher ---")
# Two-digit lottery logic:
# - Exact match (both digits and order): $10,000
# - All digits match (reverse order): $3,000
# - One digit matches: $1,000
lottery = 48
user_guess = 84

# Extract digits using floor division and modulo:
lottery_d1 = lottery // 10
lottery_d2 = lottery % 10
guess_d1 = user_guess // 10
guess_d2 = user_guess % 10

print(f"Lottery: {lottery} (digits: {lottery_d1}, {lottery_d2}) | Guess: {user_guess} (digits: {guess_d1}, {guess_d2})")

if user_guess == lottery:
    print("Prize: Exact Match! You win $10,000!")
elif (guess_d1 == lottery_d2) and (guess_d2 == lottery_d1):
    print("Prize: All digits match! You win $3,000!")
elif (guess_d1 == lottery_d1 or guess_d1 == lottery_d2 or
      guess_d2 == lottery_d1 or guess_d2 == lottery_d2):
    print("Prize: One digit matched! You win $1,000!")
else:
    print("Prize: No match. Better luck next time!")


# ------------------------------------------------------------------------------
# 3.13: Conditional Expressions (Ternary Operator)
# ------------------------------------------------------------------------------
print("\n--- 3.13: Conditional Expressions (Ternary Operator) ---")
# Syntax: expression1 if boolean_condition else expression2
score = 82
status = "Passing" if score >= 70 else "Failing"
print(f"Score {score} -> Status: {status}")

# Finding maximum in a single clean line:
num1, num2 = 45, 78
larger = num1 if num1 > num2 else num2
print(f"Larger of {num1} and {num2} is: {larger}")


# ------------------------------------------------------------------------------
# 3.14: Python 3.10 match-case Statements
# ------------------------------------------------------------------------------
print("\n--- 3.14: Python 3.10 match-case Statements ---")
# Structural pattern matching was introduced in Python 3.10.
# If your machine runs Python 3.9 or earlier, Python will show a SyntaxError.
# Here is the modern Python 3.10+ syntax:
#
# match command:
#     case "start":
#         action = "System starting up..."
#     case "stop":
#         action = "System shutting down..."
#     case "status":
#         action = "System operational: 100% health."
#     case _:
#         action = "Unknown command. Type 'help' for options."

command = "status"

import sys
if sys.version_info >= (3, 10):
    # Dynamically executed on Python 3.10+
    match_code = """
match command:
    case "start":
        action = "System starting up..."
    case "stop":
        action = "System shutting down..."
    case "status":
        action = "System operational: 100% health."
    case _:
        action = "Unknown command. Type 'help' for options."
"""
    local_vars = {"command": command}
    exec(match_code, {}, local_vars)
    action = local_vars["action"]
    print(f"[Python 3.10+ match-case] Command '{command}' -> Action: {action}")
else:
    # Python 3.9 (or earlier) fallback using if-elif-else:
    if command == "start":
        action = "System starting up..."
    elif command == "stop":
        action = "System shutting down..."
    elif command == "status":
        action = "System operational: 100% health."
    else:
        action = "Unknown command. Type 'help' for options."
    print(f"[Python {sys.version_info.major}.{sys.version_info.minor} fallback] Command '{command}' -> Action: {action}")
    print("  Note: Python 3.10+ supports native 'match command:' and 'case _:' syntax!")



# ------------------------------------------------------------------------------
# 4.2: Built-in Numeric Functions & math Module
# ------------------------------------------------------------------------------
print("\n--- 4.2: Built-in Numeric Functions & math Module ---")
# 1. Built-in functions:
print("abs(-15.6):     ", abs(-15.6))       # 15.6
print("max(4, 9, 2, 7): ", max(4, 9, 2, 7))  # 9
print("min(4, 9, 2, 7): ", min(4, 9, 2, 7))  # 2
print("pow(2, 5):       ", pow(2, 5))        # 32 (same as 2 ** 5)
print("round(3.14159, 2):", round(3.14159, 2)) # 3.14

# 2. math module functions:
print("math.sqrt(49):   ", math.sqrt(49))    # 7.0
print("math.ceil(4.1):  ", math.ceil(4.1))   # 5 (rounds UP to nearest integer)
print("math.floor(4.9): ", math.floor(4.9))  # 4 (rounds DOWN to nearest integer)
print("math.pi:         ", math.pi)          # 3.141592653589793
print("math.e:          ", math.e)           # 2.718281828459045

# Trigonometry (expects angles in radians!):
angle_degrees = 30
angle_radians = math.radians(angle_degrees)
print(f"sin(30 deg):     {math.sin(angle_radians):.4f}")  # 0.5000


# ------------------------------------------------------------------------------
# 4.3: Strings and Characters (ord() and chr())
# ------------------------------------------------------------------------------
print("\n--- 4.3: Strings & Characters (ASCII / Unicode Codes) ---")
# ord(ch): returns the numeric ASCII/Unicode code for a single character
# chr(code): returns the character corresponding to an integer code

print("ord('A'):        ", ord('A'))        # 65
print("ord('a'):        ", ord('a'))        # 97 (lowercase is +32 away from uppercase)
print("ord('0'):        ", ord('0'))        # 48
print("chr(65):         ", chr(65))         # 'A'
print("chr(97):         ", chr(97))         # 'a'

# Mini Cipher demo: Shift character 'A' by 3 positions:
shifted_char = chr(ord('A') + 3)
print(f"'A' shifted by +3 -> '{shifted_char}' (ASCII {ord(shifted_char)})")

print("\n" + "=" * 70)
print("     DEMO COMPLETE! READY FOR DAY 4 HANDS-ON ACTIVITIES!")
print("=" * 70)
