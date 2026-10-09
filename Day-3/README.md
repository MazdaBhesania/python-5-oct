# 🎢 Day 3 In-Class Activity: Selections (Conditionals) & The Smart Kiosk

- **Course:** Python Programming
- **Session:** Day 3 (Selection Statements — Chapter 4)
- **Pedagogical Scope:** Relational operators, one-way `if`, two-way `if-else`, multi-way `if-elif-else`, nested `if`, and `random.randint()`.
  *(Note: Logical operators `and`, `or`, and `not` are **left to teach in the next session**; all activities today are solved using clean branching and nested selections).*
- **Time Allocated:** 45–60 minutes
- **Files in this folder:**
  - [`concepts_demo.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-3/concepts_demo.py) — Runnable master reference guide for all Day 3 selection concepts.
  - [`bug_hunt_day3.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-3/bug_hunt_day3.py) — 5 debugging mini-challenges on common selection mistakes.
  - [`practice_drills.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-3/practice_drills.py) — 3 quick 5-minute warm-up drills (Even/Odd, BMI, Nested Grade Honors).
  - [`starter_ticket_kiosk.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-3/starter_ticket_kiosk.py) — Starter template for the main hands-on project.
  - [`solution_ticket_kiosk.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-3/solution_ticket_kiosk.py) — Complete reference solution.

---

## 🎯 Learning Objectives

1. Evaluate **Boolean expressions** using relational operators: `==`, `!=`, `<`, `<=`, `>`, `>=`.
2. Differentiate between assignment (`=`) and equality testing (`==`).
3. Implement **one-way `if` statements** for conditional alerts, notices, and optional actions.
4. Implement **two-way `if-else` statements** for mutually exclusive binary decisions (e.g., even vs odd, pass vs fail, safety clearance).
5. Structure **multi-way `if-elif-else` cascades** for multi-bracket classification (e.g., age tiers, letter grades) and understand why branch order matters.
6. Design **nested `if` statements** to handle multi-level decisions hierarchically **without requiring logical operators (`and`, `or`, `not`)**.
7. Generate and utilize pseudorandom numbers using Python's `random.randint()`.

---

## 📋 Activity Roadmap

### Part 1: Interactive Shell Warm-up (10 mins)

Open your terminal or IDLE shell and test these Boolean and selection expressions:

```python
>>> 10 > 5                          # True
>>> 10 == 10.0                      # True (value comparison)
>>> "apple" == "Apple"              # False (case-sensitive)
>>> 14 % 2 == 0                     # True (even number test)
>>> 15 % 2 == 0                     # False (odd number test)
>>> import random
>>> random.randint(1, 6)            # Generates a random integer from 1 to 6
```

---

### Part 2: The Debugging Mini-Game (15 mins)

Open [`bug_hunt_day3.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-3/bug_hunt_day3.py). Uncomment each challenge, run the script, examine the error message or faulty output, and fix the bugs:

- **Challenge 1:** Fixing assignment `=` used inside an `if` condition instead of equality comparison `==`.
- **Challenge 2:** Correcting missing colons (`:`) at the ends of `if` and `else` statements.
- **Challenge 3:** Indentation error causing code intended for the `if` block to run unconditionally for every user.
- **Challenge 4:** Branch ordering trap in `if-elif-else` where an overly broad condition intercepts values prematurely.
- **Challenge 5:** Aligning nested `if-else` indentation so the `else` pairs with the intended decision level.

Run to verify:

```bash
python3 Day-3/bug_hunt_day3.py
```

---

### Part 3: Quick Concept Drills (Optional / Warm-up — 10 mins)

Open [`practice_drills.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-3/practice_drills.py) to practice three rapid coding checkpoints:
1. **Drill 1:** Even or Odd integer tester using `% 2 == 0`.
2. **Drill 2:** BMI health classification using cascading `elif` branches (no compound logic needed).
3. **Drill 3:** Exam grade with a nested `if` checking for Dean's List distinction.

Run to verify:

```bash
python3 Day-3/practice_drills.py
```

---

### Part 4: Main Lab Project — Adventure Island Smart Kiosk (25–30 mins)

Open [`starter_ticket_kiosk.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-3/starter_ticket_kiosk.py) and complete the guided `# TODO` items:

1. **Step 1 & 2:** Review defined pricing constants and prompt for guest inputs (`name`, `age`, `height`, `is_matinee`).
2. **Step 3:** Use a **multi-way `if-elif-else`** to determine ticket category (`Child Pass`, `Youth / Student Pass`, `General Adult Pass`, `Senior Gold Pass`) and base pricing.
3. **Step 4:** Use a **nested `if` statement** (without `and`) to apply matinee early-bird discounts ($10 off for adults, $5 off for youth/students).
4. **Step 5:** Use a **two-way `if-else`** statement to evaluate height against the minimum 48-inch requirement for the Cyclone Roller Coaster.
5. **Step 6:** Use a **one-way `if`** to display a mandatory adult accompaniment notice for guests under 12.
6. **Step 7:** Generate a random lucky door number (`1` to `4`) using `random.randint()` and determine the door prize.
7. **Step 8:** Display a clean, formatted receipt / visitor pass.

Run your script:

```bash
python3 Day-3/starter_ticket_kiosk.py
```

---

## 🧪 Sample Execution

### Sample Run 1: Adult Visiting in the Afternoon

```text
============================================================
     🎡 WELCOME TO ADVENTURE ISLAND SMART KIOSK 🎢
============================================================
Enter visitor name: Maya Lin
Enter age: 24
Enter height in inches: 54.5
Are you visiting before 2:00 PM? (yes/no): yes

============================================================
             ADVENTURE ISLAND VISITOR PASS
============================================================
Guest Name:           Maya Lin
Age:                  24 years old
Height:               54.5 inches
Ticket Category:      General Adult Pass
Base Admission:       $ 50.00
Early-Bird Discount: -$ 10.00
Final Total Due:      $ 40.00
------------------------------------------------------------
Cyclone Coaster:      APPROVED: Eligible to ride the Cyclone Coaster!
Lucky Spin (Rolled 1): FREE Popcorn Coupon!
============================================================
       Enjoy your day of thrills and excitement! 🎢
============================================================
```

### Sample Run 2: Child Visitor (Safety Notice Triggered)

```text
============================================================
     🎡 WELCOME TO ADVENTURE ISLAND SMART KIOSK 🎢
============================================================
Enter visitor name: Tommy Smith
Enter age: 8
Enter height in inches: 42.0
Are you visiting before 2:00 PM? (yes/no): no

============================================================
             ADVENTURE ISLAND VISITOR PASS
============================================================
Guest Name:           Tommy Smith
Age:                  8 years old
Height:               42.0 inches
Ticket Category:      Child Pass
Base Admission:       $ 20.00
Early-Bird Discount: -$  0.00
Final Total Due:      $ 20.00
------------------------------------------------------------
Cyclone Coaster:      RESTRICTED: Under 48 inches. Eligible for Kiddie Land rides only.
Safety Alert:         NOTICE: Visitors under 12 must be accompanied by an adult.
Lucky Spin (Rolled 3): FREE Arcade Token Pack!
============================================================
       Enjoy your day of thrills and excitement! 🎢
============================================================
```
