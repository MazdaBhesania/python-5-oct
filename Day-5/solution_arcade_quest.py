# ==============================================================================
# Course: Python Programming (Session 5)
# Lab Activity: RetroArcade — NumberQuest & High-Score Ledger (SOLUTION)
# Instructor / Reference Solution
#
# Description:
#   An interactive retro arcade gaming terminal demonstrating:
#   - Counter-controlled loops & Sentinel-controlled loops (while)
#   - For loops with single-, two-, and three-argument range()
#   - Accumulator patterns (sum, count, average, min, max)
#   - Flow control keywords (break and continue)
#   - Nested loops for rendering a formatted game multiplier matrix
# ==============================================================================

import random

print("=" * 68)
print("       🕹️ WELCOME TO RETROARCADE: NUMBERQUEST & LEDGER 🕹️")
print("=" * 68)


# ------------------------------------------------------------------------------
# STEP 1: Player Registration
# ------------------------------------------------------------------------------
player_name = input("Enter your Arcade Tag / Nickname: ").strip()
print(f"\nWelcome, Player {player_name}! Preparing your game terminal...")


# ------------------------------------------------------------------------------
# STEP 2: MODULE 1 — The NumberQuest Secret Vault Cracker (Liang 5.3)
# ------------------------------------------------------------------------------
print("\n" + "-" * 68)
print(">>> MISSION 1: CRACK THE SECRET NUMBER VAULT (1 to 100)")
print("    You have a maximum of 7 attempts. Choose wisely!")
print("-" * 68)

secret_number = random.randint(1, 100)
MAX_ATTEMPTS = 7

attempts_used = 0
vault_cracked = False
vault_score = 0

while attempts_used < MAX_ATTEMPTS and not vault_cracked:
    guess_input = input(f"Attempt {attempts_used + 1}/{MAX_ATTEMPTS} — Enter guess (1-100): ").strip()
    
    if not guess_input.isdigit():
        print("  Invalid entry! Please enter a whole number.")
        continue
    
    guess = int(guess_input)
    
    # Range check validation using 'continue' to not penalize attempt
    if guess < 1 or guess > 100:
        print("  Out of range! Must be between 1 and 100.")
        continue
    
    attempts_used += 1
    
    if guess < secret_number:
        print("  Too low! ⬆️ Try higher.")
    elif guess > secret_number:
        print("  Too high! ⬇️ Try lower.")
    else:
        vault_cracked = True
        print(f"  🎉 BINGO! You cracked the vault in {attempts_used} attempt(s)!")
        vault_score = (MAX_ATTEMPTS - attempts_used + 1) * 150
        break

if not vault_cracked:
    print(f"  🔒 Vault lockdown! The secret number was {secret_number}.")


# ------------------------------------------------------------------------------
# STEP 3: MODULE 2 — Sentinel-Controlled Daily Score Ledger (Liang 5.5)
# ------------------------------------------------------------------------------
print("\n" + "-" * 68)
print(">>> MISSION 2: ARCADE ROUNDS LEDGER (Sentinel = -1)")
print("    Enter your previous game scores. Type -1 when finished.")
print("-" * 68)

total_points = 0.0
games_played = 0
high_score = 0.0
low_score = 0.0

while True:
    entry = input("  Enter round score (-1 to stop): ").strip()
    
    try:
        val = float(entry)
    except ValueError:
        print("    Invalid number! Please re-enter.")
        continue
    
    if val == -1:
        break  # Sentinel encountered: exit loop
    
    if val < 0:
        print("    Negative scores are not permitted. Skipping.")
        continue
    
    # Update accumulators
    total_points += val
    games_played += 1
    
    # Initialize high/low on first valid entry, otherwise compare
    if games_played == 1:
        high_score = val
        low_score = val
    else:
        if val > high_score:
            high_score = val
        if val < low_score:
            low_score = val


# ------------------------------------------------------------------------------
# STEP 4: Compute Statistics (Average & Zero-Guard)
# ------------------------------------------------------------------------------
if games_played > 0:
    average_score = total_points / games_played
else:
    average_score = 0.0


# ------------------------------------------------------------------------------
# STEP 5: MODULE 3 — XP Multiplier Matrix (Nested Loops - Liang 5.7)
# ------------------------------------------------------------------------------
print("\n" + "-" * 68)
print(">>> MISSION 3: XP MULTIPLIER MATRIX (Nested Loops)")
print("-" * 68)

# Header
print("Tier \\ Stage   |  Stage 1  |  Stage 2  |  Stage 3  |  Stage 4")
print("-" * 58)

tier_names = {1: "Tier 1 (Brz)", 2: "Tier 2 (Sil)", 3: "Tier 3 (Gld)"}

for tier in range(1, 4):
    label = tier_names.get(tier, f"Tier {tier}      ")
    print(f"{label}  |", end="")
    for stage in range(1, 5):
        xp_points = tier * stage * 25
        print(f"{xp_points:8d}  |", end="")
    print()  # End of row newline


# ------------------------------------------------------------------------------
# STEP 6: Display Final Player Arcade Certificate
# ------------------------------------------------------------------------------
print("\n" + "=" * 68)
print("             RETROARCADE: PLAYER PERFORMANCE SUMMARY")
print("=" * 68)
print(f"Player Tag:           {player_name}")
print(f"Vault Quest Status:   {'CRACKED! 🎉' if vault_cracked else 'LOCKED 🔒'}")
print(f"Attempts Used:        {attempts_used} / {MAX_ATTEMPTS}")
print(f"Secret Target:        {secret_number}")
print(f"Vault Quest Points:   {vault_score:,} pts")
print("-" * 68)
print(f"Ledger Rounds Logged: {games_played} round(s)")
print(f"Total Ledger Score:   {total_points:,.1f} pts")
print(f"Average Round Score:  {average_score:,.2f} pts")
if games_played > 0:
    print(f"Highest Round Score:  {high_score:,.1f} pts")
    print(f"Lowest Round Score:   {low_score:,.1f} pts")
else:
    print("Highest / Lowest:     N/A (No rounds logged)")
grand_total = vault_score + total_points
print("-" * 68)
print(f"GRAND TOTAL POINTS:   {grand_total:,.1f} pts")
print("=" * 68)
