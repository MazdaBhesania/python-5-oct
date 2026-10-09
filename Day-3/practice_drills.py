# ==============================================================================
# Day 3: Quick Concept Drills — Selections (Chapter 4)
# Note: Practice these 3 short exercises during lecture or as a warm-up!
#       No logical operators (and, or, not) needed.
# ==============================================================================

print("=" * 60)
print("             DAY 3: 3 QUICK PRACTICE DRILLS")
print("=" * 60)

# ------------------------------------------------------------------------------
# DRILL 1: Even or Odd Number Checker (Two-Way if-else)
# A number is even if dividing by 2 leaves a remainder of 0 (number % 2 == 0).
# ------------------------------------------------------------------------------
print("\n--- Drill 1: Even or Odd Checker ---")
test_number = int(input("Enter an integer to test: "))

if test_number % 2 == 0:
    print(f"Result: {test_number} is an EVEN number.")
else:
    print(f"Result: {test_number} is an ODD number.")


# ------------------------------------------------------------------------------
# DRILL 2: BMI Health Classifier (Multi-Way if-elif-else)
# BMI formula: weight_kg / (height_m ** 2)
# Interpretation (Standard Liang Chapter 4 Case Study):
#   - BMI < 18.5:        Underweight
#   - BMI < 25.0:        Normal
#   - BMI < 30.0:        Overweight
#   - 30.0 and above:    Obese
# Notice: No 'and' operator is required because each elif only runs
#         if all previous conditions were False!
# ------------------------------------------------------------------------------
print("\n--- Drill 2: BMI Health Classifier ---")
weight_kg = float(input("Enter weight in kg (e.g. 70.0): "))
height_m = float(input("Enter height in meters (e.g. 1.75): "))

bmi = weight_kg / (height_m ** 2)

if bmi < 18.5:
    status = "Underweight"
elif bmi < 25.0:
    status = "Normal weight"
elif bmi < 30.0:
    status = "Overweight"
else:
    status = "Obese"

print(f"Calculated BMI: {bmi:.2f} -> Status: {status}")


# ------------------------------------------------------------------------------
# DRILL 3: Honors Distinction Checker (Nested if)
# 1. Determine base grade:
#    - score >= 90: "A"
#    - score >= 80: "B"
#    - score >= 70: "C"
#    - else:        "Needs Review"
# 2. If the grade is "A", use a NESTED if to check if attendance is >= 95%:
#    - If attendance >= 95: award "Dean's List Honors"
#    - Otherwise: award "Dean's Commendation"
# ------------------------------------------------------------------------------
print("\n--- Drill 3: Grade & Honors (Nested if) ---")
score = float(input("Enter exam score (0-100): "))
attendance = float(input("Enter attendance percentage (0-100): "))

if score >= 90:
    print("Grade: A")
    # Nested check for Grade A students:
    if attendance >= 95:
        print("Special Honor: Awarded Dean's List with High Honors!")
    else:
        print("Special Honor: Awarded Dean's Commendation.")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: Needs Review. Please attend tutoring.")

print("\n" + "=" * 60)
print("                  DRILLS COMPLETE!")
print("=" * 60)
