# ==============================================================================
# Course: Python Programming
# Session: Day 7 (Chapter 7 & 8: 1D Lists & Multi-Dimensional Lists)
# Lab Activity: MatrixOps Analytics Hub — Regional Energy & Sensor Grid
# File: starter_matrix_ops.py (Student Starter Template)
#
# Instructions:
# Complete the 7 TODO sections below to build your grid analytics dashboard!
# Follow the docstrings and guided comments.
# ==============================================================================

import copy
from matrix_helpers import (
    create_grid,
    print_matrix,
    calculate_row_totals,
    calculate_col_totals,
    transpose_matrix,
    clone_matrix
)

print("=" * 72)
print("     ⚡ MATRIXOPS ANALYTICS HUB: REGIONAL ENERGY SENSOR GRID ⚡")
print("=" * 72)

# ------------------------------------------------------------------------------
# STEP 1: Regional Energy Grid Data (4 Sectors / Rows x 4 Turbines / Columns)
# Values represent Megawatts (MW) generated per turbine across 4 sectors.
# ------------------------------------------------------------------------------
sector_names = ["Sector Alpha", "Sector Beta", "Sector Gamma", "Sector Delta"]
turbine_names = ["Turbine-1", "Turbine-2", "Turbine-3", "Turbine-4"]

energy_grid = [
    [45.5, 62.0, 78.5, 55.0],   # Sector Alpha
    [52.0, 81.5, 90.0, 64.5],   # Sector Beta
    [38.0, 42.5, 49.0, 51.5],   # Sector Gamma
    [70.0, 88.5, 95.0, 84.0]    # Sector Delta
]

print("\n[Step 1: Raw Sensor Grid Initialized]")
# TODO 1.1: Use print_matrix() from matrix_helpers to display energy_grid
# with label "Initial Regional Energy Grid (MW)"
# YOUR CODE HERE


# ------------------------------------------------------------------------------
# STEP 2: Flattening & 1D Global Energy Statistics
# ------------------------------------------------------------------------------
# TODO 2.1: Flatten the 2D energy_grid into a single 1D list called `all_readings`
# Hint: Use a nested list comprehension: [val for row in energy_grid for val in row]
all_readings = []  # REPLACE WITH YOUR CODE

# TODO 2.2: Compute the basic statistics using 1D list built-ins:
# total_power = ...
# min_power = ...
# max_power = ...
# avg_power = ...

print("\n" + "=" * 50)
print(">>> STEP 2: GLOBAL 1D TELEMETRY STATISTICS")
print("=" * 50)
# TODO 2.3: Print total turbines, total power, lowest, peak, and average

# TODO 2.4: Use a list comprehension to filter high-yield readings (> 75.0 MW)
high_yield_turbines = []  # REPLACE WITH YOUR COMPREHENSION
# print(f"High-Yield Outputs (>75MW): {high_yield_turbines} (Count: {len(high_yield_turbines)})")


# ------------------------------------------------------------------------------
# STEP 3: Sector-by-Sector Analysis (Row Calculations)
# ------------------------------------------------------------------------------
print("\n" + "=" * 50)
print(">>> STEP 3: SECTOR PRODUCTION TOTALS (ROW SUMS)")
print("=" * 50)
# TODO 3.1: Use calculate_row_totals() to find the total power of each sector
sector_totals = []  # REPLACE WITH YOUR CODE

# TODO 3.2: Iterate through sector_names and sector_totals to print each sector's total & average
# Hint: Use enumerate() or zip(sector_names, sector_totals)

# TODO 3.3: Find the index of the top producing sector using sector_totals.index(max(sector_totals))
# Print the winning sector's name and total


# ------------------------------------------------------------------------------
# STEP 4: Turbine Model Performance (Column Calculations)
# ------------------------------------------------------------------------------
print("\n" + "=" * 50)
print(">>> STEP 4: TURBINE FLEET TOTALS (COLUMN SUMS)")
print("=" * 50)
# TODO 4.1: Use calculate_col_totals() to compute sums across each column
turbine_totals = []  # REPLACE WITH YOUR CODE

# TODO 4.2: Iterate through turbine_names and turbine_totals to print the combined output


# ------------------------------------------------------------------------------
# STEP 5: Diagonal Cross-Grid Calibration Check (Square Matrix)
# ------------------------------------------------------------------------------
print("\n" + "=" * 50)
print(">>> STEP 5: DIAGONAL CALIBRATION VECTORS")
print("=" * 50)
grid_size = len(energy_grid)

# TODO 5.1: Extract the primary diagonal readings (row == col -> energy_grid[i][i])
primary_diag = []  # REPLACE WITH YOUR LIST COMPREHENSION
primary_sum = 0    # sum(primary_diag)

# TODO 5.2: Extract the secondary diagonal readings (energy_grid[i][grid_size - 1 - i])
secondary_diag = []  # REPLACE WITH YOUR LIST COMPREHENSION
secondary_sum = 0    # sum(secondary_diag)

# Print both diagonal vectors and their sums


# ------------------------------------------------------------------------------
# STEP 6: Overload Alert Detection & Coordinate Mapping
# ------------------------------------------------------------------------------
print("\n" + "=" * 50)
print(">>> STEP 6: OVERLOAD DETECTION (Readings >= 85.0 MW)")
print("=" * 50)
ALERT_THRESHOLD = 85.0
alerts_found = []

# TODO 6.1: Use nested loops (for r in range(grid_size): for c in range(...))
# Check if energy_grid[r][c] >= ALERT_THRESHOLD.
# If so, append a tuple (r, c, val, sector_names[r], turbine_names[c]) to alerts_found.

# TODO 6.2: Print formatted alert messages if alerts_found has items,
# else print "All turbines operating under normal parameters."


# ------------------------------------------------------------------------------
# STEP 7: Safe Simulation Mode (Deep Copy vs Mutating Original)
# ------------------------------------------------------------------------------
print("\n" + "=" * 50)
print(">>> STEP 7: WHAT-IF SIMULATION (ISOLATED DEEP COPY)")
print("=" * 50)

# TODO 7.1: Create an isolated copy of energy_grid using clone_matrix()
simulation_grid = []  # REPLACE WITH clone_matrix(energy_grid)

# TODO 7.2: Apply a 15% efficiency boost (* 1.15) to all turbines in Sector Alpha (row 0)
# within simulation_grid.

# TODO 7.3: Verify that energy_grid[0] was NOT modified, while simulation_grid[0] was!
# print("Original Grid Row 0 (Unchanged):", energy_grid[0])
# print("Simulated Grid Row 0 (+15%):     ", simulation_grid[0])

print("\n" + "=" * 72)
print(">>> END OF STARTER TEMPLATE — FILL IN TODOS TO TEST")
print("=" * 72)
