# ==============================================================================
# Course: Python Programming
# Session: Day 7 (Chapter 7 & 8: 1D Lists & Multi-Dimensional Lists)
# Activity: Quick Practice Drills — 3 Rapid Warm-up Exercises
#
# Instructions:
# Practice these 3 short coding drills to master:
#   - Drill 1: List Statistics & Outlier Filtering (1D search, min, max, average)
#   - Drill 2: 1D List Transformations & List Comprehensions (mapping & filtering)
#   - Drill 3: 2D Grid Transposition & Row/Column Analysis (Matrix manipulation)
# ==============================================================================

print("=" * 68)
print("             DAY 7: 3 QUICK PRACTICE DRILLS")
print("=" * 68)


# ------------------------------------------------------------------------------
# DRILL 1: List Statistics & Outlier Filter (Liang 7.3 & 7.4)
# Goal:
#   1. Prompt or load a list of student quiz marks (numbers).
#   2. Compute and print: Count, Min, Max, Total Sum, and Average (rounded to 2 decimals).
#   3. Remove the single lowest score (outlier) and compute the new adjusted average.
# ------------------------------------------------------------------------------
print("\n--- Drill 1: Quiz Scores Analysis & Outlier Dropping ---")
quiz_scores = [78, 92, 45, 88, 95, 82, 60, 91]
print(f"Original Scores: {quiz_scores}")

# Compute core statistics
score_count = len(quiz_scores)
lowest_score = min(quiz_scores)
highest_score = max(quiz_scores)
total_score = sum(quiz_scores)
avg_score = total_score / score_count

print(f"Count of Scores: {score_count}")
print(f"Lowest Score:    {lowest_score}")
print(f"Highest Score:   {highest_score}")
print(f"Class Average:   {avg_score:.2f}")

# Create a copy and remove lowest score
adjusted_scores = quiz_scores.copy()
adjusted_scores.remove(lowest_score)
adjusted_avg = sum(adjusted_scores) / len(adjusted_scores)

print(f"Scores after dropping lowest ({lowest_score}): {adjusted_scores}")
print(f"Adjusted Class Average: {adjusted_avg:.2f}")


# ------------------------------------------------------------------------------
# DRILL 2: List Comprehensions & Word Length Filter (Liang 7.11)
# Goal:
#   Given a list of planet names:
#   1. Filter names that have 6 or more characters using a list comprehension.
#   2. Create a list of lengths corresponding to each planet name.
#   3. Create an uppercase copy of all planet names.
# ------------------------------------------------------------------------------
print("\n--- Drill 2: List Comprehensions with String Sequences ---")
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print(f"Original Planets: {planets}")

# 1. Long names (>= 6 chars)
long_planets = [p for p in planets if len(p) >= 6]
print(f"Planets with >= 6 characters: {long_planets}")

# 2. Length of each planet
name_lengths = [len(p) for p in planets]
print(f"Planet name lengths: {name_lengths}")

# 3. Uppercase transform
caps_planets = [p.upper() for p in planets]
print(f"Uppercase Planets: {caps_planets}")


# ------------------------------------------------------------------------------
# DRILL 3: 2D Matrix Transpose & Grid Summary (Liang 8.4 - 8.6)
# Goal:
#   Given a 3x2 matrix (3 rows, 2 columns):
#   1. Display original matrix formatted row by row.
#   2. Compute the transpose (flip rows and columns -> 2 rows, 3 columns).
#   3. Calculate the sum of every column.
# ------------------------------------------------------------------------------
print("\n--- Drill 3: 2D Matrix Transpose & Column Totals ---")
matrix_3x2 = [
    [10, 20],
    [30, 40],
    [50, 60]
]

print("Original 3x2 Grid:")
for row in matrix_3x2:
    print(" ", row)

rows = len(matrix_3x2)
cols = len(matrix_3x2[0])

# Compute Transpose: row i, col j becomes row j, col i
transposed = [[matrix_3x2[r][c] for r in range(rows)] for c in range(cols)]

print("Transposed 2x3 Grid:")
for row in transposed:
    print(" ", row)

# Column sums of original matrix
col_sums = []
for c in range(cols):
    c_sum = sum(matrix_3x2[r][c] for r in range(rows))
    col_sums.append(c_sum)

print(f"Original Column Sums (Col 0, Col 1): {col_sums}")

print("\n" + "=" * 68)
print(">>> DAY 7 PRACTICE DRILLS COMPLETE!")
print("=" * 68)
