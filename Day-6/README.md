# 🚀 Day 6 In-Class Activity: Mastering Functions & Modular Programming

- **Course:** Python Programming
- **Session:** Day 6 (Chapter 6: Functions — Sessions 13, 14 & 15)
- **Pedagogical Scope:** Function definitions (`def`), headers, parameters vs arguments, execution flow, void vs value-returning functions (`None` return), positional vs keyword arguments, default parameters, pass-by-object-reference (mutable vs immutable), multiple return values (tuple packing and sequence unpacking), variable scope (local vs global, variable lifetime, name shadowing, the `global` keyword), and modular code architecture (creating custom `.py` libraries, imports, and `if __name__ == '__main__':`).
- **Textbook Alignment:** Liang, *Introduction to Programming Using Python*, Chapter 6 (Sections 6.1 – 6.10).
- **Time Allocated:** 45–60 minutes
- **Files in this folder:**
  - [`concepts_demo.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-6/concepts_demo.py) — Comprehensive reference guide and runnable demonstrations covering all Session 13, 14, and 15 concepts.
  - [`bug_hunt_day6.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-6/bug_hunt_day6.py) — 5 debugging mini-challenges on print vs return traps, positional/keyword argument ordering, non-default parameter placement, `UnboundLocalError` scope collisions, and tuple unpacking mismatches.
  - [`practice_drills.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-6/practice_drills.py) — 3 quick 5-minute warm-up drills (hypotenuse & prime checkers, flexible flight badge builder, telemetry batch analyzer).
  - [`telemetry_helpers.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-6/telemetry_helpers.py) — Reusable helper module demonstrating modular programming, default parameters, and the `__name__ == '__main__':` unit testing guard.
  - [`starter_astro_voyager.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-6/starter_astro_voyager.py) — Guided starter template for the main hands-on lab project.
  - [`solution_astro_voyager.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-6/solution_astro_voyager.py) — Complete instructor reference solution.

---

## 🎯 Learning Objectives

1. **Define and invoke functions** using the `def` keyword, proper parameter lists, docstrings, and understand execution jumps across the call stack (Liang 6.1 – 6.3).
2. Distinguish between **value-returning functions** and **void functions**, recognizing that Python functions without an explicit `return` evaluate to `None` (Liang 6.4).
3. Apply **positional and keyword arguments**, adhering strictly to the Python rule that all positional arguments must precede keyword arguments (Liang 6.5).
4. Understand Python's **Object Reference Model** (pass-by-object-reference): contrast immutable data types (integers, floats, strings, tuples) with mutable data types (lists) modified in-place (Liang 6.6).
5. Specify **default argument values** for optional parameters and adhere to the structural constraint that default parameters must trail non-default parameters (Liang 6.9).
6. Return **multiple values** from a single function using tuple packing and unpack them cleanly into multiple recipient variables (Liang 6.10).
7. Master **variable scope**: differentiate local variables (temporary lifetime inside functions) from global variables, analyze variable shadowing, and recognize when and why to minimize the `global` keyword (Liang 6.8).
8. Architect **modular Python software**: construct separate `.py` module files, import functions using `from module import func`, and isolate test code using `if __name__ == '__main__':` (Liang 6.7).

---

## 📋 Activity Roadmap

### Part 1: Interactive Shell Warm-up (10 mins)

Open your terminal or interactive Python shell and test these function mechanics:

```python
# 1. Void function returning None
>>> def greet(name):
...     print(f"Hello, {name}!")
>>> res = greet("Aria")
Hello, Aria!
>>> print(res)
None

# 2. Positional vs Keyword Arguments
>>> def describe_ship(name, warp=1, shields=True):
...     return f"{name} (Warp {warp}, Shields: {shields})"
>>> describe_ship("Defiant", shields=False)
'Defiant (Warp 1, Shields: False)'

# 3. Multiple Return Values (Tuple Unpacking)
>>> def get_dimensions():
...     return 1920, 1080
>>> width, height = get_dimensions()
>>> width
1920
>>> height
1080

# 4. Modifying Mutable Lists by Reference
>>> def add_crate(manifest):
...     manifest.append("Rations")
>>> cargo = ["Tools"]
>>> add_crate(cargo)
>>> cargo
['Tools', 'Rations']
```

---

### Part 2: The Debugging Mini-Game (15 mins)

Open [`bug_hunt_day6.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-6/bug_hunt_day6.py). Uncomment each challenge, run the script, examine the error message or faulty output, and fix the bugs:

- **Challenge 1:** *The "Print Instead of Return" Trap* — Replacing `print()` with `return` so arithmetic does not fail with `TypeError: unsupported operand type(s) for +: 'float' and 'NoneType'`.
- **Challenge 2:** *Argument Ordering* — Resolving `SyntaxError: positional argument follows keyword argument` by passing positional parameters first.
- **Challenge 3:** *Default Parameter Placement* — Fixing `SyntaxError: non-default argument follows default argument` by placing required parameters before default ones.
- **Challenge 4:** *UnboundLocalError / Scope Collision* — Resolving scope conflict when reassigning a variable within a function via `global` declaration or return values.
- **Challenge 5:** *Tuple Unpacking Count Mismatch* — Correcting `ValueError: too many values to unpack` by aligning the recipient variables with the function's returned tuple size.

Run to verify:

```bash
python3 Day-6/bug_hunt_day6.py
```

---

### Part 3: Quick Concept Drills (10 mins)

Open [`practice_drills.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-6/practice_drills.py) to complete three rapid coding checkpoints:

1. **Drill 1:** Implement pure functions `calculate_hypotenuse(a, b)` and prime-number tester `is_prime(n)` with early returns.
2. **Drill 2:** Construct `generate_flight_badge()` featuring default arguments and call it using positional, keyword, and mixed calling styles.
3. **Drill 3:** Write `analyze_telemetry_batch()` returning minimum, maximum, average, and spread as a 4-value tuple and unpack them.

Run to verify:

```bash
python3 Day-6/practice_drills.py
```

---

### Part 4: Main Lab Project — AstroVoyager: Deep-Space Fleet Dispatch & Telemetry Hub (25–30 mins)

Open [`starter_astro_voyager.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-6/starter_astro_voyager.py) and implement the guided `# TODO` sections:

1. **TODO 1 (Modular Imports):** Import `calculate_fuel_burn`, `compute_comm_delay`, `assess_hull_integrity`, and `format_mission_header` from [`telemetry_helpers.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-6/telemetry_helpers.py).
2. **TODO 2 (Warp Travel Calculator):** Define `calculate_warp_travel_time(distance_ly, warp_factor=1.0)` using the relativistic formula `distance / (warp ** (10/3))`.
3. **TODO 3 (Life Support Provisions):** Define `provision_crew_supplies(crew_size, duration_days, safety_margin=0.20)` calculating food, water, and oxygen packs with safety buffers.
4. **TODO 4 (Mission Risk Assessment):** Define `evaluate_mission_risk(distance_ly, crew_count, anomaly_index)` returning a 3-element tuple `(risk_score, category, is_approved)`.
5. **TODO 5 (Pass-by-Reference Cargo Loading):** Define `load_cargo_manifest(manifest_list, cargo_item)` demonstrating in-place list mutation.
6. **TODO 6 (Global State Tracking):** Implement `increment_dispatch_counter()` to update and report total fleet departures.

Run your script:

```bash
python3 Day-6/starter_astro_voyager.py
```

Instructor reference solution is available in [`solution_astro_voyager.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-6/solution_astro_voyager.py).

---

## 🧪 Sample Execution

```text
====================================================================
       🚀 ASTROVOYAGER: DEEP-SPACE FLEET DISPATCH TERMINAL 🚀
====================================================================
Enter Commander Name / Callsign: Commander Shepard
Enter Target Sector (e.g. Proxima Centauri): Alpha Centauri

====================================================================
  🛰️ ASTROVOYAGER MISSION CONTROL | SECTOR: ALPHA CENTAURI
  Commander: Commander Shepard | Security Clearance: LEVEL 2 (OFFICER)
====================================================================

>>> STEP 1: CONFIGURE SHIP & CREW PARAMETERS
  Enter destination distance in Light-Years (e.g. 4.24): 4.24
  Enter dry ship mass in metric tonnes (e.g. 150): 180
  Enter number of active crew members (e.g. 6): 8
  Enter warp factor (1.0 to 9.9, default 3.0): 3.5
  Enter current Shield Energy (0-250, default 200): 210
  Enter current Hull Armor (0-250, default 220): 230

>>> STEP 2: RUNNING TELEMETRY & FLIGHT DIAGNOSTICS...

  Initial Manifest: ['Emergency Beacon', 'First Aid Nanokits']
  Updated Manifest (after pass-by-reference calls): ['Emergency Beacon', 'First Aid Nanokits', 'Cryo-Stasis Pods', 'Sub-Space Transponder']

====================================================================
            OFFICIAL ASTROVOYAGER DISPATCH SUMMARY
====================================================================
Mission Commander:       Commander Shepard
Destination Sector:      Alpha Centauri (4.24 Light-Years)
Ship Mass & Crew:        180.0 tonnes | 8 personnel
Cruising Warp Factor:    Warp 3.5
Estimated Travel Time:   0.07 Earth Years (26 days)
Antimatter Fuel Needed:  33.92 metric tonnes
--------------------------------------------------------------------
LIFE SUPPORT & PROVISIONS REQUIRED:
  Food Rations:          360.0 kg
  Potable Water:         720.0 Litres
  Pressurized Oxygen:    192.0 kg
--------------------------------------------------------------------
DEFENSIVE & RISK ASSESSMENTS:
  Hull Integrity:        88.0% [GREEN] — Nominal — All Systems Operational
  Risk Index:            38.2 pts (LOW)
  Flight Clearance:      ✅ DISPATCH APPROVED FOR LAUNCH
--------------------------------------------------------------------
Active Dispatched Total: 1 mission(s) recorded in registry.
====================================================================
```
