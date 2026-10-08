# ==============================================================================
# Course: Python Programming (Session 2)
# Topic: Elementary Programming Reference Guide
# ==============================================================================

print("=" * 60)
print("     DAY 2: ELEMENTARY PROGRAMMING MASTER REFERENCE SCRIPT")
print("=" * 60)

# ------------------------------------------------------------------------------
# 2.1 & 2.2: Writing a Simple Program
# ------------------------------------------------------------------------------
print("\n--- 2.1 & 2.2: Simple Program (Circle Area Calculation) ---")
# Assigning values to variables and evaluating expressions
radius = 5.0
area = radius * radius * 3.14159
print("Radius:", radius)
print("Area of Circle:", area)


# ------------------------------------------------------------------------------
# 2.3: Reading Input from the Console & Type Conversion
# ------------------------------------------------------------------------------
print("\n--- 2.3: Reading Console Input ---")
# input() ALWAYS returns a string (str). We must convert (cast) it to numeric types.
# Simulated input examples (in real scripts, use: user_age = int(input("Age: ")))
sample_str = "25"
sample_price = "19.99"

age = int(sample_str)           # Converted to integer
price = float(sample_price)     # Converted to floating point

print("Original string:", sample_str, "| Type:", type(sample_str))
print("Converted int:  ", age,        "| Type:", type(age))
print("Converted float:", price,      "| Type:", type(price))


# ------------------------------------------------------------------------------
# 2.4: Identifiers (Naming Rules in Python)
# ------------------------------------------------------------------------------
print("\n--- 2.4: Identifiers (Variable Naming Rules) ---")
# VALID:
student_score = 95       # Letters, numbers, underscores (snake_case)
item_1 = "Book"
_internal_id = 1001

# INVALID (would cause SyntaxError if uncommented):
# 1st_score = 90         # Cannot start with a digit!
# student-score = 90     # Cannot contain hyphens (interpreted as minus)!
# student score = 90     # Cannot contain spaces!
# class = "Python"       # Cannot use reserved Python keywords!

print("Valid identifier conventions: snake_case (e.g., student_score, total_count)")


# ------------------------------------------------------------------------------
# 2.5: Variables, Assignment Statements, and Expressions
# ------------------------------------------------------------------------------
print("\n--- 2.5: Variables & Expressions ---")
count = 1                # Assignment: variable on left, value/expression on right
count = count + 1        # Right side is evaluated first, then stored in count
print("Updated count:", count)


# ------------------------------------------------------------------------------
# 2.6: Simultaneous Assignments & The Variable Swap
# ------------------------------------------------------------------------------
print("\n--- 2.6: Simultaneous Assignment & Swapping ---")
# Assign multiple variables at once:
x, y = 10, 20
print(f"Before swap -> x: {x}, y: {y}")

# Pythonic swap without needing a third 'temp' variable:
x, y = y, x
print(f"After swap  -> x: {x}, y: {y}")

# Multiple inputs simulation:
width, height = 4.5, 8.0
rect_area = width * height
print(f"Rectangle ({width} x {height}) area: {rect_area}")


# ------------------------------------------------------------------------------
# 2.7: Named Constants
# ------------------------------------------------------------------------------
print("\n--- 2.7: Named Constants ---")
# Constants use ALL_CAPS by convention to signal they should not be changed:
PI = 3.141592653589793
SALES_TAX_RATE = 0.0825
SECONDS_PER_MINUTE = 60

print("Named Constants:", PI, SALES_TAX_RATE, SECONDS_PER_MINUTE)


# ------------------------------------------------------------------------------
# 2.8: Numeric Data Types and Operators (+, -, *, /, //, %, **)
# ------------------------------------------------------------------------------
print("\n--- 2.8: Numeric Data Types & Operators ---")
a = 17
b = 4

print(f"Numbers: a = {a}, b = {b}")
print(f"Addition (a + b):            {a + b}")
print(f"Subtraction (a - b):         {a - b}")
print(f"Multiplication (a * b):      {a * b}")
print(f"Float Division (a / b):      {a / b}       (Always produces a float)")
print(f"Integer/Floor Div (a // b):  {a // b}         (Drops fractional part)")
print(f"Modulo/Remainder (a % b):    {a % b}         (17 divided by 4 leaves 1)")
print(f"Exponentiation (a ** 2):     {a ** 2}       (17 squared)")


# ------------------------------------------------------------------------------
# 2.9: Case Study Preview — Minimum Change Breakdown
# ------------------------------------------------------------------------------
print("\n--- 2.9: Case Study Breakdown Preview ---")
# Given 93 cents, find quarters and remaining cents:
total_cents = 93
quarters = total_cents // 25       # 93 // 25 = 3
remaining_cents = total_cents % 25 # 93 % 25 = 18
print(f"From {total_cents} cents:")
print(f"  Quarters: {quarters} (worth {quarters * 25} cents)")
print(f"  Remaining cents to break down: {remaining_cents} cents")


# ------------------------------------------------------------------------------
# 2.10: Evaluating Expressions and Operator Precedence
# ------------------------------------------------------------------------------
print("\n--- 2.10: Operator Precedence (PEMDAS) ---")
# 1. Parentheses ()
# 2. Exponentiation **
# 3. Multiplication, Division, Modulo (*, /, //, %) - Left to right
# 4. Addition, Subtraction (+, -) - Left to right

score1, score2, score3 = 80, 90, 85
# WRONG without parentheses: score1 + score2 + (score3 / 3) = 80 + 90 + 28.33 = 198.33
wrong_avg = score1 + score2 + score3 / 3
# CORRECT with parentheses:
correct_avg = (score1 + score2 + score3) / 3

print("Incorrect average (no parens):", wrong_avg)
print("Correct average (with parens):", correct_avg)


# ------------------------------------------------------------------------------
# 2.11: Augmented Assignment Operators (+=, -=, *=, /=, //=, %=)
# ------------------------------------------------------------------------------
print("\n--- 2.11: Augmented Assignment Operators ---")
score = 100
print("Initial score:", score)

score += 15     # Same as score = score + 15
print("After score += 15: ", score)

score -= 5      # Same as score = score - 5
print("After score -= 5:  ", score)

score *= 2      # Same as score = score * 2
print("After score *= 2:  ", score)

score //= 4     # Same as score = score // 4
print("After score //= 4: ", score)

score %= 7      # Same as score = score % 7
print("After score %= 7:  ", score)


# ------------------------------------------------------------------------------
# 2.12: Type Conversions and Rounding
# ------------------------------------------------------------------------------
print("\n--- 2.12: Type Conversions & Rounding ---")
# Explicit conversion
val_float = 9.876
val_int = int(val_float)   # Truncates (does NOT round! Drops .876)
print(f"float: {val_float} -> int() truncates to: {val_int}")

# round(number, ndigits)
rounded_2 = round(val_float, 2)
rounded_0 = round(val_float)
print(f"round({val_float}, 2) -> {rounded_2}")
print(f"round({val_float})    -> {rounded_0}")

print("\n" + "=" * 60)
print("End of Day 2 Concept Reference Demo")
print("=" * 60)
