# ==============================================================================
# Day 5: Quick Concept Drills — Repetition Structures & Loops
# Note: Practice these 3 short exercises during lecture or as a warm-up!
# Topics Covered:
#   - Drill 1: Multiplication Table Generator (for loop with range)
#   - Drill 2: Sentinel-Controlled Score Accumulator (while loop with sentinel = -1)
#   - Drill 3: Divisor Finder & Prime Check (for loop with loop counter & break)
# ==============================================================================

print("=" * 65)
print("             DAY 5: 3 QUICK PRACTICE DRILLS")
print("=" * 65)


# ------------------------------------------------------------------------------
# DRILL 1: Multiplication Table Generator (Liang Section 5.6)
# Prompt user for an integer N, then print its multiplication table from 1 to 12.
# Format: "N x i = Result"
# ------------------------------------------------------------------------------
print("\n--- Drill 1: Multiplication Table Generator ---")
base_num = int(input("Enter an integer for its multiplication table (e.g. 7): "))

print(f"Multiplication Table for {base_num}:")
for multiplier in range(1, 13):
    result = base_num * multiplier
    print(f"  {base_num:2d} x {multiplier:2d} = {result:4d}")


# ------------------------------------------------------------------------------
# DRILL 2: Sentinel-Controlled Score Accumulator (Liang Section 5.5)
# Prompt the user for exam scores repeatedly until they enter -1 to stop.
# Calculate: Total Sum, Count of Scores, and Average Score.
# Guard against ZeroDivisionError if the user enters -1 immediately!
# ------------------------------------------------------------------------------
print("\n--- Drill 2: Sentinel-Controlled Accumulator ---")
print("Enter test scores one by one. Enter -1 when finished:")

total_score = 0.0
count = 0

while True:
    score_entry = float(input("  Enter score (-1 to finish): "))
    if score_entry == -1:
        break  # Sentinel encountered
    
    total_score += score_entry
    count += 1

if count > 0:
    avg_score = total_score / count
    print(f"Summary: {count} score(s) entered | Total: {total_score:.1f} | Average: {avg_score:.2f}")
else:
    print("No scores were entered.")


# ------------------------------------------------------------------------------
# DRILL 3: Divisor Finder & Prime Check (Liang Sections 5.6 & 5.10)
# Prompt for an integer greater than 1. Find all its divisors from 1 to N.
# If it has exactly 2 divisors (1 and itself), announce that it is a Prime Number!
# ------------------------------------------------------------------------------
print("\n--- Drill 3: Divisor Finder & Prime Check ---")
test_val = int(input("Enter an integer > 1 to inspect (e.g. 17, 24): "))

divisors = []
for i in range(1, test_val + 1):
    if test_val % i == 0:
        divisors.append(i)

print(f"Divisors of {test_val}: {divisors}")
if len(divisors) == 2:
    print(f"Result: {test_val} is a PRIME NUMBER! (Only divisible by 1 and {test_val})")
else:
    print(f"Result: {test_val} is a COMPOSITE NUMBER with {len(divisors)} divisors.")

print("\n" + "=" * 65)
print("             DRILLS COMPLETE!")
print("=" * 65)
