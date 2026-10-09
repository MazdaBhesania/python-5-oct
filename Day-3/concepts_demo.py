# ==============================================================================
# Course: Python Programming (Session 3)
# Topic: Chapter 4 — Selections (Conditionals) Reference Guide
# Note: Relational operators, 1-way if, 2-way if-else, multi-way if-elif-else,
#       and nested if statements are covered here.
#       *Logical operators (and, or, not) will be covered in the next session!*
# ==============================================================================

import random

print("=" * 65)
print("     DAY 3: SELECTION STATEMENTS MASTER REFERENCE SCRIPT")
print("=" * 65)

# ------------------------------------------------------------------------------
# 4.1 & 4.2: Boolean Data Type & Relational (Comparison) Operators
# ------------------------------------------------------------------------------
print("\n--- 4.1 & 4.2: Boolean Expressions & Relational Operators ---")
# Python booleans have exactly two values: True and False (capitalized!)
# Relational operators compare two values and produce a boolean:
#   ==  Equal to
#   !=  Not equal to
#   <   Less than
#   <=  Less than or equal to
#   >   Greater than
#   >=  Greater than or equal to

score = 85
passing_score = 70

print(f"score = {score}, passing_score = {passing_score}")
print("score > passing_score: ", score > passing_score)   # True
print("score == 100:          ", score == 100)           # False
print("score != 100:          ", score != 100)           # True
print("score <= 85:           ", score <= 85)            # True

# Common beginner trap:
# '='  is ASSIGNMENT (puts a value into a variable)
# '==' is EQUALITY COMPARISON (asks: are these two equal?)


# ------------------------------------------------------------------------------
# 4.3: Generating Random Numbers (random module)
# ------------------------------------------------------------------------------
print("\n--- 4.3: Generating Random Numbers (random.randint) ---")
# random.randint(a, b) returns a random integer N such that a <= N <= b (inclusive)
secret_die = random.randint(1, 6)
print(f"Rolled a 6-sided die: {secret_die}")


# ------------------------------------------------------------------------------
# 4.4: One-Way 'if' Statements
# ------------------------------------------------------------------------------
print("\n--- 4.4: One-Way 'if' Statements ---")
# Executes a block of code ONLY IF the condition is True.
# If False, Python simply skips the indented block and continues.

cart_total = 120.0
discount = 0.0

# Grant a $15 discount only if cart total exceeds $100
if cart_total > 100.0:
    discount = 15.0
    print(">> Congratulations! You unlocked a $15 loyalty discount!")

final_total = cart_total - discount
print(f"Final Cart Total: ${final_total:.2f}")


# ------------------------------------------------------------------------------
# 4.5: Two-Way 'if-else' Statements
# ------------------------------------------------------------------------------
print("\n--- 4.5: Two-Way 'if-else' Statements ---")
# Exactly one of the two blocks will execute:
# - 'if' block runs if condition is True
# - 'else' block runs if condition is False

test_score = 68

if test_score >= 70:
    print(f"Score {test_score}: Passed! Great job.")
else:
    print(f"Score {test_score}: Needs improvement. Please retake the quiz.")


# Checking Even or Odd using the Modulo operator (%):
number = 17
if number % 2 == 0:
    print(f"{number} is an EVEN number.")
else:
    print(f"{number} is an ODD number.")


# ------------------------------------------------------------------------------
# 4.6: Multi-Way 'if-elif-else' Statements
# ------------------------------------------------------------------------------
print("\n--- 4.6: Multi-Way 'if-elif-else' Statements ---")
# Used when choosing among multiple mutually exclusive options.
# Python checks conditions from top to bottom.
# As soon as one condition is True, its block runs, and the rest are SKIPPED!

exam_score = 84

if exam_score >= 90:
    letter_grade = "A"
elif exam_score >= 80:
    letter_grade = "B"      # Reached only if exam_score < 90
elif exam_score >= 70:
    letter_grade = "C"      # Reached only if exam_score < 80
elif exam_score >= 60:
    letter_grade = "D"      # Reached only if exam_score < 70
else:
    letter_grade = "F"      # Reached only if exam_score < 60

print(f"Exam score: {exam_score} -> Letter Grade: {letter_grade}")


# ------------------------------------------------------------------------------
# 4.7: Nested 'if' Statements (Decisions inside Decisions)
# ------------------------------------------------------------------------------
print("\n--- 4.7: Nested 'if' Statements ---")
# When logical operators ('and', 'or') have not been introduced,
# or when decisions are hierarchical, nested 'if' statements are used!

age = 16
has_parental_consent = True

if age >= 18:
    print("Eligibility: Fully eligible to register independently.")
else:
    # Nested check for minors under 18:
    if has_parental_consent == True:
        print("Eligibility: Minor registered with signed parental consent.")
    else:
        print("Eligibility: Ineligible. Minor requires parental consent.")


# ------------------------------------------------------------------------------
# 4.8: Common Selection Pitfalls to Avoid
# ------------------------------------------------------------------------------
print("\n--- 4.8: Common Selection Pitfalls ---")

# 1. FORGETTING THE COLON (:) AT THE END OF if/elif/else
#    if score > 50   <-- SyntaxError! Must be: if score > 50:

# 2. USING '=' INSTEAD OF '=='
#    if score = 100: <-- SyntaxError! Assignment cannot be in condition.

# 3. INDENTATION ERRORS
#    Python uses indentation (4 spaces) to define code blocks.
#    All statements inside a branch must be aligned.

# 4. WRONG ORDER IN if-elif-else CASCADES
#    Incorrect order:
#        if score >= 60:
#            grade = "D"
#        elif score >= 90:  # DEAD CODE! Score 95 will match >= 60 first and get "D"!
#            grade = "A"

# 5. REDUNDANT CONDITIONS
#    In 'if score >= 90: ... elif score >= 80: ...',
#    there is NO need to write 'score < 90' in the elif, because the elif
#    only executes if the first condition was False!

print("Demo complete! Ready for hands-on practice.")
print("=" * 65)
