# ==============================================================================
# Day 6: Quick Concept Drills — Mastering Functions
# Note: Practice these 3 short exercises during lecture or as a warm-up!
#
# Topics Covered:
#   - Drill 1: Pure Functions & Return Values (Liang 6.2 – 6.4)
#   - Drill 2: Positional, Keyword & Default Arguments (Liang 6.5 & 6.9)
#   - Drill 3: Returning Multiple Values & Tuple Unpacking (Liang 6.10)
# ==============================================================================

import math

print("=" * 68)
print("             DAY 6: 3 QUICK FUNCTION PRACTICE DRILLS")
print("=" * 68)


# ------------------------------------------------------------------------------
# DRILL 1: Pure Functions & Return Values (Liang Sections 6.2 – 6.4)
# 1. Define 'calculate_hypotenuse(a, b)': Computes and returns sqrt(a^2 + b^2).
# 2. Define 'is_prime(n)': Returns True if integer n > 1 is prime, False otherwise.
# ------------------------------------------------------------------------------
print("\n--- Drill 1: Mathematical & Predicate Functions ---")

def calculate_hypotenuse(side_a, side_b):
    """Calculates the hypotenuse of a right-angled triangle."""
    return math.sqrt(side_a ** 2 + side_b ** 2)

def is_prime(n):
    """Returns True if n is prime, False otherwise (Liang Case Study)."""
    if n <= 1:
        return False
    # Check divisors from 2 up to sqrt(n)
    for divisor in range(2, int(math.isqrt(n)) + 1):
        if n % divisor == 0:
            return False
    return True

# Test Drill 1
hyp = calculate_hypotenuse(3.0, 4.0)
print(f"Hypotenuse of 3.0 and 4.0: {hyp:.2f}")

test_primes = [1, 2, 17, 21, 29, 35, 97]
print("Prime number check:")
for num in test_primes:
    status = "PRIME" if is_prime(num) else "COMPOSITE / NON-PRIME"
    print(f"  Number {num:2d} -> {status}")


# ------------------------------------------------------------------------------
# DRILL 2: Positional, Keyword & Default Arguments (Liang Sections 6.5 & 6.9)
# Define 'generate_flight_badge(pilot_name, callsign="Starlight", rank="Cadet", hours=0)':
# Formats and returns a clean badge string.
# Demonstrate calling it:
#   a) With only the required argument
#   b) With positional arguments
#   c) With mixed positional and keyword arguments
# ------------------------------------------------------------------------------
print("\n--- Drill 2: Flexible Argument Patterns ---")

def generate_flight_badge(pilot_name, callsign="Starlight", rank="Cadet", flight_hours=0):
    """Generates an astronaut flight badge string using default and keyword args."""
    return f"[{rank.upper()}] {pilot_name} (Callsign: '{callsign}') | Logged: {flight_hours} hrs"

# a) Only required argument (uses all 3 defaults):
badge1 = generate_flight_badge("Elena Rostova")
print(f"  Badge 1 (Defaults): {badge1}")

# b) Positional arguments:
badge2 = generate_flight_badge("Marcus Vance", "Viper", "Commander", 1450)
print(f"  Badge 2 (Positional): {badge2}")

# c) Mixed positional and keyword arguments:
badge3 = generate_flight_badge("Aria Chen", rank="Lieutenant", flight_hours=320)
print(f"  Badge 3 (Keyword/Mixed): {badge3}")


# ------------------------------------------------------------------------------
# DRILL 3: Multiple Return Values & Tuple Unpacking (Liang Section 6.10)
# Define 'analyze_telemetry_batch(readings)':
# Computes and returns 4 values in a single tuple:
#   (min_reading, max_reading, avg_reading, spread)
# Unpack the returned tuple into 4 distinct variables and display summary.
# ------------------------------------------------------------------------------
print("\n--- Drill 3: Multiple Return Values & Unpacking ---")

def analyze_telemetry_batch(readings):
    """Computes minimum, maximum, average, and spread (max - min) from numeric readings."""
    if not readings:
        return 0.0, 0.0, 0.0, 0.0
    
    lowest = min(readings)
    highest = max(readings)
    average = sum(readings) / len(readings)
    spread = highest - lowest
    
    return lowest, highest, average, spread

sensor_data = [102.4, 108.9, 99.1, 105.3, 112.7, 104.0]

# Unpack the 4 returned values
min_val, max_val, avg_val, delta = analyze_telemetry_batch(sensor_data)

print(f"Sensor Readings Batch: {sensor_data}")
print(f"  Lowest Value:   {min_val:.1f}")
print(f"  Highest Value:  {max_val:.1f}")
print(f"  Average Value:  {avg_val:.2f}")
print(f"  Reading Spread: {delta:.2f}")

print("\n" + "=" * 68)
print("             ALL 3 PRACTICE DRILLS COMPLETE!")
print("=" * 68)
