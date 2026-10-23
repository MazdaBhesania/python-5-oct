# ==============================================================================
# Course: Python Programming
# Session: Day 7 (Chapter 7 & 8: 1D Lists & Multi-Dimensional Lists)
# Lab Activity: MatrixOps Analytics Hub — Regional Energy & Sensor Grid
# File: solution_matrix_ops.py (Reference Solution)
#
# Concepts Integrated:
#   - 1D List Aggregations (min, max, sum, len, average)
#   - List Comprehensions & Conditional Filtering
#   - 2D Matrix Creation, Indexing, and Traversal
#   - Row-wise and Column-wise Computations
#   - Main & Anti-Diagonal Traversal for Square Core Analysis
#   - Threshold Alert Detection in 2D Coordinates
#   - Deep Copy Matrix Isolation
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
print_matrix(energy_grid, "Initial Regional Energy Grid (MW)")


# ------------------------------------------------------------------------------
# STEP 2: Flattening & 1D Global Energy Statistics
# ------------------------------------------------------------------------------
# Flatten 2D matrix into a 1D list using list comprehension
all_readings = [val for row in energy_grid for val in row]

total_power = sum(all_readings)
min_power = min(all_readings)
max_power = max(all_readings)
avg_power = total_power / len(all_readings)

print("\n" + "=" * 50)
print(">>> STEP 2: GLOBAL 1D TELEMETRY STATISTICS")
print("=" * 50)
print(f"Total Grid Turbines:      {len(all_readings)}")
print(f"Total Power Generated:    {total_power:.1f} MW")
print(f"Lowest Turbine Output:    {min_power:.1f} MW")
print(f"Peak Turbine Output:      {max_power:.1f} MW")
print(f"Average Turbine Output:   {avg_power:.2f} MW")

# Filter high-yield turbines (> 75.0 MW) using list comprehension
high_yield_turbines = [p for p in all_readings if p > 75.0]
print(f"High-Yield Outputs (>75MW): {high_yield_turbines} (Count: {len(high_yield_turbines)})")


# ------------------------------------------------------------------------------
# STEP 3: Sector-by-Sector Analysis (Row Calculations)
# ------------------------------------------------------------------------------
print("\n" + "=" * 50)
print(">>> STEP 3: SECTOR PRODUCTION TOTALS (ROW SUMS)")
print("=" * 50)
sector_totals = calculate_row_totals(energy_grid)

for idx, (name, total) in enumerate(zip(sector_names, sector_totals)):
    print(f"  {name:<14} | Total: {total:6.1f} MW | Avg: {total / len(energy_grid[idx]):5.2f} MW")

top_sector_idx = sector_totals.index(max(sector_totals))
print(f"\n🏆 Top Producing Sector: {sector_names[top_sector_idx]} ({sector_totals[top_sector_idx]:.1f} MW)")


# ------------------------------------------------------------------------------
# STEP 4: Turbine Model Performance (Column Calculations)
# ------------------------------------------------------------------------------
print("\n" + "=" * 50)
print(">>> STEP 4: TURBINE FLEET TOTALS (COLUMN SUMS)")
print("=" * 50)
turbine_totals = calculate_col_totals(energy_grid)

for t_name, total in zip(turbine_names, turbine_totals):
    print(f"  {t_name:<10} | Combined Fleet Output: {total:6.1f} MW")


# ------------------------------------------------------------------------------
# STEP 5: Diagonal Cross-Grid Calibration Check (Square Matrix)
# ------------------------------------------------------------------------------
print("\n" + "=" * 50)
print(">>> STEP 5: DIAGONAL CALIBRATION VECTORS")
print("=" * 50)
grid_size = len(energy_grid)

# Primary Diagonal: Top-Left to Bottom-Right (grid[i][i])
primary_diag = [energy_grid[i][i] for i in range(grid_size)]
primary_sum = sum(primary_diag)

# Secondary Diagonal: Top-Right to Bottom-Left (grid[i][grid_size - 1 - i])
secondary_diag = [energy_grid[i][grid_size - 1 - i] for i in range(grid_size)]
secondary_sum = sum(secondary_diag)

print(f"Primary Diagonal Readings:   {primary_diag} -> Sum: {primary_sum:.1f} MW")
print(f"Secondary Diagonal Readings: {secondary_diag} -> Sum: {secondary_sum:.1f} MW")


# ------------------------------------------------------------------------------
# STEP 6: Overload Alert Detection & Coordinate Mapping
# ------------------------------------------------------------------------------
print("\n" + "=" * 50)
print(">>> STEP 6: OVERLOAD DETECTION (Readings >= 85.0 MW)")
print("=" * 50)
ALERT_THRESHOLD = 85.0
alerts_found = []

for r in range(grid_size):
    for c in range(len(energy_grid[r])):
        val = energy_grid[r][c]
        if val >= ALERT_THRESHOLD:
            alerts_found.append((r, c, val, sector_names[r], turbine_names[c]))

if alerts_found:
    print(f"⚠️  ALERT: {len(alerts_found)} Turbines operating at or above {ALERT_THRESHOLD} MW:")
    for r, c, val, sec, turb in alerts_found:
        print(f"   - [Row {r}, Col {c}] {sec} / {turb}: {val:.1f} MW (CRITICAL LOAD)")
else:
    print("All turbines operating under normal parameters.")


# ------------------------------------------------------------------------------
# STEP 7: Safe Simulation Mode (Deep Copy vs Mutating Original)
# ------------------------------------------------------------------------------
print("\n" + "=" * 50)
print(">>> STEP 7: WHAT-IF SIMULATION (ISOLATED DEEP COPY)")
print("=" * 50)

# Simulate a 15% efficiency boost across Sector Alpha
simulation_grid = clone_matrix(energy_grid)

# Boost sector 0 by 15%
for c in range(len(simulation_grid[0])):
    simulation_grid[0][c] = round(simulation_grid[0][c] * 1.15, 1)

print("Original Grid Row 0 (Unchanged):", energy_grid[0])
print("Simulated Grid Row 0 (+15%):     ", simulation_grid[0])

print("\n" + "=" * 72)
print(">>> MATRIXOPS ANALYTICS RUN COMPLETED SUCCESSFULLY!")
print("=" * 72)
