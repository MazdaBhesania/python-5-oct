# ==============================================================================
# Course: Python Programming (Session 2)
# Lab Activity: Smart Cashier — Minimum Change Breakdown (Section 2.9)
# Student Name: [YOUR NAME HERE]
# Date: [TODAY'S DATE]
# Description:
#   A cashier assistant program that computes change due and breaks it down
#   into the minimum number of dollars, quarters, dimes, nickels, and pennies.
#   Uses concepts from Chapter 2 (Sections 2.1 – 2.12):
#   - Named Constants (2.7)
#   - input() & float() conversion (2.3, 2.12)
#   - Arithmetic operators: // and % (2.8, 2.9)
#   - Augmented assignment operators (2.11)
# ==============================================================================

# ------------------------------------------------------------------------------
# STEP 1: Define Named Constants (Section 2.7)
# Tip: Use UPPER_CASE naming convention
# ------------------------------------------------------------------------------
CENTS_PER_DOLLAR = 100
CENTS_PER_QUARTER = 25
CENTS_PER_DIME = 10
CENTS_PER_NICKEL = 5

print("=" * 50)
print("          SMART CASHIER CHANGE ASSISTANT")
print("=" * 50)

# ------------------------------------------------------------------------------
# STEP 2: Read Input from Console (Section 2.3 & 2.12)
# Prompt user for item name, bill total ($), and cash tendered ($)
# Note: input() returns a string, so convert amounts to float!
# ------------------------------------------------------------------------------
item_name = input("Enter item or service name: ")

# TODO: Convert the inputs below to float()
bill_total = float(input("Enter bill amount ($): "))
cash_given = float(input("Enter cash received ($): "))

# ------------------------------------------------------------------------------
# STEP 3: Calculate Change Due
# Compute: change_due = cash_given - bill_total
# ------------------------------------------------------------------------------
change_due = cash_given - bill_total

# To avoid floating-point rounding inaccuracies (e.g., 0.1 + 0.2 != 0.3),
# convert total change into whole cents (an integer):
# TODO: Multiply change_due by 100, round it, and cast to int():
remaining_cents = int(round(change_due * 100))

print("\n" + "-" * 50)
print(f"Receipt for:   {item_name}")
print(f"Bill Total:    ${bill_total:.2f}")
print(f"Cash Received: ${cash_given:.2f}")
print(f"Change Due:    ${change_due:.2f} ({remaining_cents} total cents)")
print("-" * 50)

# ------------------------------------------------------------------------------
# STEP 4: Compute Breakdown using Floor Division (//) and Modulo (%) (Section 2.8, 2.9)
# ------------------------------------------------------------------------------

# 1. Dollars ($1.00 = 100 cents)
num_dollars = remaining_cents // CENTS_PER_DOLLAR
remaining_cents = remaining_cents % CENTS_PER_DOLLAR

# 2. Quarters (25 cents)
# TODO: Calculate num_quarters using // and update remaining_cents using % (or %=)
num_quarters = remaining_cents // CENTS_PER_QUARTER
remaining_cents %= CENTS_PER_QUARTER

# 3. Dimes (10 cents)
# TODO: Calculate num_dimes using // and update remaining_cents using % (or %=)
num_dimes = 0        # Replace with your formula
# remaining_cents = ...

# 4. Nickels (5 cents)
# TODO: Calculate num_nickels using // and update remaining_cents using % (or %=)
num_nickels = 0      # Replace with your formula
# remaining_cents = ...

# 5. Pennies (1 cent)
# TODO: Whatever remaining_cents are left are pennies:
num_pennies = 0      # Replace with your formula


# ------------------------------------------------------------------------------
# STEP 5: Display Coin Breakdown
# ------------------------------------------------------------------------------
print("COIN BREAKDOWN:")
print(f"  • One-Dollar Bills / Coins: {num_dollars}")
print(f"  • Quarters (25¢):           {num_quarters}")
print(f"  • Dimes    (10¢):           {num_dimes}")
print(f"  • Nickels   (5¢):           {num_nickels}")
print(f"  • Pennies   (1¢):           {num_pennies}")
print("=" * 50)
print("Thank you for your business!")
