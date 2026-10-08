# ==============================================================================
# Course: Python Programming (Session 2)
# Lab Activity: Smart Cashier — Minimum Change Breakdown (Section 2.9)
# Reference Solution
# Topics: Liang Chapter 2 (Sections 2.1 – 2.12)
# ==============================================================================

# ------------------------------------------------------------------------------
# STEP 1: Define Named Constants (Section 2.7)
# ------------------------------------------------------------------------------
CENTS_PER_DOLLAR = 100
CENTS_PER_QUARTER = 25
CENTS_PER_DIME = 10
CENTS_PER_NICKEL = 5

print("=" * 52)
print("           SMART CASHIER CHANGE ASSISTANT")
print("=" * 52)

# ------------------------------------------------------------------------------
# STEP 2: Console Input & Type Conversions (Sections 2.3, 2.12)
# ------------------------------------------------------------------------------
item_name = input("Enter item or service name: ")
bill_total = float(input("Enter bill amount ($): "))
cash_given = float(input("Enter cash received ($): "))

# ------------------------------------------------------------------------------
# STEP 3: Calculate Change Due & Convert to Cents
# ------------------------------------------------------------------------------
change_due = cash_given - bill_total

# Convert to whole cents to avoid binary float precision issues
remaining_cents = int(round(change_due * 100))

print("\n" + "-" * 52)
print(f"Receipt for:      {item_name}")
print(f"Bill Total:       ${bill_total:8.2f}")
print(f"Cash Received:    ${cash_given:8.2f}")
print(f"Change Due:       ${change_due:8.2f} ({remaining_cents} total cents)")
print("-" * 52)

# ------------------------------------------------------------------------------
# STEP 4: Compute Currency Breakdown with // and %= (Sections 2.8, 2.9, 2.11)
# ------------------------------------------------------------------------------
# 1. Dollars
num_dollars = remaining_cents // CENTS_PER_DOLLAR
remaining_cents %= CENTS_PER_DOLLAR

# 2. Quarters
num_quarters = remaining_cents // CENTS_PER_QUARTER
remaining_cents %= CENTS_PER_QUARTER

# 3. Dimes
num_dimes = remaining_cents // CENTS_PER_DIME
remaining_cents %= CENTS_PER_DIME

# 4. Nickels
num_nickels = remaining_cents // CENTS_PER_NICKEL
remaining_cents %= CENTS_PER_NICKEL

# 5. Pennies (whatever is left)
num_pennies = remaining_cents

# ------------------------------------------------------------------------------
# STEP 5: Display Summary
# ------------------------------------------------------------------------------
print("OPTIMAL CHANGE BREAKDOWN:")
print(f"  • One-Dollar Bills:  {num_dollars:3d}  (${num_dollars * 1.00:6.2f})")
print(f"  • Quarters (25¢):    {num_quarters:3d}  (${num_quarters * 0.25:6.2f})")
print(f"  • Dimes    (10¢):    {num_dimes:3d}  (${num_dimes * 0.10:6.2f})")
print(f"  • Nickels   (5¢):    {num_nickels:3d}  (${num_nickels * 0.05:6.2f})")
print(f"  • Pennies   (1¢):    {num_pennies:3d}  (${num_pennies * 0.01:6.2f})")
print("=" * 52)
total_coins = num_quarters + num_dimes + num_nickels + num_pennies
print(f"Total Coins Dispensed: {total_coins}")
print("Transaction Completed Successfully.")
print("=" * 52)
