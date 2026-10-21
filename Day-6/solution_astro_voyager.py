# ==============================================================================
# Course: Python Programming
# Session: Day 6 (Chapter 6: Functions — Sessions 13, 14 & 15)
# Lab Activity: AstroVoyager — Deep-Space Fleet Dispatch & Telemetry Hub (SOLUTION)
# Instructor / Reference Solution
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
# STEP 1: MODULAR IMPORTS (Liang Section 6.7)
# Import functions from telemetry_helpers.py
# ------------------------------------------------------------------------------
from telemetry_helpers import (
    calculate_fuel_burn,
    compute_comm_delay,
    assess_hull_integrity,
    format_mission_header,
)


# Global dispatch counter (Liang Section 6.8)
TOTAL_DISPATCHED_MISSIONS = 0


# ------------------------------------------------------------------------------
# STEP 2: PURE FUNCTION WITH DEFAULT ARGUMENT (Liang Sections 6.2 & 6.9)
# ------------------------------------------------------------------------------
def calculate_warp_travel_time(distance_ly, warp_factor=1.0):
    """
    Computes travel time in Earth years given distance and warp factor.
    
    Formula:
        effective_speed = warp_factor ** (10.0 / 3.0)
        travel_time_years = distance_ly / effective_speed
    """
    if distance_ly <= 0 or warp_factor <= 0:
        return 0.0
    effective_speed = warp_factor ** (10.0 / 3.0)
    travel_time_years = distance_ly / effective_speed
    return round(travel_time_years, 2)


# ------------------------------------------------------------------------------
# STEP 3: FUNCTION WITH KEYWORD/DEFAULT ARGUMENTS (Liang Section 6.9)
# ------------------------------------------------------------------------------
def provision_crew_supplies(crew_size, duration_days, safety_margin=0.20):
    """
    Computes provision requirements including safety buffer.
    Returns: (total_food_kg, total_water_l, total_oxygen_kg)
    """
    if crew_size <= 0 or duration_days <= 0:
        return 0.0, 0.0, 0.0
    
    multiplier = 1.0 + safety_margin
    total_food_kg = round(crew_size * duration_days * 1.5 * multiplier, 1)
    total_water_l = round(crew_size * duration_days * 3.0 * multiplier, 1)
    total_oxygen_kg = round(crew_size * duration_days * 0.8 * multiplier, 1)
    
    return total_food_kg, total_water_l, total_oxygen_kg


# ------------------------------------------------------------------------------
# STEP 4: MULTIPLE RETURN VALUES & CATEGORIZATION (Liang Section 6.10)
# ------------------------------------------------------------------------------
def evaluate_mission_risk(distance_ly, crew_count, anomaly_index=1.0):
    """
    Evaluates mission safety score and returns (risk_score, category, is_approved).
    """
    risk_score = (distance_ly * 2.5) + (crew_count * 1.2) + (anomaly_index * 15.0)
    risk_score = round(risk_score, 1)
    
    if risk_score < 40.0:
        category = "LOW"
        approved = True
    elif risk_score <= 100.0:
        category = "MODERATE"
        approved = True
    else:
        category = "HIGH / HAZARDOUS"
        approved = False
        
    return risk_score, category, approved


# ------------------------------------------------------------------------------
# STEP 5: PASS-BY-OBJECT-REFERENCE & MUTATION (Liang Section 6.6)
# ------------------------------------------------------------------------------
def load_cargo_manifest(manifest_list, cargo_item):
    """
    Demonstrates passing mutable lists by reference: appends cargo_item in-place.
    """
    manifest_list.append(cargo_item)


# ------------------------------------------------------------------------------
# STEP 6: VARIABLE SCOPE & COUNTERS (Liang Section 6.8)
# ------------------------------------------------------------------------------
def increment_dispatch_counter():
    """
    Increments the global dispatch tracker using the global keyword.
    """
    global TOTAL_DISPATCHED_MISSIONS
    TOTAL_DISPATCHED_MISSIONS += 1
    return TOTAL_DISPATCHED_MISSIONS


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
        raw_dist = input("  Enter destination distance in Light-Years (e.g. 4.24): ").strip()
        distance_ly = float(raw_dist) if raw_dist else 4.24
        
        raw_mass = input("  Enter dry ship mass in metric tonnes (e.g. 150): ").strip()
        ship_mass = float(raw_mass) if raw_mass else 150.0
        
        raw_crew = input("  Enter number of active crew members (e.g. 6): ").strip()
        crew_count = int(raw_crew) if raw_crew else 6
        
        raw_warp = input("  Enter warp factor (1.0 to 9.9, default 3.0): ").strip()
        warp_speed = float(raw_warp) if raw_warp else 3.0
        
        raw_shields = input("  Enter current Shield Energy (0-250, default 200): ").strip()
        shields = float(raw_shields) if raw_shields else 200.0
        
        raw_armor = input("  Enter current Hull Armor (0-250, default 220): ").strip()
        armor = float(raw_armor) if raw_armor else 220.0
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
    
    # Call imported helper for fuel calculation (Liang 6.5 - positional & keyword)
    fuel_needed = calculate_fuel_burn(distance_ly, ship_mass, engine_efficiency=0.90)
    
    # Call student function for warp flight time (Liang 6.9 - default argument)
    travel_years = calculate_warp_travel_time(distance_ly, warp_factor=warp_speed)
    travel_days = travel_years * 365.25
    
    # Call student function for crew provisions (Liang 6.10 - multiple returns)
    food_kg, water_l, o2_kg = provision_crew_supplies(crew_count, max(1, int(travel_days)))
    
    # Call student function for risk evaluation (Liang 6.10 - multiple returns)
    risk_score, risk_tier, is_approved = evaluate_mission_risk(distance_ly, crew_count, anomaly_index=1.2)
    
    # Call imported helper for hull integrity assessment (Liang 6.7/6.10)
    hull_pct, hull_code, hull_alert = assess_hull_integrity(shields, armor)
    
    # --------------------------------------------------------------------------
    # Step 3: Demonstrate Mutable Cargo List Loading (Pass-by-Reference - Liang 6.6)
    # --------------------------------------------------------------------------
    manifest = ["Emergency Beacon", "First Aid Nanokits"]
    print(f"\n  Initial Manifest: {manifest}")
    load_cargo_manifest(manifest, "Cryo-Stasis Pods")
    load_cargo_manifest(manifest, "Sub-Space Transponder")
    print(f"  Updated Manifest (after pass-by-reference calls): {manifest}")
    
    # Increment global dispatch counter (Liang 6.8)
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
    print(f"Estimated Travel Time:   {travel_years:.2f} Earth Years ({travel_days:,.0f} days)")
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
