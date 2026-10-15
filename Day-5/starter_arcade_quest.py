# ==============================================================================
# Course: Python Programming (Session 5)
# Lab Activity: RetroArcade — NumberQuest & High-Score Ledger
# Student Name: [YOUR NAME HERE]
# Date: [TODAY'S DATE]
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
# Prompt for player nickname and starting difficulty level.
# ------------------------------------------------------------------------------
player_name = input("Enter your Arcade Tag / Nickname: ").strip()
print(f"\nWelcome, Player {player_name}! Preparing your game terminal...")


# ------------------------------------------------------------------------------
# STEP 2: MODULE 1 — The NumberQuest Secret Vault Cracker (Liang 5.3)
#
# Mechanics:
#   - The vault generates a hidden number between 1 and 100 inclusive.
#   - The player has a maximum of 7 attempts to guess the secret number.
#   - Use a 'while' or 'for' loop to manage the guessing attempts.
#
# For each attempt:
#   1. Prompt the player for their guess.
#   2. Input validation: If the guess is < 1 or > 100, print "Invalid! 1-100 only."
#      and use 'continue' to re-prompt without wasting an attempt.
#   3. If guess < secret_number: Print "Too low! ⬆️ Try higher."
#   4. If guess > secret_number: Print "Too high! ⬇️ Try lower."
#   5. If guess == secret_number:
#      - Set 'vault_cracked = True'
#      - Announce victory!
#      - 'break' out of the loop immediately!
#
# Bonus:
#   If cracked, score_earned = (7 - attempts_used + 1) * 150 points.
#   If failed, score_earned = 0 points.
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

# TODO: Write the loop for the guessing game
# YOUR CODE HERE:
# Hint: You can use a while loop: while attempts_used < MAX_ATTEMPTS and not vault_cracked:
pass


# ------------------------------------------------------------------------------
# STEP 3: MODULE 2 — Sentinel-Controlled Daily Score Ledger (Liang 5.5)
#
# Mechanics:
#   - The player enters scores achieved in previous arcade rounds.
#   - They enter scores one by one until they enter the SENTINEL value: -1.
#
# Accumulators to track:
#   - total_points: running sum of valid scores
#   - games_played: count of valid scores entered
#   - high_score  : maximum score observed
#   - low_score   : minimum score observed
#
# Flow Control Rule:
#   - If user enters a negative score other than -1 (e.g. -5), print "Invalid score!"
#     and use 'continue' to skip it.
#   - When user enters -1, use 'break' to finish input.
# ------------------------------------------------------------------------------
print("\n" + "-" * 68)
print(">>> MISSION 2: ARCADE ROUNDS LEDGER (Sentinel = -1)")
print("    Enter your previous game scores. Type -1 when finished.")
print("-" * 68)

total_points = 0.0
games_played = 0
high_score = 0.0
low_score = 0.0

# TODO: Write the sentinel-controlled while loop to accumulate scores
# YOUR CODE HERE:
pass


# ------------------------------------------------------------------------------
# STEP 4: Compute Statistics (Average & Zero-Guard)
#
# Guard against ZeroDivisionError:
# If games_played > 0:
#     average_score = total_points / games_played
# Else:
#     average_score = 0.0
# ------------------------------------------------------------------------------
# TODO: Calculate 'average_score'
# YOUR CODE HERE:
average_score = 0.0


# ------------------------------------------------------------------------------
# STEP 5: MODULE 3 — XP Multiplier Matrix (Nested Loops - Liang 5.7)
#
# Mechanics:
#   Display a formatted XP Reward Matrix showing potential points across:
#   - 3 Difficulty Tiers (Rows 1 to 3: Bronze, Silver, Gold)
#   - 4 Game Stages     (Cols 1 to 4: Stage 1 to 4)
#   Formula for cell value: tier * stage * 25
#
# Format:
#   Tier \ Stage | Stage 1 | Stage 2 | Stage 3 | Stage 4
#   Tier 1 (Brz) |      25 |      50 |      75 |     100
#   ...
# ------------------------------------------------------------------------------
print("\n" + "-" * 68)
print(">>> MISSION 3: XP MULTIPLIER MATRIX (Nested Loops)")
print("-" * 68)

# Header
print("Tier \\ Stage   |  Stage 1  |  Stage 2  |  Stage 3  |  Stage 4")
print("-" * 58)

# TODO: Write outer loop for tiers (1 to 3) and inner loop for stages (1 to 4)
# YOUR CODE HERE:
pass


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
