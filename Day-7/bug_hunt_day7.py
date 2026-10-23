# ==============================================================================
# Course: Python Programming
# Session: Day 7 (Chapter 7 & 8: 1D Lists & Multi-Dimensional Lists)
# Activity: The Bug Hunt — 5 Tricky List & Matrix Bugs
#
# Instructions:
# 1. Read through each challenge below.
# 2. Uncomment the buggy line(s) under "UNCOMMENT TO TEST".
# 3. Run the file: python3 Day-7/bug_hunt_day7.py
# 4. Observe the error message or faulty logic.
# 5. Fix the bug so that all 5 challenges produce the expected output!
# ==============================================================================

import copy

print("=" * 68)
print("       DAY 7 BUG HUNT: 5 LIST & MATRIX CODING CHALLENGES")
print("=" * 68)


# ------------------------------------------------------------------------------
# CHALLENGE 1: The Shallow 2D Multiplication Trap
# Goal: Create a 3x3 game board initialized with empty string "."
#       Place a token 'X' at row 0, column 1.
# Problem: Using `[["."] * 3] * 3` duplicates references to a SINGLE list.
#          Modifying [0][1] also mutates [1][1] and [2][1]!
# Fix: Use list comprehension `[["." for _ in range(3)] for _ in range(3)]`
#      so each row is a distinct list in memory.
# ------------------------------------------------------------------------------
print("\n[Challenge 1: 2D Matrix Row Reference Duplication]")

# BUGGY VERSION (Uncomment to test):
# board = [["."] * 3] * 3
# board[0][1] = "X"
# print("Buggy Board:")
# for row in board:
#     print(row)
# Expected only row 0 to have "X", but all rows got "X"!

# FIXED VERSION:
board = [["." for _ in range(3)] for _ in range(3)]
board[0][1] = "X"
print("Fixed Board:")
for row in board:
    print(row)


# ------------------------------------------------------------------------------
# CHALLENGE 2: Off-By-One IndexError in Traversal
# Goal: Loop through all items in `scores` using indexing and print each element.
# Problem: `range(1, len(scores) + 1)` misses index 0 and attempts `scores[len(scores)]`,
#          triggering an `IndexError: list index out of range`.
# Fix: In Python, indexing is 0-based and ends at `len - 1`. Use `range(len(scores))`.
# ------------------------------------------------------------------------------
print("\n[Challenge 2: 0-Based Indexing & Off-by-One Trap]")
scores = [95, 82, 67, 100, 74]

# BUGGY VERSION (Uncomment to test):
# try:
#     for i in range(1, len(scores) + 1):
#         print(f"Item at {i}: {scores[i]}")
# except IndexError as e:
#     print(f"Caught IndexError: {e}")

# FIXED VERSION:
print("Correctly indexed traversal:")
for i in range(len(scores)):
    print(f"  Index {i}: {scores[i]}")


# ------------------------------------------------------------------------------
# CHALLENGE 3: Mutating a List While Iterating Over It
# Goal: Remove all negative numbers from `temperatures`.
# Problem: Deleting elements with `remove()` or `pop()` during `for temp in temperatures:`
#          shifts list indices leftward, causing Python to skip the next adjacent element!
# Fix: Iterate over a copy of the list `temperatures[:]`, or use list comprehension.
# ------------------------------------------------------------------------------
print("\n[Challenge 3: Mutating a List During Iteration]")
temperatures = [15, -3, -7, 22, -1, 30]

# BUGGY VERSION (Uncomment to test):
# buggy_temps = [15, -3, -7, 22, -1, 30]
# for t in buggy_temps:
#     if t < 0:
#         buggy_temps.remove(t)
# print(f"Buggy filtered temps (skipped -7!): {buggy_temps}")

# FIXED VERSION (Using List Comprehension):
temperatures = [t for t in temperatures if t >= 0]
print(f"Correctly filtered non-negative temperatures: {temperatures}")


# ------------------------------------------------------------------------------
# CHALLENGE 4: List Method Return Value Trap (sort vs sorted / append vs None)
# Goal: Sort student names alphabetically and store the sorted list.
# Problem: `.sort()` modifies the list IN-PLACE and returns `None`!
#          Assigning `sorted_names = names.sort()` results in `sorted_names` being `None`.
# Fix: Either call `names.sort()` and use `names`, or use `sorted_names = sorted(names)`.
# ------------------------------------------------------------------------------
print("\n[Challenge 4: In-Place Method Return Value Trap]")
names = ["Zara", "Alex", "Marcus", "Elena"]

# BUGGY VERSION (Uncomment to test):
# sorted_names = names.sort()
# print(f"sorted_names: {sorted_names} (BUG: NoneType!)")

# FIXED VERSION:
sorted_names = sorted(names)
print(f"Original list preserved: {names}")
print(f"Sorted names list: {sorted_names}")


# ------------------------------------------------------------------------------
# CHALLENGE 5: Matrix Row vs Column Index Inversion
# Goal: Calculate the sum of column 0 in a 3x3 matrix:
#       Matrix:
#       [10, 20, 30]
#       [40, 50, 60]
#       [70, 80, 90]
#       Column 0 values are 10, 40, 70 -> Sum should be 120.
# Problem: Accessing `matrix[0][r]` iterates through ROW 0 instead of COLUMN 0!
# Fix: Access `matrix[r][0]` where row index `r` varies and col index is fixed at 0.
# ------------------------------------------------------------------------------
print("\n[Challenge 5: Matrix Row vs Column Coordinate Inversion]")
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# BUGGY VERSION (Uncomment to test):
# buggy_col0_sum = 0
# for i in range(len(matrix)):
#     buggy_col0_sum += matrix[0][i]  # Summing row 0 (10 + 20 + 30 = 60)
# print(f"Buggy Col 0 sum: {buggy_col0_sum} (BUG: computed row 0 instead!)")

# FIXED VERSION:
correct_col0_sum = 0
for r in range(len(matrix)):
    correct_col0_sum += matrix[r][0]  # Access row r, column 0
print(f"Correct Column 0 sum: {correct_col0_sum} (Expected: 120)")

print("\n" + "=" * 68)
print(">>> ALL 5 DAY 7 BUG CHALLENGES RESOLVED SUCCESSFULLY!")
print("=" * 68)
