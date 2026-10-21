# ==============================================================================
# Day 6: In-Class Activity — Function Debugging Bug Hunt
# Topics Covered:
#   - Challenge 1: The "Printing Instead of Returning" Trap (Liang 6.4)
#   - Challenge 2: Positional Argument Following Keyword Argument (Liang 6.5)
#   - Challenge 3: Non-Default Parameter Following Default Parameter (Liang 6.9)
#   - Challenge 4: UnboundLocalError / Scope Collision (Liang 6.8)
#   - Challenge 5: Multiple Return Value Unpacking Mismatch (Liang 6.10)
#
# Instructions:
# 1. Read through each challenge below.
# 2. Uncomment the buggy line(s) under "UNCOMMENT TO TEST".
# 3. Run the script: python3 Day-6/bug_hunt_day6.py
# 4. Observe the error message or faulty output.
# 5. Fix the bug so that all 5 challenges execute smoothly and output correctly!
# ==============================================================================

print("=" * 68)
print("             DAY 6 BUG HUNT: 5 FUNCTION CHALLENGES")
print("=" * 68)


# ------------------------------------------------------------------------------
# CHALLENGE 1: The "Printing Instead of Returning" Trap (Liang 6.4)
# Goal: Compute sales tax for an invoice subtotal and add it to the subtotal.
# Problem: A function that uses 'print()' instead of 'return' produces None!
#          Attempting arithmetic (+ tax) on None raises:
#          TypeError: unsupported operand type(s) for +: 'float' and 'NoneType'
# Fix: Replace 'print()' with 'return' inside the function body.
# ------------------------------------------------------------------------------
print("\n[Challenge 1: Print vs Return Trap]")

# BUGGY VERSION (Uncomment to test):
# def compute_tax_buggy(subtotal, tax_rate=0.08):
#     tax_amount = subtotal * tax_rate
#     print(f"Tax calculated: {tax_amount}")  # Prints, but returns None!
#
# subtotal = 120.00
# tax = compute_tax_buggy(subtotal)
# total = subtotal + tax  # CRASH! float + NoneType
# print(f"Total Invoice: ${total:.2f}")

# FIXED VERSION:
def compute_tax_fixed(subtotal, tax_rate=0.08):
    tax_amount = subtotal * tax_rate
    return tax_amount  # Properly returns calculated value to caller!

subtotal = 120.00
tax = compute_tax_fixed(subtotal)
total = subtotal + tax
print(f"  Subtotal: ${subtotal:.2f} | Tax: ${tax:.2f} | Total: ${total:.2f} (Correct!)")


# ------------------------------------------------------------------------------
# CHALLENGE 2: Positional Argument Following Keyword Argument (Liang 6.5)
# Goal: Configure a telemetry sensor with ID, frequency, and units.
# Problem: Python syntax strictly requires ALL positional arguments to appear
#          BEFORE any keyword arguments. Mixing them out of order raises:
#          SyntaxError: positional argument follows keyword argument
# Fix: Move all positional arguments to the front, or pass all as keyword arguments.
# ------------------------------------------------------------------------------
print("\n[Challenge 2: Argument Ordering]")

def configure_sensor(sensor_id, frequency_hz, units="Celsius"):
    return f"Sensor [{sensor_id}]: {frequency_hz} Hz ({units})"

# BUGGY VERSION (Uncomment to test):
# # SyntaxError occurs at parse time if uncommented:
# # config_str = configure_sensor(sensor_id="TEMP_MOD_1", 250, units="Kelvin")

# FIXED VERSION:
# Option A: Place positional argument '250' before keyword arguments:
config_str = configure_sensor("TEMP_MOD_1", 250, units="Kelvin")
# Option B: Use keyword arguments for all:
# config_str = configure_sensor(sensor_id="TEMP_MOD_1", frequency_hz=250, units="Kelvin")

print(f"  {config_str} (Correct!)")


# ------------------------------------------------------------------------------
# CHALLENGE 3: Non-Default Parameter Following Default Parameter (Liang 6.9)
# Goal: Define a broadcast function with message priority and message body.
# Problem: Defining parameters with default values BEFORE parameters without
#          defaults causes Python to fail at parse time:
#          SyntaxError: non-default argument follows default argument
# Fix: Reorder parameters so required parameters come first, defaults last.
# ------------------------------------------------------------------------------
print("\n[Challenge 3: Default Parameter Order in Definition]")

# BUGGY VERSION (Uncomment to test - causes SyntaxError on def):
# # def broadcast_alert_buggy(priority="STANDARD", message):
# #     return f"[{priority}] {message}"

# FIXED VERSION:
def broadcast_alert_fixed(message, priority="STANDARD"):
    """Required parameters first, parameters with default values last!"""
    return f"[{priority}] {message}"

print(f"  {broadcast_alert_fixed('Solar flare detected!')}")
print(f"  {broadcast_alert_fixed('Meteor shower warning!', priority='CRITICAL')}")


# ------------------------------------------------------------------------------
# CHALLENGE 4: UnboundLocalError / Scope Collision (Liang 6.8)
# Goal: Track total dispatched missions using a counter.
# Problem: Inside 'record_launch()', Python sees 'mission_count += 1' as an
#          assignment to 'mission_count', automatically categorizing it as a
#          LOCAL variable. But trying to read it on the right side before it is
#          assigned raises:
#          UnboundLocalError: cannot access local variable 'mission_count' where it is not associated with a value
# Fix: Declare 'global mission_count' inside the function, or pass & return it!
# ------------------------------------------------------------------------------
print("\n[Challenge 4: UnboundLocalError & Variable Scope]")

mission_count = 10

# BUGGY VERSION (Uncomment to test):
# def record_launch_buggy():
#     mission_count += 1  # UnboundLocalError!
#     print(f"Missions logged: {mission_count}")
# record_launch_buggy()

# FIXED VERSION:
def record_launch_fixed():
    global mission_count  # Explicitly tell Python to use the global variable!
    mission_count += 1
    return mission_count

new_total = record_launch_fixed()
print(f"  Global missions updated: {new_total} (Correct!)")


# ------------------------------------------------------------------------------
# CHALLENGE 5: Multiple Return Value Unpacking Mismatch (Liang 6.10)
# Goal: Compute 3D navigational vectors (dx, dy, dz) and unpack into variables.
# Problem: The function returns 3 values (a tuple of 3 items), but the caller
#          attempts to unpack into only 2 variables. This raises:
#          ValueError: too many values to unpack (expected 2)
# Fix: Provide exactly 3 recipient variables to match the returned tuple.
# ------------------------------------------------------------------------------
print("\n[Challenge 5: Tuple Unpacking Mismatch]")

def calculate_displacement(origin, target):
    """Returns displacement in X, Y, and Z axes as a 3-element tuple."""
    dx = target[0] - origin[0]
    dy = target[1] - origin[1]
    dz = target[2] - origin[2]
    return dx, dy, dz  # Returns tuple of 3 values!

coord_start = (0.0, 10.0, 5.0)
coord_end = (15.0, 20.0, 12.0)

# BUGGY VERSION (Uncomment to test):
# delta_x, delta_y = calculate_displacement(coord_start, coord_end)  # CRASH! Expected 2, got 3

# FIXED VERSION:
delta_x, delta_y, delta_z = calculate_displacement(coord_start, coord_end)
print(f"  Displacement vector: dx={delta_x:.1f}, dy={delta_y:.1f}, dz={delta_z:.1f} (Correct!)")

print("\n" + "=" * 68)
print("             ALL 5 BUG HUNT CHALLENGES RESOLVED!")
print("=" * 68)
