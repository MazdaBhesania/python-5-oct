# ==============================================================================
# Day 5: In-Class Activity — Loop Debugging Bug Hunt
# Topics:
#   - Off-by-one errors in range()
#   - Infinite while loops (missing update variable)
#   - Accumulator reset trap (variable scope inside loop)
#   - Premature loop exit (misplaced break)
#   - Skipped update variable before continue in while loop
#
# Instructions:
# 1. Read through each challenge below.
# 2. Uncomment the buggy line(s) under "UNCOMMENT TO TEST".
# 3. Run the file: python3 Day-5/bug_hunt_day5.py
# 4. Observe the infinite loop, error message, or faulty calculation.
# 5. Fix the bug so that all 5 challenges produce the expected output!
# ==============================================================================

print("=" * 65)
print("             DAY 5 BUG HUNT: 5 CODING CHALLENGES")
print("=" * 65)


# ------------------------------------------------------------------------------
# CHALLENGE 1: Off-by-One Error in range()
# Goal: Print all numbers from 1 to 10 inclusive and compute their sum.
# Problem: range(start, stop) generates numbers UP TO, BUT NOT INCLUDING, stop!
#          range(1, 10) stops at 9, leaving out 10.
# Fix: Change stop to 11: range(1, 11).
# ------------------------------------------------------------------------------
print("\n[Challenge 1: Off-by-One Error]")

# BUGGY VERSION (Uncomment to test):
# numbers_sum = 0
# for num in range(1, 10):
#     numbers_sum += num
# print(f"Sum of 1 to 10: {numbers_sum} (BUG: got 45 instead of 55!)")

# FIXED VERSION:
numbers_sum = 0
for num in range(1, 11):
    numbers_sum += num
print(f"Sum of 1 to 10: {numbers_sum} (Correct: 55)")


# ------------------------------------------------------------------------------
# CHALLENGE 2: Infinite while Loop (Missing Counter Update)
# Goal: Count down from 3 to 1, then print "Blastoff!".
# Problem: Forgetting to decrement the counter inside the loop body causes
#          the condition 'countdown > 0' to stay True forever!
# Fix: Add 'countdown -= 1' inside the while loop body.
# ------------------------------------------------------------------------------
print("\n[Challenge 2: Infinite Loop Prevention]")
countdown = 3

# BUGGY VERSION (Uncomment to test - WARNING: INFINITE LOOP! Press Ctrl+C to stop):
# while countdown > 0:
#     print(f"  T-minus {countdown}...")
#     # Missing: countdown -= 1

# FIXED VERSION:
while countdown > 0:
    print(f"  T-minus {countdown}...")
    countdown -= 1
print("  Blastoff!")


# ------------------------------------------------------------------------------
# CHALLENGE 3: Accumulator Reset Trap
# Goal: Compute the total cost of 4 shopping cart items: [12.50, 4.00, 8.50, 25.00].
# Problem: Initializing the running sum accumulator variable INSIDE the loop
#          resets the total back to 0 on every single iteration!
# Fix: Initialize 'total_cost = 0.0' OUTSIDE (before) the loop.
# ------------------------------------------------------------------------------
print("\n[Challenge 3: Accumulator Variable Scope Trap]")
cart_prices = [12.50, 4.00, 8.50, 25.00]

# BUGGY VERSION (Uncomment to test):
# for price in cart_prices:
#     total_cost = 0.0  # BUG: Resetting total on every item!
#     total_cost += price
# print(f"Cart total: ${total_cost:.2f} (BUG: only captures the last item!)")

# FIXED VERSION:
total_cost = 0.0  # Correctly initialized before the loop begins
for price in cart_prices:
    total_cost += price
print(f"Cart total: ${total_cost:.2f} (Correct: $50.00)")


# ------------------------------------------------------------------------------
# CHALLENGE 4: Premature Loop Exit with Misplaced break
# Goal: Search a list of student scores [68, 74, 95, 82] to see if ANY score >= 90.
# Problem: Placing 'break' in an 'else' block causes the loop to exit on the
#          very FIRST item (68) without checking the rest of the list!
# Fix: Remove the 'else: break' branch so the loop continues searching until
#      the condition is met or all items are inspected.
# ------------------------------------------------------------------------------
print("\n[Challenge 4: Premature Exit with break]")
scores = [68, 74, 95, 82]
has_honor_score = False

# BUGGY VERSION (Uncomment to test):
# for s in scores:
#     if s >= 90:
#         has_honor_score = True
#         break
#     else:
#         break  # BUG: Immediately aborts on 68 without inspecting 74 or 95!
# print(f"Found score >= 90? {has_honor_score} (BUG: False)")

# FIXED VERSION:
for s in scores:
    if s >= 90:
        has_honor_score = True
        break
print(f"Found score >= 90? {has_honor_score} (Correct: True)")


# ------------------------------------------------------------------------------
# CHALLENGE 5: Skipped Counter Update with continue in while Loop
# Goal: Print only the even numbers between 1 and 6 using a while loop.
# Problem: When 'continue' is executed, Python skips all remaining statements
#          in the loop body — including the counter increment!
#          This causes the counter to freeze at that value forever.
# Fix: Always ensure the loop counter is incremented BEFORE calling 'continue',
#      or re-structure the loop so the increment is never bypassed.
# ------------------------------------------------------------------------------
print("\n[Challenge 5: while Loop with continue]")
num = 0

# BUGGY VERSION (Uncomment to test - WARNING: FREEZES LOOP):
# while num < 6:
#     if num % 2 != 0:
#         continue  # BUG: num += 1 is skipped, freezing num forever on 1!
#     print(f"  Even: {num}")
#     num += 1

# FIXED VERSION:
while num < 6:
    num += 1
    if num % 2 != 0:
        continue  # Safely skip odd numbers; num was already incremented
    print(f"  Even: {num}")

print("\n" + "=" * 65)
print("             ALL BUG HUNT CHALLENGES RESOLVED!")
print("=" * 65)
