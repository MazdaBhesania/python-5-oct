# ==============================================================================
# Course: Python Programming
# Session: Day 6 (Chapter 6: Functions — Sessions 13, 14 & 15)
# Textbook Reference: Liang, Chapter 6 (Sections 6.1 – 6.10)
#
# Sections Covered:
#   - Session 13: Defining & Calling Functions (Liang 6.1 – 6.4)
#       * 6.1: Introduction to Functions & Modular Programming
#       * 6.2: Defining Functions (def keyword, headers, parameters, return)
#       * 6.3: Calling Functions (Execution flow, call stack, arguments)
#       * 6.4: Functions With vs Without Return Values (Void vs Value-Returning)
#   - Session 14: Argument Types, Pass-by-Reference & Multiple Returns (Liang 6.5, 6.6, 6.9, 6.10)
#       * 6.5: Positional vs Keyword Arguments (Rules for mixing)
#       * 6.6: Passing Arguments by Reference (Python's Object Reference Model)
#       * 6.9: Default Arguments (Trailing defaults, optional parameters)
#       * 6.10: Returning Multiple Values (Tuple packing & unpacking)
#   - Session 15: Variable Scope & Modular Code Architecture (Liang 6.7 – 6.8)
#       * 6.7: Modularizing Code (Creating custom modules & imports)
#       * 6.8: Variable Scope (Local vs Global, shadowing, global keyword)
# ==============================================================================

print("=" * 72)
print("     DAY 6: MASTERING PYTHON FUNCTIONS (SESSIONS 13, 14 & 15)")
print("=" * 72)


# ==============================================================================
# 1. SESSION 13: DEFINING & CALLING FUNCTIONS (Liang 6.1 - 6.4)
# ==============================================================================
print("\n" + "=" * 55)
print(">>> PART 1: DEFINING & CALLING FUNCTIONS (Liang 6.1 - 6.4)")
print("=" * 55)

# ------------------------------------------------------------------------------
# 1.1: Function Definition Syntax & Docstrings (Liang 6.2)
# ------------------------------------------------------------------------------
# Syntax:
# def function_name(parameter1, parameter2, ...):
#     """Optional docstring describing what the function does."""
#     # Function body statements
#     return value_to_return

def calculate_circle_area(radius):
    """Compute and return the area of a circle given its radius."""
    PI = 3.141592653589793
    area = PI * (radius ** 2)
    return area

# 1.2 Calling the function (Liang 6.3)
r = 5.0
circle_area = calculate_circle_area(r)
print(f"[6.2/6.3] Circle Area with radius {r}: {circle_area:.2f}")


# ------------------------------------------------------------------------------
# 1.3: Void Functions vs Value-Returning Functions (Liang 6.4)
# ------------------------------------------------------------------------------
# Value-returning functions compute a result and send it back with 'return'.
# Void functions perform actions (e.g., printing or writing to a file).
# In Python, if a function does NOT explicitly return a value, it returns None.

def print_mission_banner(mission_title):
    """Void function: Prints a decorative header banner. Returns None implicitly."""
    print("*" * 45)
    print(f"  🚀 MISSION: {mission_title.upper()}")
    print("*" * 45)
    # Notice: No return statement here!

banner_result = print_mission_banner("Apollo Deep Space Survey")
print(f"[6.4] Return value of print_mission_banner(): {banner_result} (type: {type(banner_result).__name__})")

# Best Practice Note:
# Functions should generally RETURN their results rather than printing them.
# Returning values makes your functions reusable, composable, and testable!


# ==============================================================================
# 2. SESSION 14: ARGUMENT TYPES, OBJECT REFERENCES & RETURNS (Liang 6.5, 6.6, 6.9, 6.10)
# ==============================================================================
print("\n" + "=" * 55)
print(">>> PART 2: ARGUMENTS, REFERENCES & MULTIPLE RETURNS (Liang 6.5 - 6.10)")
print("=" * 55)

# ------------------------------------------------------------------------------
# 2.1: Positional vs Keyword Arguments (Liang 6.5)
# ------------------------------------------------------------------------------
def compute_velocity(distance_km, time_hours):
    """Compute average speed in km/h."""
    return distance_km / time_hours

# Positional: arguments matched strictly by position (order matters!)
v1 = compute_velocity(300, 2)
print(f"[6.5] Positional args (300 km in 2 hrs): {v1:.1f} km/h")

# Keyword: arguments matched by parameter name (order does NOT matter!)
v2 = compute_velocity(time_hours=2, distance_km=300)
print(f"[6.5] Keyword args (time=2, dist=300):    {v2:.1f} km/h")

# Mixed: Positional MUST come before keyword arguments!
v3 = compute_velocity(300, time_hours=2)
print(f"[6.5] Mixed args (positional first):      {v3:.1f} km/h")
# CRITICAL RULE: compute_velocity(distance_km=300, 2) -> SyntaxError!


# ------------------------------------------------------------------------------
# 2.2: Default Arguments (Liang 6.9)
# ------------------------------------------------------------------------------
# Default arguments provide fallback values if the caller omits them.
# RULE: Parameters with defaults MUST follow all parameters without defaults!
def dispatch_starship(ship_name, destination="Mars Colony", warp_factor=1, shields_active=True):
    """Dispatches a ship with sensible defaults for destination, warp, and shields."""
    shield_status = "ONLINE" if shields_active else "OFFLINE"
    return (f"  Ship: {ship_name:<16} | Dest: {destination:<15} | "
            f"Warp: {warp_factor} | Shields: {shield_status}")

print("[6.9] Default Arguments Demonstration:")
print(dispatch_starship("USS Enterprise"))  # Uses all 3 defaults
print(dispatch_starship("Millennium Falcon", "Kessel Sector", warp_factor=5))
print(dispatch_starship("Voyager Probe", shields_active=False))


# ------------------------------------------------------------------------------
# 2.3: Passing Arguments by Reference (Object Reference Model) (Liang 6.6)
# ------------------------------------------------------------------------------
# In Python, all variables are references to objects:
# - IMMUTABLE objects (int, float, str, tuple, bool):
#   Reassigning inside a function does NOT modify the caller's variable!
# - MUTABLE objects (list, dict, set):
#   Modifying the contents inside a function modifies the caller's object!

def modify_primitives(num, text):
    """Attempts to modify immutable arguments."""
    num += 100
    text += " (MODIFIED)"
    print(f"    Inside modify_primitives: num={num}, text='{text}'")

def modify_list(items):
    """Modifies a mutable list in place."""
    items.append("NEW_CARGO_CRATE")
    print(f"    Inside modify_list: items={items}")

print("[6.6] Python Object Reference Passing Model:")
score_val = 10
label_val = "Alpha"
print(f"  Before immutable call: score={score_val}, label='{label_val}'")
modify_primitives(score_val, label_val)
print(f"  After immutable call:  score={score_val}, label='{label_val}' (UNCHANGED!)")

inventory = ["Fuel Cells", "Oxygen Tank"]
print(f"  Before mutable list call: inventory={inventory}")
modify_list(inventory)
print(f"  After mutable list call:  inventory={inventory} (MUTATED IN-PLACE!)")


# ------------------------------------------------------------------------------
# 2.4: Returning Multiple Values (Liang 6.10)
# ------------------------------------------------------------------------------
# A Python function can return multiple values separated by commas.
# Python automatically packs them into a single tuple.
# The caller can unpack them into separate variables!

def calculate_flight_stats(speed_readings):
    """Calculates min, max, average, and reading count from a sequence."""
    if not speed_readings:
        return 0.0, 0.0, 0.0, 0
    
    min_speed = min(speed_readings)
    max_speed = max(speed_readings)
    avg_speed = sum(speed_readings) / len(speed_readings)
    count = len(speed_readings)
    
    return min_speed, max_speed, avg_speed, count  # Returns a tuple!

speeds = [450.5, 620.0, 510.2, 740.8, 595.0]

# Tuple unpacking:
low, high, avg, total_samples = calculate_flight_stats(speeds)
print(f"[6.10] Multiple Return Values Unpacked:")
print(f"  Samples: {total_samples} | Min: {low:.1f} | Max: {high:.1f} | Avg: {avg:.2f} km/s")


# ==============================================================================
# 3. SESSION 15: VARIABLE SCOPE & MODULAR ARCHITECTURE (Liang 6.7 - 6.8)
# ==============================================================================
print("\n" + "=" * 55)
print(">>> PART 3: VARIABLE SCOPE & MODULAR CODE (Liang 6.7 - 6.8)")
print("=" * 55)

# ------------------------------------------------------------------------------
# 3.1: Local vs Global Scope & Variable Shadowing (Liang 6.8)
# ------------------------------------------------------------------------------
# Global variable: defined outside any function; visible to all functions in this file.
station_status = "NORMAL_OPERATION"
telemetry_counter = 0

def log_telemetry_reading(sensor_name, value):
    """Demonstrates local variables and accessing a global variable."""
    # 'sensor_name', 'value', and 'entry' are LOCAL variables.
    # They are created when log_telemetry_reading() is called,
    # and destroyed when it finishes.
    entry = f"[{sensor_name}] -> {value}"
    
    # Reading a global variable is permitted without 'global' keyword:
    print(f"  Reading global station_status inside function: '{station_status}'")
    print(f"  Recorded local entry: {entry}")

log_telemetry_reading("Thermal Core", 98.6)

def demonstrate_shadowing():
    """Local variable 'station_status' shadows (hides) the global one."""
    station_status = "LOCAL_OVERRIDE"  # Shadows global station_status!
    print(f"  Inside shadowing func: station_status = '{station_status}'")

demonstrate_shadowing()
print(f"  Global station_status remains unchanged: '{station_status}'")


# ------------------------------------------------------------------------------
# 3.2: The 'global' Keyword (When & How to Use, and Why to Minimize) (Liang 6.8)
# ------------------------------------------------------------------------------
# To REASSIGN a global variable inside a function, you must declare it with 'global'.
# CAUTION: Overusing 'global' leads to spaghetti code, race conditions, and bugs.
# Prefer passing parameters in and returning updated values!

def increment_telemetry():
    """Modifies the global variable using the 'global' keyword."""
    global telemetry_counter
    telemetry_counter += 1

increment_telemetry()
increment_telemetry()
print(f"[6.8] Global telemetry_counter after 2 increments: {telemetry_counter}")


# ------------------------------------------------------------------------------
# 3.3: Modularizing Code (Creating Reusable Libraries) (Liang 6.7)
# ------------------------------------------------------------------------------
# A Python module is simply a .py file containing reusable functions.
# Other scripts can import it:
#   import my_module
#   from my_module import specific_function
#   from my_module import specific_function as alias
#
# Best practice pattern inside modules:
# if __name__ == '__main__':
#     # Code here runs ONLY when the file is executed directly,
#     # NOT when it is imported into another script!
print("[6.7] Modular Code Pattern:")
print("  - Place reusable functions in separate .py files (e.g. telemetry_helpers.py)")
print("  - Import functions cleanly using: from telemetry_helpers import calculate_fuel_burn")
print("  - Protect runnable test code with: if __name__ == '__main__':")

print("\n" + "=" * 72)
print("     ALL CONCEPTS SUCCESSFULLY DEMONSTRATED!")
print("=" * 72)
