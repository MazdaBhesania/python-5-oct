# 🔐 Day 4 In-Class Activity: Advanced Selections, Math Functions & Characters

- **Course:** Python Programming
- **Session:** Day 4 (Advanced Selections, Math Functions & Characters — Chapters 3 & 4)
- **Pedagogical Scope:** Logical operators (`and`, `or`, `not`), short-circuit evaluation, operator precedence, leap year logic, 2-digit lottery matcher, conditional expressions (ternary operator), Python 3.10 `match-case`, built-in math functions & `math` module (`sqrt`, `ceil`, `floor`, `radians`), and character encoding (`ord()`, `chr()`).
- **Time Allocated:** 45–60 minutes
- **Files in this folder:**
  - [`concepts_demo.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-4/concepts_demo.py) — Master reference guide and runnable demonstrations for all Day 4 concepts.
  - [`bug_hunt_day4.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-4/bug_hunt_day4.py) — 5 debugging mini-challenges on logical operator precedence, short-circuit crashes, ternary syntax, radians vs degrees, and character arithmetic.
  - [`practice_drills.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-4/practice_drills.py) — 3 quick 5-minute warm-up drills (Leap Year boolean checker, ternary conditional with range chaining, character cipher with math checksum).
  - [`starter_cyber_vault.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-4/starter_cyber_vault.py) — Starter template for the main hands-on lab project.
  - [`solution_cyber_vault.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-4/solution_cyber_vault.py) — Complete instructor reference solution.

---

## 🎯 Learning Objectives

1. Apply **logical operators** (`and`, `or`, `not`) to construct robust, multi-condition decision rules.
2. Understand **operator precedence** (`not` > `and` > `or`) and use parentheses to prevent logical precedence bugs.
3. Leverage **short-circuit evaluation** to safely guard against runtime errors such as `ZeroDivisionError`.
4. Implement the textbook **Leap Year Case Study** (Liang 3.11) using compound boolean expressions.
5. Code the **Lottery Number Matcher Case Study** (Liang 3.12) using digit extraction (`// 10`, `% 10`) and logical matching tiers.
6. Write concise, idiomatic Python using **conditional expressions** (ternary operator: `val_if_true if condition else val_if_false`) and range chaining (`18 <= age <= 65`).
7. Understand modern Python structural pattern matching with **`match-case`** statements (Liang 3.14).
8. Utilize Python's standard **`math` module** (`math.sqrt()`, `math.ceil()`, `math.floor()`, `math.radians()`, `math.pi`) and differentiate degrees from radians.
9. Perform character conversions and dynamic cipher manipulation using **`ord()`** (character to ASCII/Unicode code) and **`chr()`** (numeric code to character).

---

## 📋 Activity Roadmap

### Part 1: Interactive Shell Warm-up (10 mins)

Open your terminal or interactive Python shell and experiment with these expressions:

```python
# 1. Logical Operators & Precedence
>>> True and False
False
>>> True or False
True
>>> not True
False
>>> True or False and False     # 'and' evaluates first -> True or (False) = True
True
>>> (True or False) and False   # Parentheses enforce precedence -> False

# 2. Short-Circuit Evaluation
>>> count = 0
>>> count != 0 and (100 / count > 5)  # Evaluates to False safely without division by zero!
False

# 3. Ternary Conditional Expression
>>> score = 85
>>> "Pass" if score >= 70 else "Fail"
'Pass'

# 4. Math & Characters
>>> import math
>>> math.sqrt(25)
5.0
>>> math.ceil(3.2)
4
>>> ord('A')
65
>>> chr(65 + 3)
'D'
```

---

### Part 2: The Debugging Mini-Game (15 mins)

Open [`bug_hunt_day4.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-4/bug_hunt_day4.py). Uncomment each challenge, run the script, examine the error message or faulty output, and fix the bugs:

- **Challenge 1:** Operator Precedence Trap — Fixing missing parentheses in `(is_admin or is_employee) and has_keycard` where `and` binds tighter than `or`.
- **Challenge 2:** Short-Circuit Crash — Guarding a division by zero by reordering conditions so the zero check evaluates first.
- **Challenge 3:** Ternary Operator Syntax — Correcting invalid `if condition value` syntax to Python's `<val_if_true> if <cond> else <val_if_false>`.
- **Challenge 4:** Trigonometry Radians Pitfall — Converting degree inputs with `math.radians()` before calling trigonometric functions like `math.sin()`.
- **Challenge 5:** Character Arithmetic Error — Replacing illegal string-to-int addition `'A' + 4` with `chr(ord('A') + 4)`.

Run to verify:

```bash
python3 Day-4/bug_hunt_day4.py
```

---

### Part 3: Quick Concept Drills (10 mins)

Open [`practice_drills.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-4/practice_drills.py) to complete three rapid coding checkpoints:

1. **Drill 1:** Leap Year determination using `(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)`.
2. **Drill 2:** Working adult verification (`18 <= age <= 65`) and ticket price assignment using a single-line ternary conditional expression.
3. **Drill 3:** Upper-case letter cipher with `ord()` / `chr()` and mathematical checksum with `math.sqrt()`.

Run to verify:

```bash
python3 Day-4/practice_drills.py
```

---

### Part 4: Main Lab Project — CyberVault 2026: Security & Lottery Terminal (25–30 mins)

Open [`starter_cyber_vault.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-4/starter_cyber_vault.py) and implement the guided `# TODO` steps:

1. **Step 1 & 2:** Review security constants and collect visitor parameters (name, clearance level, officer certification, blacklist status, badge year, grid coordinates, payload size, badge initial, and 2-digit lottery guess).
2. **Step 3:** Use **logical operators** (`and`, `or`, `not`) with **short-circuit protection** to evaluate access eligibility.
3. **Step 4:** Implement the **Leap Year calculation** on `badge_year` to award bonus operating hours (366 vs 365).
4. **Step 5:** Write **ternary conditional expressions** to determine `status_label` (`"ACCESS GRANTED"` vs `"ACCESS DENIED"`) and `gate_lane`.
5. **Step 6:** Use Python's **`math` module** to compute Euclidean distance to the central server grid and `math.ceil()` to compute required communication packets.
6. **Step 7:** Generate a 3-character security cipher key using **`ord()`** and **`chr()`** character offset shifts (+1, +3, +5).
7. **Step 8:** Implement the **Liang 3.12 Two-Digit Lottery Game** using integer floor division (`//`) and remainder (`%`) to reward exact matches ($10,000), reverse matches ($3,000), and partial matches ($1,000).
8. **Step 9:** Execute system security protocol classification (`match-case` / fallback).
9. **Step 10:** Output a formatted terminal report pass.

Run your script:

```bash
python3 Day-4/starter_cyber_vault.py
```

---

## 🧪 Sample Execution

```text
====================================================================
     🔐 CYBERVAULT 2026: QUANTUM ACCESS & LOTTERY TERMINAL 🔐
====================================================================
Enter Operative Codename: Agent-007
Enter Clearance Level (1 to 5): 4
Are you a certified security officer? (yes/no): yes
Is this badge flagged on the blacklist? (yes/no): no
Enter Badge Issue Year (e.g. 2024, 2025): 2024
Enter Terminal Grid X coordinate (e.g. 12.0): 12.0
Enter Terminal Grid Y coordinate (e.g. 16.0): 16.0
Enter transmission payload size in bytes (e.g. 250): 250
Enter single badge initial letter (A-W): B
Enter 2-digit Lucky Vault guess (10 to 99): 48

====================================================================
             CYBERVAULT 2026: TERMINAL CLEARANCE REPORT
====================================================================
Operative Codename:   Agent-007
Clearance Level:      Level 4 (Priority Quantum Lane)
Badge Security State: CLEAN / VERIFIED
Access Decision:      ACCESS GRANTED
Badge Year 2024:     Leap Year Bonus (366 hrs)
--------------------------------------------------------------------
Terminal Grid:        (12.0, 16.0)
Server Grid Distance: 20.00 meters
Payload Size:         250 bytes -> 4 packet(s) required
Badge Initial:        'B' -> Cipher Key Token: [CEG]
System Mode Protocol: Standard surveillance and biometric checks active.
--------------------------------------------------------------------
Vault Lottery Draw:   Target [84] | Your Guess [48]
Lottery Result:       Silver Tier! All Digits Matched!
Cash Payout:          $3,000.00
====================================================================
```

---

## 💡 Instructor & Study Notes

- **Logical Precedence Memory Hook:** `not` acts like a negative sign (highest), `and` acts like multiplication, and `or` acts like addition. When mixing `and` and `or`, always use parentheses for clarity.
- **Short-Circuit Performance & Safety:** In `condA and condB`, if `condA` is `False`, Python never evaluates `condB`. In `condA or condB`, if `condA` is `True`, Python never evaluates `condB`.
- **Character Math:** Computers store characters as integers under ASCII/Unicode. `ord('A')` is 65, and `chr(65)` is `'A'`. Adding numbers changes the code point, enabling simple Caesar ciphers.
