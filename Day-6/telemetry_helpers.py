# ==============================================================================
# Course: Python Programming
# Session: Day 6 (Chapter 6: Modularizing Code — Liang Section 6.7)
# Module: telemetry_helpers.py
#
# Description:
#   A reusable utility library containing pure functions for deep-space flight
#   calculations, communication latency, and hull integrity diagnostics.
#
#   This module illustrates:
#   - Writing reusable library functions with type hints and docstrings
#   - Default parameters (Liang 6.9)
#   - Returning multiple values as tuples (Liang 6.10)
#   - The 'if __name__ == "__main__":' guard to enable standalone unit testing
#     without executing when imported by other scripts (Liang 6.7).
# ==============================================================================

def calculate_fuel_burn(distance_ly, ship_mass_tons, engine_efficiency=0.85):
    """
    Computes required antimatter fuel in metric tonnes (Liang 6.2, 6.9).
    
    Formula:
        fuel = (distance_ly * ship_mass_tons * 0.04) / engine_efficiency
    
    Parameters:
        distance_ly (float): Travel distance in Light-Years.
        ship_mass_tons (float): Dry mass of the spacecraft in metric tonnes.
        engine_efficiency (float): Engine rating between 0.10 and 1.00 (default: 0.85).
    
    Returns:
        float: Total required fuel in metric tonnes rounded to 2 decimal places.
    """
    if engine_efficiency <= 0:
        engine_efficiency = 0.85  # Fallback safety guard
    
    required_fuel = (distance_ly * ship_mass_tons * 0.04) / engine_efficiency
    return round(required_fuel, 2)


def compute_comm_delay(distance_au, light_speed_au_per_min=0.1207):
    """
    Computes one-way radio communication latency from Earth in minutes.
    
    Parameters:
        distance_au (float): Distance in Astronomical Units (1 AU ~= Sun-Earth distance).
        light_speed_au_per_min (float): Speed of radio/light in AU/min (default: 0.1207).
        
    Returns:
        float: One-way communication delay in minutes.
    """
    if distance_au <= 0:
        return 0.0
    delay_minutes = distance_au / light_speed_au_per_min
    return round(delay_minutes, 2)


def assess_hull_integrity(shield_hp, armor_hp, max_hp=500.0):
    """
    Evaluates current defensive health and returns 3 diagnostic values (Liang 6.10).
    
    Parameters:
        shield_hp (float): Remaining shield energy points.
        armor_hp (float): Remaining physical hull plating points.
        max_hp (float): Nominal maximum combined HP (default: 500.0).
        
    Returns:
        tuple: (health_pct, status_code, alert_level)
            - health_pct (float): Percentage of remaining HP.
            - status_code (str): 'GREEN', 'YELLOW', or 'RED'.
            - alert_level (str): Descriptive status message.
    """
    total_hp = max(0.0, shield_hp + armor_hp)
    health_pct = min(100.0, (total_hp / max_hp) * 100.0)
    
    if health_pct >= 75.0:
        status_code = "GREEN"
        alert_level = "Nominal — All Systems Operational"
    elif health_pct >= 40.0:
        status_code = "YELLOW"
        alert_level = "Warning — Defensive Degradation Detected"
    else:
        status_code = "RED"
        alert_level = "CRITICAL — Shield Collapse & Hull Breach Hazard"
        
    return round(health_pct, 1), status_code, alert_level


def format_mission_header(callsign, sector="Orion Nebula", clearance_level=1):
    """
    Formats a standardized mission header string using keyword/default args.
    """
    border = "=" * 68
    clearance_tags = {1: "STANDARD CADET", 2: "OFFICER", 3: "FLEET ADMIRAL"}
    tier_label = clearance_tags.get(clearance_level, "CONFIDENTIAL")
    
    header = (
        f"{border}\n"
        f"  🛰️ ASTROVOYAGER MISSION CONTROL | SECTOR: {sector.upper()}\n"
        f"  Commander: {callsign} | Security Clearance: LEVEL {clearance_level} ({tier_label})\n"
        f"{border}"
    )
    return header


# ------------------------------------------------------------------------------
# Module Self-Test Guard (Liang Section 6.7)
# Code inside this block executes ONLY when telemetry_helpers.py is run directly.
# When imported into another script, this block is completely skipped!
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    print("[telemetry_helpers.py] Running standalone self-test...")
    
    test_header = format_mission_header("Vanguard-1", sector="Kepler-186", clearance_level=2)
    print(test_header)
    
    fuel = calculate_fuel_burn(distance_ly=4.24, ship_mass_tons=120.0)
    print(f"Test Fuel (Alpha Centauri, 120t ship): {fuel} tonnes")
    
    latency = compute_comm_delay(distance_au=5.2)  # Jupiter distance
    print(f"Test Comm Latency (Jupiter, 5.2 AU): {latency} mins")
    
    pct, code, alert = assess_hull_integrity(shield_hp=120.0, armor_hp=180.0)
    print(f"Test Hull Assessment: {pct}% [{code}] -> {alert}")
    
    print("[telemetry_helpers.py] All standalone unit tests passed successfully!")
