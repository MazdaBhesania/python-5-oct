# ==============================================================================
# Day 4: Quick Concept Drills — Logical Operators, Math & Characters
# Note: Practice these 3 short exercises during lecture or as a warm-up!
# Topics Covered:
#   - Drill 1: Leap Year Determination (Compound Boolean Logic: and / or)
#   - Drill 2: Ternary Operator & Range Chaining (Inline Conditional Decisions)
#   - Drill 3: Character Code Cipher & Math Checksum (ord(), chr(), math.sqrt())
# ==============================================================================

import math

print("=" * 65)
print("             DAY 4: 3 QUICK PRACTICE DRILLS")
print("=" * 65)


# ------------------------------------------------------------------------------
# DRILL 1: Leap Year Checker (Liang Section 3.11)
# Rule: A year is a leap year if:
#   1. It is divisible by 4 AND NOT divisible by 100, OR
#   2. It is divisible by 400.
# ------------------------------------------------------------------------------
print("\n--- Drill 1: Leap Year Determination ---")
year = int(input("Enter a year to check (e.g., 2024, 1900, 2000): "))

# Compound boolean expression:
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if is_leap:
    print(f"Result: Year {year} IS a Leap Year (366 days).")
else:
    print(f"Result: Year {year} is NOT a Leap Year (365 days).")


# ------------------------------------------------------------------------------
# DRILL 2: Range Chaining & Ternary Operator (Liang Section 3.13)
# Goal:
#   1. Check if user is working age using Python range chaining (18 <= age <= 65).
#   2. Use a ternary conditional expression to assign ticket price:
#      - If age is between 18 and 65 (inclusive) and NOT a student -> $30.00
#      - Otherwise (youth, senior, or student) -> $15.00
# ------------------------------------------------------------------------------
print("\n--- Drill 2: Range Chaining & Ternary Operator ---")
age = int(input("Enter your age: "))
is_student = input("Are you a full-time student? (yes/no): ").strip().lower() == "yes"

# Range chaining check:
is_working_adult = 18 <= age <= 65

# Ternary conditional expression:
ticket_price = 30.00 if (is_working_adult and not is_student) else 15.00

print(f"Working adult status: {is_working_adult}")
print(f"Assigned Ticket Price: ${ticket_price:.2f}")


# ------------------------------------------------------------------------------
# DRILL 3: Character Cipher & Math Checksum (Liang Sections 4.2 & 4.3)
# Goal:
#   1. Read an uppercase letter (e.g. 'A').
#   2. Shift the letter by +3 using ord() and chr() (Caesar cipher).
#   3. Compute a security checksum: math.sqrt(ord(letter) * 10).
# ------------------------------------------------------------------------------
print("\n--- Drill 3: Character Cipher & Math Checksum ---")
letter_input = input("Enter a single uppercase letter (A-W): ").strip().upper()

if len(letter_input) == 1 and "A" <= letter_input <= "Z":
    ascii_val = ord(letter_input)
    shifted_char = chr(ascii_val + 3)
    checksum = math.sqrt(ascii_val * 10)
    
    print(f"Original Letter:    '{letter_input}' (ASCII: {ascii_val})")
    print(f"Ciphered Letter (+3): '{shifted_char}' (ASCII: {ord(shifted_char)})")
    print(f"Math Checksum:       {checksum:.2f}")
else:
    print("Invalid input! Please enter exactly one uppercase letter.")

print("\n" + "=" * 65)
print("             DRILLS COMPLETE!")
print("=" * 65)
