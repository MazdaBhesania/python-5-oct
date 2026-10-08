# 🚀 Day 2 In-Class Activity: Elementary Programming & The Smart Cashier

- **Course:** Python Programming
- **Session:** Day 2 (Variables, Expressions, Operators & Input)
- **Time Allocated:** 45–60 minutes
- **Files in this folder:**
  - [`starter_change_maker.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-2/starter_change_maker.py) — Starter template for students
  - [`solution_change_maker.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-2/solution_change_maker.py) — Completed reference solution
  - [`bug_hunt_day2.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-2/bug_hunt_day2.py) — Debugging mini-challenges
  - [`concepts_demo.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-2/concepts_demo.py) — Quick concept reference examples

---

## 🎯 Learning Objectives

1. Read user input with `input()` and convert string inputs using `int()` and `float()`.
2. Master Python variable naming rules (`snake_case`, letters, numbers, underscores).
3. Use simultaneous assignments (`x, y = 10, 20`) and variable swapping (`x, y = y, x`).
4. Apply named constants using uppercase conventions (e.g., `CENTS_PER_DOLLAR = 100`).
5. Choose the right arithmetic operator: float division (`/`), floor division (`//`), modulo remainder (`%`), and exponentiation (`**`).
6. Apply operator precedence (PEMDAS) with parentheses when evaluating formulas.
7. Use augmented assignment operators (`+=`, `-=`, `*=`, `//=`, `%=`).
8. Format numeric output cleanly with `round()` and f-strings.

---

## 📋 Activity Roadmap

### Part 1: Interactive Shell Warm-up (10 mins)

Open your terminal or IDLE shell and test these expressions:

```python
>>> type("42")                     # <class 'str'>
>>> type(42)                       # <class 'int'>
>>> type(42.0)                     # <class 'float'>
>>> 7 / 2                          # 3.5 (float division)
>>> 7 // 2                         # 3   (floor / integer division)
>>> 7 % 2                          # 1   (remainder)
>>> 2 ** 3                         # 8   (exponentiation)
>>> x, y = 5, 9
>>> x, y = y, x                    # Pythonic swap!
>>> print(x, y)                    # 9 5
```

### Part 2: The Debugging Mini-Game (15 mins)

Open [`bug_hunt_day2.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-2/bug_hunt_day2.py). Uncomment each challenge, run the script, examine the error message or output, and fix the bugs:
- **Challenge 1:** Fixing `input()` string duplication (`"50" * 2`).
- **Challenge 2:** Correcting invalid variable identifiers (`1st_score`, `runner-up`).
- **Challenge 3:** Using floor division (`//`) and modulo (`%`) instead of float division (`/`).
- **Challenge 4:** Adding parentheses for PEMDAS order of operations in averages.
- **Challenge 5:** Aligning simultaneous assignment variable and value counts.

Run the file to verify:

```bash
python3 bug_hunt_day2.py
```

### Part 3: The Smart Cashier Change-Maker (25 mins)

Open [`starter_change_maker.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-2/starter_change_maker.py) and complete the guided `# TODO` items:

1. Define coin constants (`CENTS_PER_DOLLAR`, `CENTS_PER_QUARTER`, etc.).
2. Prompt user for item name, bill amount, and cash received, casting amounts to `float()`.
3. Compute total change and convert to total cents using `int(round(change_due * 100))`.
4. Calculate the breakdown into dollars, quarters, dimes, nickels, and pennies using `//` and `%=`.
5. Display a formatted receipt.

Run the script to verify your calculations:

```bash
python3 starter_change_maker.py
```
