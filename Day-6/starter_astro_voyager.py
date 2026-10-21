# ==============================================================================
# Course: Python Programming
# Session: Day 6 (Chapter 6: Functions — Sessions 13, 14 & 15)
# Lab Activity: AstroVoyager — Deep-Space Fleet Dispatch & Telemetry Hub
# Student Name: [YOUR NAME HERE]
# Date: [TODAY'S DATE]
#
# Pedagogical Focus:
#   - Defining and calling functions with parameters and return values (Liang 6.2 - 6.4)
#   - Positional, keyword, and default arguments (Liang 6.5 & 6.9)
#   - Passing mutable arguments by object reference (Liang 6.6)
#   - Returning multiple values and tuple unpacking (Liang 6.10)
#   - Variable scope (local vs global) and modular architecture (Liang 6.7 & 6.8)
#   - Importing reusable libraries (telemetry_helpers.py)
# ==============================================================================

# ------------------------------------------------------------------------------
# TODO 1: MODULAR IMPORTS (Liang Section 6.7)
# Import the required helper functions from the local 'telemetry_helpers' module:
#   - calculate_fuel_burn
#   - compute_comm_delay
#   - assess_hull_integrity
#   - format_mission_header
# ------------------------------------------------------------------------------
# HINT: from telemetry_helpers import calculate_fuel_burn, ...
from telemetry_helpers import (
    calculate_fuel_burn,
    compute_comm_delay,
    assess_hull_integrity,
    format_mission_header,
)


# Global dispatch counter (Liang Section 6.8)
TOTAL_DISPATCHED_MISSIONS = 0


# ------------------------------------------------------------------------------
# TODO 2: PURE FUNCTION WITH DEFAULT ARGUMENT (Liang Sections 6.2 & 6.9)
# Define 'calculate_warp_travel_time(distance_ly, warp_factor=1.0)':
#
# Formula:
#   effective_speed = warp_factor ** (10.0 / 3.0)  (Alcubierre Warp velocity scale)
#   travel_time_years = distance_ly / effective_speed
#
# Return the travel time in Earth years rounded to 2 decimal places.
# If distance_ly <= 0 or warp_factor <= 0, return 0.0.
# ------------------------------------------------------------------------------
def calculate_warp_travel_time(distance_ly, warp_factor=1.0):
    """
    Computes travel time in Earth years given distance and warp factor.
    """
    # TODO: Implement this function!
    # Replace the pass statement below:
    pass


# ------------------------------------------------------------------------------
# TODO 3: FUNCTION WITH KEYWORD/DEFAULT ARGUMENTS (Liang Section 6.9)
# Define 'provision_crew_supplies(crew_size, duration_days, safety_margin=0.20)':
#
# Calculations:
#   base_food_kg   = crew_size * duration_days * 1.5   (1.5 kg food per person/day)
#   base_water_l   = crew_size * duration_days * 3.0   (3.0 L water per person/day)
#   base_oxygen_kg = crew_size * duration_days * 0.8   (0.8 kg oxygen per person/day)
#
# Apply safety margin multiplier: total = base * (1.0 + safety_margin)
# Return the three values as a tuple: (total_food_kg, total_water_l, total_oxygen_kg)
# Round each to 1 decimal place.
# ------------------------------------------------------------------------------
def provision_crew_supplies(crew_size, duration_days, safety_margin=0.20):
    """
    Computes provision requirements including safety buffer.
    Returns: (total_food_kg, total_water_l, total_oxygen_kg)
    """
    # TODO: Implement this function!
    # Replace the pass statement below:
    pass


# ------------------------------------------------------------------------------
# TODO 4: MULTIPLE RETURN VALUES & CATEGORIZATION (Liang Section 6.10)
# Define 'evaluate_mission_risk(distance_ly, crew_count, anomaly_index=1.0)':
#
# Risk Formula:
#   risk_score = (distance_ly * 2.5) + (crew_count * 1.2) + (anomaly_index * 15.0)
#
# Classification Rules:
#   - If risk_score < 40.0:
#       category = "LOW"
#       approved = True
#   - Else if risk_score <= 100.0:
#       category = "MODERATE"
#       approved = True
#   - Else:
#       category = "HIGH / HAZARDOUS"
#       approved = False
#
# Return all 3 values: (round(risk_score, 1), category, approved)
# ------------------------------------------------------------------------------
def evaluate_mission_risk(distance_ly, crew_count, anomaly_index=1.0):
    """
    Evaluates mission safety score and returns (risk_score, category, is_approved).
    """
    # TODO: Implement this function!
    # Replace the pass statement below:
    pass


# ------------------------------------------------------------------------------
# TODO 5: PASS-BY-OBJECT-REFERENCE & MUTATION (Liang Section 6.6)
# Define 'load_cargo_manifest(manifest_list, cargo_item)':
#
# Appends 'cargo_item' directly to 'manifest_list'.
# In Python, lists are MUTABLE, so this modification persists in the caller's list!
# This function does not need to return anything (void function).
# ------------------------------------------------------------------------------
def load_cargo_manifest(manifest_list, cargo_item):
    """
    Demonstrates passing mutable lists by reference: appends cargo_item in-place.
    """
    # TODO: Implement this function!
    # Replace the pass statement below:
    pass


# ------------------------------------------------------------------------------
# TODO 6: VARIABLE SCOPE & COUNTERS (Liang Section 6.8)
# Define 'increment_dispatch_counter()':
# Uses the 'global' keyword to increment TOTAL_DISPATCHED_MISSIONS by 1.
# Returns the new count.
# ------------------------------------------------------------------------------
def increment_dispatch_counter():
    """
    Increments the global dispatch tracker.
    """
    global TOTAL_DISPATCHED_MISSIONS
    # TODO: Increment TOTAL_DISPATCHED_MISSIONS by 1 and return it!
    pass


# ==============================================================================
# MAIN MISSION CONTROL DISPATCHER TERMINAL
# ==============================================================================
def main():
    print("=" * 68)
    print("       🚀 ASTROVOYAGER: DEEP-SPACE FLEET DISPATCH TERMINAL 🚀")
    print("=" * 68)
    
    commander_name = input("Enter Commander Name / Callsign: ").strip()
    if not commander_name:
        commander_name = "Commander Shepard"
    
    target_sector = input("Enter Target Sector (e.g. Proxima Centauri): ").strip()
    if not target_sector:
        target_sector = "Proxima Centauri"
        
    # Print formatted header using imported helper
    header_str = format_mission_header(commander_name, sector=target_sector, clearance_level=2)
    print("\n" + header_str + "\n")
    
    # --------------------------------------------------------------------------
    # Collect Mission Parameters
    # --------------------------------------------------------------------------
    print(">>> STEP 1: CONFIGURE SHIP & CREW PARAMETERS")
    try:
        distance_ly = float(input("  Enter destination distance in Light-Years (e.g. 4.24): ") or "4.24")
        ship_mass = float(input("  Enter dry ship mass in metric tonnes (e.g. 150): ") or "150.0")
        crew_count = int(input("  Enter number of active crew members (e.g. 6): ") or "6")
        warp_speed = float(input("  Enter warp factor (1.0 to 9.9, default 3.0): ") or "3.0")
        shields = float(input("  Enter current Shield Energy (0-250, default 200): ") or "200.0")
        armor = float(input("  Enter current Hull Armor (0-250, default 220): ") or "220.0")
    except ValueError:
        print("  Invalid numeric entry! Falling back to standard mission presets.")
        distance_ly = 4.24
        ship_mass = 150.0
        crew_count = 6
        warp_speed = 3.0
        shields = 200.0
        armor = 220.0

    # --------------------------------------------------------------------------
    # Step 2: Execute Function Calculations & Module Calls
    # --------------------------------------------------------------------------
    print("\n>>> STEP 2: RUNNING TELEMETRY & FLIGHT DIAGNOSTICS...")
    
    # Call imported helper for fuel calculation
    fuel_needed = calculate_fuel_burn(distance_ly, ship_mass, engine_efficiency=0.90)
    
    # Call student function for warp flight time
    travel_years = calculate_warp_travel_time(distance_ly, warp_factor=warp_speed)
    travel_days = travel_years * 365.25 if travel_years else 0.0
    
    # Call student function for crew provisions (Unpack 3 returned values!)
    provisions = provision_crew_supplies(crew_count, max(1, int(travel_days)))
    if provisions is not None:
        food_kg, water_l, o2_kg = provisions
    else:
        food_kg, water_l, o2_kg = 0.0, 0.0, 0.0
    
    # Call student function for risk evaluation (Unpack 3 returned values!)
    risk_data = evaluate_mission_risk(distance_ly, crew_count, anomaly_index=1.2)
    if risk_data is not None:
        risk_score, risk_tier, is_approved = risk_data
    else:
        risk_score, risk_tier, is_approved = 0.0, "UNKNOWN", False
        
    # Call imported helper for hull integrity assessment (Unpack 3 values!)
    hull_pct, hull_code, hull_alert = assess_hull_integrity(shields, armor)
    
    # --------------------------------------------------------------------------
    # Step 3: Demonstrate Mutable Cargo List Loading (Pass-by-Reference)
    # --------------------------------------------------------------------------
    manifest = ["Emergency Beacon", "First Aid Nanokits"]
    print(f"\n  Initial Manifest: {manifest}")
    load_cargo_manifest(manifest, "Cryo-Stasis Pods")
    load_cargo_manifest(manifest, "Sub-Space Transponder")
    print(f"  Updated Manifest (after pass-by-reference calls): {manifest}")
    
    # Increment global dispatch counter
    increment_dispatch_counter()
    
    # --------------------------------------------------------------------------
    # Step 4: Display Comprehensive Flight Authorization Report
    # --------------------------------------------------------------------------
    print("\n" + "=" * 68)
    print("            OFFICIAL ASTROVOYAGER DISPATCH SUMMARY")
    print("=" * 68)
    print(f"Mission Commander:       {commander_name}")
    print(f"Destination Sector:      {target_sector} ({distance_ly:.2f} Light-Years)")
    print(f"Ship Mass & Crew:        {ship_mass:.1f} tonnes | {crew_count} personnel")
    print(f"Cruising Warp Factor:    Warp {warp_speed:.1f}")
    if travel_years is not None:
        print(f"Estimated Travel Time:   {travel_years:.2f} Earth Years ({travel_days:,.0f} days)")
    else:
        print("Estimated Travel Time:   [TODO 2 Incomplete]")
    print(f"Antimatter Fuel Needed:  {fuel_needed:,.2f} metric tonnes")
    print("-" * 68)
    print("LIFE SUPPORT & PROVISIONS REQUIRED:")
    print(f"  Food Rations:          {food_kg:,.1f} kg")
    print(f"  Potable Water:         {water_l:,.1f} Litres")
    print(f"  Pressurized Oxygen:    {o2_kg:,.1f} kg")
    print("-" * 68)
    print("DEFENSIVE & RISK ASSESSMENTS:")
    print(f"  Hull Integrity:        {hull_pct:.1f}% [{hull_code}] — {hull_alert}")
    print(f"  Risk Index:            {risk_score:.1f} pts ({risk_tier})")
    status_msg = "✅ DISPATCH APPROVED FOR LAUNCH" if is_approved else "❌ DISPATCH DENIED (HAZARD THRESHOLD)"
    print(f"  Flight Clearance:      {status_msg}")
    print("-" * 68)
    print(f"Active Dispatched Total: {TOTAL_DISPATCHED_MISSIONS} mission(s) recorded in registry.")
    print("=" * 68)


if __name__ == "__main__":
    main()
