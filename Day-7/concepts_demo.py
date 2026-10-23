# ==============================================================================
# Course: Python Programming
# Session: Day 7 (Chapter 7 & 8: 1D Lists & Multi-Dimensional Lists)
# Textbook Reference: Liang, Chapter 7 (1D Lists) & Chapter 8 (Multi-Dimensional Lists)
#
# Topics Covered:
#   - Part 1: Creating & Initializing 1D Lists (literals, list(), range(), repetition)
#   - Part 2: Indexing, Slicing & Sequence Operations (positive/negative indices, step)
#   - Part 3: List Traversal & Comprehensions (by element, by index, filtering, mapping)
#   - Part 4: In-Place Modification vs Methods (append, extend, insert, pop, remove, sort, reverse)
#   - Part 5: Search & Aggregation (in/not in, index, count, len, min, max, sum)
#   - Part 6: Multi-Dimensional Lists & Matrices (grid representation, coordinates row/col)
#   - Part 7: Nested Iterations & Matrix Transformations (row sums, col sums, diagonals)
#   - Part 8: Memory Model & Copying (shallow copy vs deep copy, references vs values)
# ==============================================================================

import copy
import random

print("=" * 76)
print("     DAY 7: MASTERING 1D & MULTI-DIMENSIONAL LISTS IN PYTHON")
print("=" * 76)


# ==============================================================================
# PART 1: CREATING & INITIALIZING 1D LISTS (Liang 7.1 - 7.3)
# ==============================================================================
print("\n" + "=" * 55)
print(">>> PART 1: CREATING & INITIALIZING 1D LISTS")
print("=" * 55)

# 1.1 List Literals & Empty Lists
empty_list_literal = []
empty_list_constructor = list()
numeric_list = [10, 20, 30, 40, 50]
mixed_list = ["Alpha", 42, 98.6, True, [1, 2]]  # Lists can hold heterogeneous types

# 1.2 Creating Lists from Iterables
chars = list("PYTHON")              # ['P', 'Y', 'T', 'H', 'O', 'N']
numbers_seq = list(range(1, 11))    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1.3 List Repetition (*) and Concatenation (+)
zeros = [0] * 6                     # [0, 0, 0, 0, 0, 0]
combined = [1, 2] + [3, 4]          # [1, 2, 3, 4]

print(f"[1.1] Mixed List: {mixed_list}")
print(f"[1.2] From String: {chars}")
print(f"[1.2] From range(1, 11): {numbers_seq}")
print(f"[1.3] Repeated zeros: {zeros}")
print(f"[1.3] Concatenated list: {combined}")


# ==============================================================================
# PART 2: INDEXING, SLICING & STEP (Liang 7.2)
# ==============================================================================
print("\n" + "=" * 55)
print(">>> PART 2: INDEXING & SLICING (list[start:end:step])")
print("=" * 55)

scores = [88, 92, 79, 95, 100, 64, 85, 91]
# Indices: 0   1   2   3    4   5   6   7
# Neg:    -8  -7  -6  -5   -4  -3  -2  -1

print(f"Original Scores: {scores}")
print(f"First element (scores[0]): {scores[0]}")
print(f"Last element (scores[-1]): {scores[-1]}")
print(f"Third from end (scores[-3]): {scores[-3]}")

# Slicing: [start : stop : step] (stop index is EXCLUSIVE)
print(f"Slice [1:5]: {scores[1:5]}")         # elements at indices 1, 2, 3, 4
print(f"First 3 elements [:3]: {scores[:3]}")
print(f"Elements from index 4 onwards [4:]: {scores[4:]}")
print(f"Every 2nd element [::2]: {scores[::2]}")
print(f"Reversed list [::-1]: {scores[::-1]}")


# ==============================================================================
# PART 3: TRAVERSAL & LIST COMPREHENSIONS (Liang 7.3 & 7.11)
# ==============================================================================
print("\n" + "=" * 55)
print(">>> PART 3: TRAVERSAL & LIST COMPREHENSIONS")
print("=" * 55)

inventory = ["Shield", "Potion", "Blaster", "Medkit"]

# 3.1 Loop by Element
print("Traversal by Element:")
for item in inventory:
    print(f"  - {item}")

# 3.2 Loop by Index with len()
print("Traversal by Index:")
for i in range(len(inventory)):
    print(f"  Slot {i}: {inventory[i]}")

# 3.3 Traversal with enumerate()
print("Traversal with enumerate():")
for index, item in enumerate(inventory, start=1):
    print(f"  Item #{index}: {item}")

# 3.4 List Comprehensions: [expression for item in iterable if condition]
raw_readings = [12, -4, 25, 0, 18, -9, 31, 14]
# Filter only positive readings:
positive_readings = [val for val in raw_readings if val > 0]
# Convert readings to Kelvin (C + 273.15):
kelvin_temps = [round(val + 273.15, 2) for val in raw_readings if val >= 0]

print(f"Raw Readings: {raw_readings}")
print(f"Positive Readings (Comprehension): {positive_readings}")
print(f"Kelvin Temps (Comprehension): {kelvin_temps}")


# ==============================================================================
# PART 4: MUTABLE LIST METHODS (Liang 7.5 - 7.8)
# ==============================================================================
print("\n" + "=" * 55)
print(">>> PART 4: MUTABLE IN-PLACE LIST METHODS")
print("=" * 55)

fleet = ["Apollo", "Voyager"]
print(f"Initial Fleet: {fleet}")

# 4.1 append(item) - Adds one item to the end
fleet.append("Discovery")
print(f"After append('Discovery'): {fleet}")

# 4.2 insert(index, item) - Inserts at specific position
fleet.insert(1, "Enterprise")
print(f"After insert(1, 'Enterprise'): {fleet}")

# 4.3 extend(iterable) - Appends all elements from another iterable
fleet.extend(["Galactica", "Millennium Falcon"])
print(f"After extend(['Galactica', 'Millennium Falcon']): {fleet}")

# 4.4 pop([index]) - Removes and returns element at index (default: last)
last_ship = fleet.pop()
second_ship = fleet.pop(1)
print(f"Popped last: '{last_ship}', Popped index 1: '{second_ship}'")
print(f"Fleet after pops: {fleet}")

# 4.5 remove(item) - Removes first occurrence of item
fleet.remove("Apollo")
print(f"After remove('Apollo'): {fleet}")

# 4.6 sort() and reverse() vs sorted() and reversed()
numbers = [42, 17, 88, 3, 25]
# In-place sort (modifies original, returns None):
numbers.sort()
print(f"In-place sorted numbers: {numbers}")
numbers.sort(reverse=True)
print(f"In-place reverse sorted: {numbers}")

# Non-destructive sorting with sorted():
original = [5, 1, 4, 2]
new_sorted = sorted(original)
print(f"Original untouched: {original}, New list from sorted(): {new_sorted}")


# ==============================================================================
# PART 5: SEARCH & AGGREGATION UTILITIES (Liang 7.4)
# ==============================================================================
print("\n" + "=" * 55)
print(">>> PART 5: SEARCH & AGGREGATION UTILITIES")
print("=" * 55)

telemetry = [45, 90, 12, 90, 77, 90, 33]

print(f"Telemetry Data: {telemetry}")
print(f"Length len(): {len(telemetry)}")
print(f"Minimum min(): {min(telemetry)}")
print(f"Maximum max(): {max(telemetry)}")
print(f"Sum sum(): {sum(telemetry)}")
print(f"Average: {sum(telemetry) / len(telemetry):.2f}")

# Membership testing (in / not in)
has_ninety = 90 in telemetry
has_hundred = 100 in telemetry
print(f"Is 90 in telemetry? {has_ninety}")
print(f"Is 100 in telemetry? {has_hundred}")

# count(item) and index(item)
print(f"Count of 90: {telemetry.count(90)}")
print(f"First index of 90: {telemetry.index(90)}")

# Safe search pattern to avoid ValueError:
target = 100
if target in telemetry:
    print(f"Found {target} at index {telemetry.index(target)}")
else:
    print(f"Target {target} is NOT in telemetry (safely guarded against ValueError)!")


# ==============================================================================
# PART 6: MULTI-DIMENSIONAL LISTS (MATRICES) (Liang 8.1 - 8.3)
# ==============================================================================
print("\n" + "=" * 55)
print(">>> PART 6: MULTI-DIMENSIONAL LISTS (2D MATRICES)")
print("=" * 55)

# A 2D list is a list whose elements are themselves lists:
# 3 rows x 4 columns matrix
grid = [
    [10, 20, 30, 40],   # Row 0
    [50, 60, 70, 80],   # Row 1
    [90, 95, 99, 105]   # Row 2
]

print("2D Matrix Structure:")
for r_idx, row in enumerate(grid):
    print(f"  Row {r_idx}: {row}")

# Accessing elements: matrix[row_index][column_index]
print(f"\nAccessing grid[0][2] (Row 0, Col 2): {grid[0][2]} (Expected: 30)")
print(f"Accessing grid[2][3] (Row 2, Col 3): {grid[2][3]} (Expected: 105)")

# Dimensions:
num_rows = len(grid)
num_cols = len(grid[0])
print(f"Matrix Dimensions: {num_rows} Rows x {num_cols} Columns")


# ==============================================================================
# PART 7: NESTED ITERATIONS & MATRIX OPERATIONS (Liang 8.4 - 8.6)
# ==============================================================================
print("\n" + "=" * 55)
print(">>> PART 7: MATRIX TRAVERSAL, ROW/COL SUMS & DIAGONALS")
print("=" * 55)

matrix_3x3 = [
    [5, 8, 2],
    [3, 9, 6],
    [7, 1, 4]
]

# 7.1 Pretty-printing a matrix:
print("Formatted 3x3 Grid:")
for row in matrix_3x3:
    for val in row:
        print(f"{val:3d}", end=" ")
    print()

# 7.2 Summing each Row:
print("\nRow Sums:")
for r in range(len(matrix_3x3)):
    row_sum = sum(matrix_3x3[r])
    print(f"  Row {r} Sum: {row_sum}")

# 7.3 Summing each Column:
print("\nColumn Sums:")
for c in range(len(matrix_3x3[0])):
    col_sum = 0
    for r in range(len(matrix_3x3)):
        col_sum += matrix_3x3[r][c]
    print(f"  Column {c} Sum: {col_sum}")

# 7.4 Main Diagonal Sum (where row == col):
main_diag_sum = sum(matrix_3x3[i][i] for i in range(len(matrix_3x3)))
# Anti-Diagonal Sum (where col == n - 1 - row):
n = len(matrix_3x3)
anti_diag_sum = sum(matrix_3x3[i][n - 1 - i] for i in range(n))
print(f"\nMain Diagonal Sum: {main_diag_sum}")
print(f"Anti-Diagonal Sum: {anti_diag_sum}")

# 7.5 Dynamically Building a 2D Matrix (e.g., 3 rows x 4 cols of zeros):
# CORRECT METHOD:
correct_grid = [[0 for _ in range(4)] for _ in range(3)]
correct_grid[0][0] = 99
print(f"\nCorrectly generated 2D grid after modifying [0][0]: {correct_grid}")


# ==============================================================================
# PART 8: MEMORY MODEL, REFERENCES & COPYING (Liang 7.7 & 8.3 Pitfalls)
# ==============================================================================
print("\n" + "=" * 55)
print(">>> PART 8: MEMORY MODEL: ALIASING, SHALLOW VS DEEP COPY")
print("=" * 55)

# 8.1 The List Multiplication Trap in 2D Lists:
# DANGEROUS: [ [0] * 3 ] * 3 creates 3 references to the EXACT SAME row list!
buggy_grid = [[0] * 3] * 3
buggy_grid[0][0] = 77  # Modifying row 0 affects ALL rows!
print(f"BUGGY grid using [[0]*3]*3 after modifying [0][0]: {buggy_grid}")
print("Notice how ALL rows changed because they share the identical memory reference!")

# 8.2 Aliasing in 1D Lists
orig = [1, 2, 3]
alias = orig        # Just a reference copy!
alias.append(4)
print(f"\nAliased list appended 4: orig is now {orig} (Aliasing side-effect!)")

# 8.3 Shallow Copy vs Deep Copy
shallow_copy = orig.copy()     # or orig[:]
shallow_copy.append(999)
print(f"Original: {orig}, Shallow copy modified: {shallow_copy}")

# In 2D lists, shallow copy copies outer list, but inner lists are still shared!
nested_orig = [[1, 2], [3, 4]]
nested_shallow = nested_orig.copy()
nested_shallow[0][0] = 888
print(f"Nested Original after shallow copy modification: {nested_orig} (Inner list was shared!)")

# To truly duplicate a multi-dimensional list, use copy.deepcopy():
nested_true = [[10, 20], [30, 40]]
nested_deep = copy.deepcopy(nested_true)
nested_deep[0][0] = 777
print(f"Nested True Original: {nested_true} (Untouched!)")
print(f"Nested Deep Copy: {nested_deep}")

print("\n" + "=" * 76)
print(">>> END OF DAY 7 CONCEPTS DEMO")
print("=" * 76)
