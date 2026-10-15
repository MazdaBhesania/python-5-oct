# ==============================================================================
# Course: Python Programming (Session 5)
# Topic: Repetition Structures & Loops
# Textbook Chapter: Liang Chapter 5
# Sections Covered:
#   - 5.2: The while Loop (Syntax, condition evaluation, loop counter)
#   - 5.3: Case Study: Guessing Numbers
#   - 5.4: Loop Design Strategies (Body -> Condition -> Variable Update)
#   - 5.5: Controlling Loops with Sentinel Values
#   - 5.6: The for Loop and the range() Function
#   - 5.7: Nested Loops (Tables, coordinate grids)
#   - 5.8: Minimizing Numerical Errors (Float accumulators)
#   - 5.10: Loop Control Keywords: break and continue
# ==============================================================================

import random

print("=" * 70)
print("     DAY 5: MASTERING LOOPS (WHILE, FOR, SENTINELS & CONTROL)")
print("=" * 70)


# ------------------------------------------------------------------------------
# 5.2: Counter-Controlled while Loop
# ------------------------------------------------------------------------------
print("\n--- 5.2: Counter-Controlled while Loop ---")
# A while loop executes its body as long as its boolean condition remains True.
# Three essential parts of a counter-controlled loop:
#   1. Initialization: counter = 1
#   2. Condition:      counter <= 5
#   3. Update:         counter += 1   (Crucial! Omitting this creates an INFINITE LOOP)

counter = 1
while counter <= 5:
    print(f"  Iteration {counter}: Blastoff in {6 - counter}...")
    counter += 1

print("  Countdown complete!")


# ------------------------------------------------------------------------------
# 5.5: Sentinel-Controlled while Loop
# ------------------------------------------------------------------------------
print("\n--- 5.5: Sentinel-Controlled Loop ---")
# A sentinel value is a special input value that signals the end of input.
# Example: Summing numbers until the user enters 0.
# Here we simulate with a predefined list of user inputs for demonstration:
simulated_inputs = [15, 20, 35, 0]
input_index = 0

total_sum = 0
count = 0

print("  Simulating user entering numbers to sum (Sentinel = 0):")
while True:
    val = simulated_inputs[input_index]
    input_index += 1
    print(f"    Entered: {val}")
    
    if val == 0:  # Sentinel encountered
        break
    total_sum += val
    count += 1

average = total_sum / count if count > 0 else 0.0
print(f"  Total Sum: {total_sum} | Count: {count} | Average: {average:.2f}")


# ------------------------------------------------------------------------------
# 5.6: The for Loop and the range() Function
# ------------------------------------------------------------------------------
print("\n--- 5.6: The for Loop & range() Function ---")
# range() has three distinct forms:
#   1. range(stop)             -> 0 to stop-1 (step = 1)
#   2. range(start, stop)      -> start to stop-1 (step = 1)
#   3. range(start, stop, step)-> start to stop-1 by step increments

print("1. range(4):")
for i in range(4):
    print(f"   i = {i}", end=" | ")
print()

print("2. range(5, 10):")
for i in range(5, 10):
    print(f"   i = {i}", end=" | ")
print()

print("3. range(10, 30, 5) [Step +5]:")
for i in range(10, 30, 5):
    print(f"   i = {i}", end=" | ")
print()

print("4. range(10, 0, -2) [Counting Downwards]:")
for i in range(10, 0, -2):
    print(f"   i = {i}", end=" | ")
print()


# ------------------------------------------------------------------------------
# 5.7: Nested Loops (Multiplication & Grid Generation)
# ------------------------------------------------------------------------------
print("\n--- 5.7: Nested Loops (Mini Multiplication Grid 1-5) ---")
# Outer loop controls rows; Inner loop controls columns.
# For every 1 step of the outer loop, the inner loop completes all its steps!

# Header
print("     ", end="")
for col in range(1, 6):
    print(f"{col:4d}", end="")
print("\n" + "    -" + "----" * 5)

for row in range(1, 6):
    print(f"{row:2d} |", end="")
    for col in range(1, 6):
        product = row * col
        print(f"{product:4d}", end="")
    print()  # Newline after each row


# ------------------------------------------------------------------------------
# 5.10: Loop Control Keywords: break and continue
# ------------------------------------------------------------------------------
print("\n--- 5.10: Loop Control Keywords (break and continue) ---")
# 'continue': Skips the rest of the CURRENT iteration and jumps to the next.
# 'break'   : Terminates the loop ENTIRELY and exits immediately.

print("Demonstrating 'continue' (skip multiples of 3):")
for n in range(1, 10):
    if n % 3 == 0:
        continue  # Skip 3, 6, 9
    print(f"  Processing n = {n}")

print("\nDemonstrating 'break' (stop when n == 7):")
for n in range(1, 15):
    if n == 7:
        print("  Hit emergency stop condition (n == 7)! Breaking out.")
        break
    print(f"  Running n = {n}")


# ------------------------------------------------------------------------------
# 5.3: Case Study: Number Guessing Logic
# ------------------------------------------------------------------------------
print("\n--- 5.3: Case Study — Number Guessing Logic ---")
secret_number = 42
test_guesses = [20, 60, 42]
attempts = 0

print(f"Secret Target is hidden. Testing simulation guesses: {test_guesses}")
for guess in test_guesses:
    attempts += 1
    print(f"  Attempt {attempts}: Guessed {guess} -> ", end="")
    if guess < secret_number:
        print("Too low! ⬆️")
    elif guess > secret_number:
        print("Too high! ⬇️")
    else:
        print(f"BINGO! Correct in {attempts} attempt(s)! 🎉")
        break


# ------------------------------------------------------------------------------
# Accumulator Patterns: Sum, Count, Min, Max
# ------------------------------------------------------------------------------
print("\n--- Accumulator Pattern: Computing Stats on a Sequence ---")
scores = [78, 92, 64, 88, 95, 71]

total_score = 0
highest_score = scores[0]
lowest_score = scores[0]

for score in scores:
    total_score += score
    if score > highest_score:
        highest_score = score
    if score < lowest_score:
        lowest_score = score

avg_score = total_score / len(scores)
print(f"Scores:  {scores}")
print(f"Sum:     {total_score}")
print(f"Average: {avg_score:.2f}")
print(f"Highest: {highest_score}")
print(f"Lowest:  {lowest_score}")

print("\n" + "=" * 70)
print("     DEMO COMPLETE! READY FOR DAY 5 HANDS-ON ACTIVITIES!")
print("=" * 70)
