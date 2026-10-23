# 🚀 Day 7 In-Class Activity: Mastering 1D Lists & Multi-Dimensional Lists

- **Course:** Python Programming
- **Session:** Day 7 (Liang Chapters 7 & 8: 1D Lists & Multi-Dimensional Lists)
- **Pedagogical Scope:** List creation, indexing (positive & negative), slicing (`[start:stop:step]`), sequence traversal (`for item in list`, `range(len())`, `enumerate()`), list comprehensions, in-place mutating methods (`append`, `extend`, `insert`, `pop`, `remove`, `sort`, `reverse`), search & aggregations (`in`, `index`, `count`, `min`, `max`, `sum`, `len`), 2D matrices (list of lists, rows & columns), nested loops for grid traversal, row sums, column sums, matrix transpositions, diagonal checks, and Python's memory model (aliasing, shallow copy vs deep copy).
- **Textbook Alignment:** Liang, *Introduction to Programming Using Python*, Chapter 7 (1D Lists) and Chapter 8 (Multi-Dimensional Lists).
- **Time Allocated:** 45–60 minutes
- **Files in this folder:**
  - [`concepts_demo.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-7/concepts_demo.py) — Complete concept demo and reference implementation across all 8 core list and matrix topics.
  - [`bug_hunt_day7.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-7/bug_hunt_day7.py) — 5 debugging mini-challenges on 2D shallow multiplication, off-by-one indexing, in-loop mutation skipping, method return value traps, and row-col coordinate inversions.
  - [`practice_drills.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-7/practice_drills.py) — 3 quick 5-minute warm-up drills (statistics & outlier dropping, list comprehensions with string sequences, 2D matrix transposition).
  - [`matrix_helpers.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-7/matrix_helpers.py) — Modular helper library containing `create_grid()`, `print_matrix()`, `calculate_row_totals()`, `calculate_col_totals()`, `transpose_matrix()`, and `clone_matrix()`.
  - [`starter_matrix_ops.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-7/starter_matrix_ops.py) — Guided student starter template for the main hands-on lab.
  - [`solution_matrix_ops.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-7/solution_matrix_ops.py) — Complete instructor reference solution.

---

## 🎯 Learning Objectives

1. **Construct and Initialize 1D Lists** using literals `[]`, constructor `list()`, `range()`, repetition `*`, and concatenation `+` (Liang 7.1).
2. **Access and Slice Elements** using 0-based positive indexing, negative indexing from the end, and the extended slicing syntax `list[start:stop:step]` (Liang 7.2).
3. **Traverse Sequences & Leverage List Comprehensions** to write expressive, pythonic filtering and transformation expressions (Liang 7.3 & 7.11).
4. **Master List Mutability & In-Place Methods** (`append`, `extend`, `insert`, `pop`, `remove`, `sort`, `reverse`), contrasting in-place modifications that return `None` with non-destructive built-ins (`sorted`, `reversed`) (Liang 7.5 – 7.8).
5. **Represent 2D Grids and Tables** as lists of lists, indexing them with `matrix[row][col]` syntax (Liang 8.1 – 8.3).
6. **Navigate Multi-Dimensional Data** using nested loops to compute row totals, column totals, matrix transpositions, and diagonal vectors (Liang 8.4 – 8.6).
7. **Avoid Memory Aliasing Pitfalls**: Understand why `[[0]*N]*M` creates shallow reference duplicates, and correctly isolate multi-dimensional matrices using list comprehensions or `copy.deepcopy()` (Liang 7.7 & 8.3).

---

## 📋 Activity Roadmap

### Part 1: Interactive Shell Warm-up (10 mins)

Open your terminal or interactive Python shell and test these fundamental list operations:

```python
# 1. Negative indexing & slicing
>>> values = [10, 20, 30, 40, 50]
>>> values[-1]
50
>>> values[1:4]
[20, 30, 40]
>>> values[::-1]
[50, 40, 30, 20, 10]

# 2. List comprehension filtering
>>> nums = [5, 12, 18, 7, 24, 3]
>>> evens = [n for n in nums if n % 2 == 0]
>>> evens
[12, 18, 24]

# 3. 2D Matrix indexing [row][col]
>>> matrix = [
...     [1, 2, 3],
...     [4, 5, 6]
... ]
>>> matrix[0][1]   # Row 0, Col 1
2
>>> matrix[1][2]   # Row 1, Col 2
6

# 4. The 2D Multiplication Trap
>>> buggy = [[0] * 3] * 3
>>> buggy[0][0] = 99
>>> buggy
[[99, 0, 0], [99, 0, 0], [99, 0, 0]]  # All rows affected!
```

---

### Part 2: The Bug Hunt (15 mins)

Open [`bug_hunt_day7.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-7/bug_hunt_day7.py). Uncomment each challenge, run the script, examine the error or faulty output, and fix the bugs:

- **Challenge 1:** *2D Matrix Row Reference Duplication* — Replacing `[[0]*3]*3` with list comprehension so mutating one cell does not alter every row.
- **Challenge 2:** *Off-by-One IndexError* — Correcting `range(1, len(lst) + 1)` to 0-based traversal `range(len(lst))`.
- **Challenge 3:** *Mutating List During Iteration* — Preventing skipped elements when removing items during loop traversal.
- **Challenge 4:** *In-Place Method Return Value Trap* — Fixing `sorted_lst = lst.sort()` returning `None`.
- **Challenge 5:** *Matrix Row vs Column Coordinate Inversion* — Accessing `matrix[r][col]` instead of `matrix[col][r]` during column accumulation.

Run to verify:

```bash
python3 Day-7/bug_hunt_day7.py
```

---

### Part 3: Quick Concept Drills (10 mins)

Open [`practice_drills.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-7/practice_drills.py) to complete three rapid coding checkpoints:

1. **Drill 1 (Statistics & Outlier Dropping):** Calculate score count, min, max, total, and average; drop the lowest outlier and recompute average.
2. **Drill 2 (List Comprehensions):** Filter strings by length, extract character counts, and apply string transformations.
3. **Drill 3 (Matrix Transpose):** Transpose a 3x2 grid into a 2x3 grid and calculate original column sums.

Run to verify:

```bash
python3 Day-7/practice_drills.py
```

---

### Part 4: Main Lab — MatrixOps Analytics Hub (20–25 mins)

Open [`starter_matrix_ops.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-7/starter_matrix_ops.py) and implement the regional turbine energy grid monitor:

- **Step 1:** Render formatted grid using [`matrix_helpers.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-7/matrix_helpers.py).
- **Step 2:** Flatten the 2D grid into a 1D sequence and compute global statistics (`min`, `max`, `sum`, `avg`, and filter high-yield turbines).
- **Step 3:** Calculate sector production totals across rows and identify the top producing sector.
- **Step 4:** Calculate turbine model fleet totals across columns.
- **Step 5:** Extract and compare primary and secondary diagonal calibration vectors.
- **Step 6:** Detect and log overload alerts (turbines >= 85.0 MW) with coordinate positions.
- **Step 7:** Run an isolated deep-copy simulation (+15% boost) without mutating the original operational telemetry.

Run to verify:

```bash
python3 Day-7/starter_matrix_ops.py
```

Compare with reference solution:

```bash
python3 Day-7/solution_matrix_ops.py
```

---

## 💡 Key Summary & Best Practices

| Operation | Syntax / Example | Notes |
| :--- | :--- | :--- |
| **Indexing** | `lst[0]`, `lst[-1]` | 0-based from front, negative from end |
| **Slicing** | `lst[start:stop:step]` | `stop` index is exclusive; `[::-1]` reverses |
| **Append vs Extend** | `lst.append(x)` vs `lst.extend(iterable)` | `append` adds 1 element; `extend` unpacks iterable |
| **In-place Sort** | `lst.sort()` vs `sorted(lst)` | `sort()` returns `None`; `sorted()` returns new list |
| **2D Element Access** | `matrix[row][col]` | First bracket is row (outer), second is col (inner) |
| **Independent 2D Init** | `[[0 for _ in range(cols)] for _ in range(rows)]` | Never use `[[0] * cols] * rows`! |
| **Deep Matrix Copy** | `copy.deepcopy(matrix)` | Required for multi-dimensional lists to avoid alias mutation |
