# 🕹️ Day 5 In-Class Activity: Repetition Structures & Loops

- **Course:** Python Programming
- **Session:** Day 5 (Loops & Repetition Structures — Chapter 5)
- **Pedagogical Scope:** Counter-controlled `while` loops, infinite loop prevention, sentinel-controlled loops, `for` loops with `range()`, nested loops (matrices/grids), loop control keywords (`break`, `continue`), and accumulator patterns (`sum`, `count`, `average`, `min`, `max`).
- **Time Allocated:** 45–60 minutes
- **Files in this folder:**
  - [`concepts_demo.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-5/concepts_demo.py) — Master reference guide and runnable demonstrations for all Day 5 loop concepts.
  - [`bug_hunt_day5.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-5/bug_hunt_day5.py) — 5 debugging mini-challenges on off-by-one errors, infinite loops, accumulator reset traps, premature `break` exits, and skipped updates with `continue`.
  - [`practice_drills.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-5/practice_drills.py) — 3 quick 5-minute warm-up drills (multiplication table generator, sentinel-controlled score accumulator, divisor/prime finder).
  - [`starter_arcade_quest.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-5/starter_arcade_quest.py) — Starter template for the main hands-on lab project.
  - [`solution_arcade_quest.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-5/solution_arcade_quest.py) — Complete instructor reference solution.

---

## 🎯 Learning Objectives

1. Construct **counter-controlled `while` loops** with proper initialization, boolean condition, and variable updates.
2. Recognize and prevent **infinite loops** by guaranteeing that the loop continuation condition eventually becomes `False`.
3. Implement **sentinel-controlled loops** (Liang 5.5) to process arbitrary-length user input streams until a designated termination marker (e.g. `-1` or `0`) is encountered.
4. Utilize the **`for` loop** and master all three forms of the **`range()` function**:
   - `range(stop)`
   - `range(start, stop)`
   - `range(start, stop, step)` (including reverse/countdown ranges)
5. Design **nested loops** (Liang 5.7) to generate two-dimensional tables, coordinate grids, and multiplication matrices.
6. Control execution flow with **`break`** (immediate loop termination) and **`continue`** (skipping the remainder of the current iteration).
7. Apply fundamental **accumulator design patterns**: running summation, item counting, computing averages (with zero-division guards), and tracking minimum/maximum values.
8. Implement the textbook **Guessing Numbers Case Study** (Liang 5.3).

---

## 📋 Activity Roadmap

### Part 1: Interactive Shell Warm-up (10 mins)

Open your terminal or IDLE shell and test these loop and range expressions:

```python
# 1. Inspecting range() outputs
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> list(range(2, 8))
[2, 3, 4, 5, 6, 7]
>>> list(range(10, 0, -2))
[10, 8, 6, 4, 2]

# 2. Simple counting loop
>>> for i in range(1, 4):
...     print(f"Count: {i}")
Count: 1
Count: 2
Count: 3

# 3. Summing with an accumulator
>>> total = 0
>>> for x in [10, 20, 30]:
...     total += x
>>> total
60
```

---

### Part 2: The Debugging Mini-Game (15 mins)

Open [`bug_hunt_day5.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-5/bug_hunt_day5.py). Uncomment each challenge, run the script, examine the error message or faulty output, and fix the bugs:

- **Challenge 1:** Off-by-One Error — Adjusting `range(1, 10)` to `range(1, 11)` so the upper bound 10 is included.
- **Challenge 2:** Infinite `while` Loop — Adding the missing counter decrement statement (`countdown -= 1`).
- **Challenge 3:** Accumulator Scope Trap — Moving `total = 0.0` outside and before the loop so running totals are preserved across iterations.
- **Challenge 4:** Premature Loop Exit — Removing an erroneous `else: break` inside a search loop so the search doesn't terminate on the first element.
- **Challenge 5:** Skipped Update Trap — Ensuring `num += 1` executes before a `continue` call in a `while` loop so the counter does not freeze.

Run to verify:

```bash
python3 Day-5/bug_hunt_day5.py
```

---

### Part 3: Quick Concept Drills (10 mins)

Open [`practice_drills.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-5/practice_drills.py) to complete three rapid coding checkpoints:

1. **Drill 1:** Multiplication table generator from 1 to 12 for an entered integer using a `for` loop with `range(1, 13)`.
2. **Drill 2:** Sentinel-controlled score accumulator accepting floating-point values until `-1` is entered, computing total, count, and average.
3. **Drill 3:** Divisor finder checking all numbers from 1 to N, reporting divisors and flagging prime numbers.

Run to verify:

```bash
python3 Day-5/practice_drills.py
```

---

### Part 4: Main Lab Project — RetroArcade: NumberQuest & High-Score Ledger (25–30 mins)

Open [`starter_arcade_quest.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-5/starter_arcade_quest.py) and implement the guided `# TODO` sections:

1. **Step 1:** Player tag registration and greeting.
2. **Step 2 (Mission 1):** Code the **NumberQuest Secret Vault Cracker** (Liang 5.3):
   - Hidden number between 1 and 100 (`random.randint(1, 100)`).
   - Maximum 7 attempts using a `while` loop.
   - Out-of-bounds validation with `continue`.
   - "Too high!" and "Too low!" feedback.
   - Immediate exit with `break` when guessed correctly.
   - Bonus points awarded for remaining attempts.
3. **Step 3 (Mission 2):** Code the **Sentinel-Controlled Score Ledger** (Liang 5.5):
   - Repeatedly prompt for past arcade round scores until the player enters `-1`.
   - Skip invalid negative entries with `continue`.
   - Track accumulators: running sum, count, minimum score, and maximum score.
4. **Step 4:** Calculate average round score with zero-division safeguard.
5. **Step 5 (Mission 3):** Code the **XP Multiplier Matrix** using nested `for` loops (Liang 5.7) to render a formatted 3x4 difficulty grid.
6. **Step 6:** Display the final formatted Player Performance Summary.

Run your script:

```bash
python3 Day-5/starter_arcade_quest.py
```

---

## 🧪 Sample Execution

```text
====================================================================
       🕹️ WELCOME TO RETROARCADE: NUMBERQUEST & LEDGER 🕹️
====================================================================
Enter your Arcade Tag / Nickname: PixelHero

Welcome, Player PixelHero! Preparing your game terminal...

--------------------------------------------------------------------
>>> MISSION 1: CRACK THE SECRET NUMBER VAULT (1 to 100)
    You have a maximum of 7 attempts. Choose wisely!
--------------------------------------------------------------------
Attempt 1/7 — Enter guess (1-100): 50
  Too low! ⬆️ Try higher.
Attempt 2/7 — Enter guess (1-100): 75
  Too high! ⬇️ Try lower.
Attempt 3/7 — Enter guess (1-100): 62
  Too high! ⬇️ Try lower.
Attempt 4/7 — Enter guess (1-100): 56
  🎉 BINGO! You cracked the vault in 4 attempt(s)!

--------------------------------------------------------------------
>>> MISSION 2: ARCADE ROUNDS LEDGER (Sentinel = -1)
    Enter your previous game scores. Type -1 when finished.
--------------------------------------------------------------------
  Enter round score (-1 to stop): 120
  Enter round score (-1 to stop): 350
  Enter round score (-1 to stop): 210
  Enter round score (-1 to stop): -1

--------------------------------------------------------------------
>>> MISSION 3: XP MULTIPLIER MATRIX (Nested Loops)
--------------------------------------------------------------------
Tier \ Stage   |  Stage 1  |  Stage 2  |  Stage 3  |  Stage 4
----------------------------------------------------------
Tier 1 (Brz)  |      25  |      50  |      75  |     100  |
Tier 2 (Sil)  |      50  |     100  |     150  |     200  |
Tier 3 (Gld)  |      75  |     150  |     225  |     300  |

====================================================================
             RETROARCADE: PLAYER PERFORMANCE SUMMARY
====================================================================
Player Tag:           PixelHero
Vault Quest Status:   CRACKED! 🎉
Attempts Used:        4 / 7
Secret Target:        56
Vault Quest Points:   600 pts
--------------------------------------------------------------------
Ledger Rounds Logged: 3 round(s)
Total Ledger Score:   680.0 pts
Average Round Score:  226.67 pts
Highest Round Score:  350.0 pts
Lowest Round Score:   120.0 pts
--------------------------------------------------------------------
GRAND TOTAL POINTS:   1,280.0 pts
====================================================================
```

---

## 💡 Instructor & Study Notes

- **`while` vs `for` Rule of Thumb:** Use a `for` loop when you know in advance how many times the loop will execute (definite iteration, e.g. ranges, lists, fixed counts). Use a `while` loop when the number of repetitions depends on a condition or user action (indefinite iteration, e.g. game loops, sentinel inputs, convergence).
- **The Three Essentials of a Loop:**
  1. **Initialization:** Set up variables before the loop.
  2. **Continuation Condition:** Tested before each iteration.
  3. **Update:** Modify variables in the body so the condition eventually changes to `False`.
- **Sentinel Design Pattern:** Always choose a sentinel value that cannot be mistaken for legitimate data (e.g. `-1` when scores are positive numbers, or `"quit"` when strings are expected).
