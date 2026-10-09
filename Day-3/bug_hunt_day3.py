# ==============================================================================
# Day 3: In-Class Activity — Selection Statements Bug Hunt
# Topics: Chapter 4 (Relational Operators, if, if-else, if-elif-else, nested if)
# Note: Logical operators (and, or, not) are NOT used in these challenges.
#
# Instructions:
# 1. Read through each challenge below.
# 2. Uncomment the buggy line(s) under "UNCOMMENT TO TEST".
# 3. Run the file: python3 Day-3/bug_hunt_day3.py
# 4. Observe the error message or incorrect program logic.
# 5. Fix the bug so that all 5 challenges produce the expected output!
# ==============================================================================

print("=" * 60)
print("             DAY 3 BUG HUNT: 5 CODING CHALLENGES")
print("=" * 60)


# ------------------------------------------------------------------------------
# CHALLENGE 1: Assignment '=' vs Equality Comparison '=='
# Goal: Check if a user's role is "admin" to grant access.
# Problem: Using a single '=' attempts to assign a value inside an 'if' test,
#          causing a SyntaxError in Python.
# Fix: Use '==' to compare equality.
# ------------------------------------------------------------------------------
print("\n[Challenge 1]")
user_role = "admin"

# BUGGY VERSION (Uncomment to test):
# if user_role = "admin":
#     print("Access granted to administrative portal.")

# FIXED VERSION:
if user_role == "admin":
    print("Access granted to administrative portal.")


# ------------------------------------------------------------------------------
# CHALLENGE 2: Missing Colons on Selection Headers
# Goal: Test if temperature is above freezing (32 F).
# Problem: Python requires a colon (:) at the end of 'if', 'elif', and 'else' lines.
# Fix: Add the missing colon after the conditions.
# ------------------------------------------------------------------------------
print("\n[Challenge 2]")
temperature = 45

# BUGGY VERSION (Uncomment to test):
# if temperature > 32
#     print(f"Temperature {temperature}F: Above freezing.")
# else
#     print(f"Temperature {temperature}F: Freezing or below.")

# FIXED VERSION:
if temperature > 32:
    print(f"Temperature {temperature}F: Above freezing.")
else:
    print(f"Temperature {temperature}F: Freezing or below.")


# ------------------------------------------------------------------------------
# CHALLENGE 3: Unintended Unconditional Execution (Indentation Pitfall)
# Goal: Only print the celebration message if score is at least 90.
# Problem: The second print statement was not indented, so it runs for ALL scores,
#          even when the student failed!
# Fix: Indent the second print statement so it belongs to the 'if' body.
# ------------------------------------------------------------------------------
print("\n[Challenge 3]")
student_score = 65

# BUGGY VERSION (Uncomment to test - notice what prints even with score 65!):
# if student_score >= 90:
#     print("Status: Outstanding performance!")
#     print("Congratulations! You won a certificate of honor!")

# FIXED VERSION:
if student_score >= 90:
    print("Status: Outstanding performance!")
    print("Congratulations! You won a certificate of honor!")
else:
    print(f"Status: Score {student_score}. No certificate awarded this time.")


# ------------------------------------------------------------------------------
# CHALLENGE 4: The Order Trap in Multi-Way if-elif-else
# Goal: Assign medals based on marathon time (in minutes):
#       - Under 120 mins: Gold
#       - Under 150 mins: Silver
#       - Under 180 mins: Bronze
#       - 180 or more: Finisher Ribbon
# Problem: Checking '< 180' FIRST means a runner with 110 minutes matches
#          '< 180' and gets Bronze instead of Gold!
# Fix: Order multi-way conditions from most restrictive (< 120) to least.
# ------------------------------------------------------------------------------
print("\n[Challenge 4]")
runner_time = 115   # 115 minutes should earn a GOLD medal!

# BUGGY VERSION (Uncomment to test):
# if runner_time < 180:
#     medal = "Bronze Medal"
# elif runner_time < 150:
#     medal = "Silver Medal"
# elif runner_time < 120:
#     medal = "Gold Medal"
# else:
#     medal = "Finisher Ribbon"

# FIXED VERSION:
if runner_time < 120:
    medal = "Gold Medal"
elif runner_time < 150:
    medal = "Silver Medal"
elif runner_time < 180:
    medal = "Bronze Medal"
else:
    medal = "Finisher Ribbon"

print(f"Runner Time: {runner_time} mins -> Awarded: {medal}")


# ------------------------------------------------------------------------------
# CHALLENGE 5: Nested 'if' and the Dangling 'else' Trap
# Goal: Verify account access:
#       1. Check if account is active.
#       2. If active, check if PIN matches 1234.
#       3. If PIN is wrong, say "Incorrect PIN".
#       4. If account is inactive, say "Account is deactivated".
# Problem: The 'else' was misaligned, causing the wrong error message to show!
# Fix: Align each 'else' with its matching 'if' level.
# ------------------------------------------------------------------------------
print("\n[Challenge 5]")
is_account_active = True
entered_pin = 9999      # Incorrect PIN! Should say "Incorrect PIN"

# BUGGY VERSION (Uncomment to test):
# if is_account_active == True:
#     if entered_pin == 1234:
#         print("Welcome to your bank account!")
# else:
#     print("Security Alert: Account is deactivated!")

# FIXED VERSION (Correctly aligned nested if-else):
if is_account_active == True:
    if entered_pin == 1234:
        print("Welcome to your bank account!")
    else:
        print("Security Alert: Incorrect PIN entered!")
else:
    print("Security Alert: Account is deactivated!")

print("\n" + "=" * 60)
print("     ALL CHALLENGES COMPLETED & VERIFIED SUCCESSFULLY!")
print("=" * 60)
