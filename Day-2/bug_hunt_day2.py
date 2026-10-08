# ==============================================================================
# Day 2: In-Class Activity — Elementary Programming Bug Hunt
# Topics: Liang Chapter 2 (Sections 2.1 – 2.12)
#
# Instructions:
# 1. Read through each challenge below.
# 2. Uncomment the buggy line(s) under "UNCOMMENT TO TEST".
# 3. Run the file: python3 bug_hunt_day2.py
# 4. Read the Python error message or examine incorrect output.
# 5. Fix the bug so that all challenges pass!
# ==============================================================================

print("=" * 60)
print("             DAY 2 BUG HUNT: 5 CODING CHALLENGES")
print("=" * 60)


# ------------------------------------------------------------------------------
# CHALLENGE 1: The input() String Trap (Sections 2.3 & 2.12)
# Goal: We want to double the user's score.
# Problem: input() always returns a str. Multiplying a string by 2 duplicates it!
# Example: "50" * 2 results in "5050" instead of 100!
# Fix: Cast the input value to an int() or float().
# ------------------------------------------------------------------------------
print("\n[Challenge 1]")
raw_score = "50"     # Simulates: input("Enter your score: ")
# BUGGY VERSION (Uncomment to test):
# doubled_score = raw_score * 2
# FIXED VERSION:
doubled_score = int(raw_score) * 2
print("Doubled Score (should be 100):", doubled_score)


# ------------------------------------------------------------------------------
# CHALLENGE 2: Invalid Variable Identifiers (Section 2.4)
# Goal: Store the top two tournament scores.
# Problem: Variable names cannot start with a digit, and cannot contain hyphens.
# Fix: Rename the variables to follow snake_case naming rules.
# ------------------------------------------------------------------------------
print("\n[Challenge 2]")
# BUGGY VERSION (Uncomment to test):
# 1st_score = 98
# runner-up = 85
# FIXED VERSION:
first_score = 98
runner_up = 85
print("First score:", first_score, "| Runner-up score:", runner_up)


# ------------------------------------------------------------------------------
# CHALLENGE 3: Integer Division vs Float Division (Section 2.8)
# Goal: Calculate how many whole 6-pack egg cartons 26 eggs can fill.
# Problem: Using float division (/) produces 4.333333333333333 cartons.
# Fix: Use floor/integer division (//) to get whole cartons, and modulo (%) for leftover eggs.
# ------------------------------------------------------------------------------
print("\n[Challenge 3]")
total_eggs = 26
EGGS_PER_CARTON = 6
# BUGGY VERSION:
# full_cartons = total_eggs / EGGS_PER_CARTON
# leftover_eggs = 0
# FIXED VERSION:
full_cartons = total_eggs // EGGS_PER_CARTON
leftover_eggs = total_eggs % EGGS_PER_CARTON
print(f"26 eggs fill {full_cartons} full cartons with {leftover_eggs} eggs left over.")


# ------------------------------------------------------------------------------
# CHALLENGE 4: Operator Precedence Trap (Section 2.10)
# Goal: Calculate the average of 3 test scores: 80, 90, 100. (Expected: 90.0)
# Problem: Without parentheses, score3 / 3 is evaluated first due to PEMDAS!
# Fix: Wrap the addition in parentheses before dividing.
# ------------------------------------------------------------------------------
print("\n[Challenge 4]")
s1, s2, s3 = 80, 90, 100
# BUGGY VERSION:
# calculated_avg = s1 + s2 + s3 / 3   # Evaluates to 80 + 90 + 33.33 = 203.33
# FIXED VERSION:
calculated_avg = (s1 + s2 + s3) / 3
print("Average of 80, 90, 100 (should be 90.0):", calculated_avg)


# ------------------------------------------------------------------------------
# CHALLENGE 5: Simultaneous Assignment Mismatch (Section 2.6)
# Goal: Assign initial coordinates for player_x and player_y.
# Problem: Python requires the same number of variables on the left as values on the right!
# Fix: Ensure variable count matches value count, or assign properly.
# ------------------------------------------------------------------------------
print("\n[Challenge 5]")
# BUGGY VERSION (Uncomment to test):
# player_x, player_y = 100        # TypeError: cannot unpack non-iterable int object
# player_x, player_y = 10, 20, 30 # ValueError: too many values to unpack
# FIXED VERSION:
player_x, player_y = 10, 20
print(f"Player starting position -> X: {player_x}, Y: {player_y}")

print("\n" + "=" * 60)
print("🎉 All 5 Challenge Checks Passed Successfully!")
print("=" * 60)
