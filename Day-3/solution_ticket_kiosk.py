# ==============================================================================
# Course: Python Programming (Session 3)
# Lab Activity: Adventure Island — Smart Ticket & Ride Kiosk
# Reference Solution
# Topics: Chapter 4 (Selections / Conditionals)
# Note: Implemented entirely without logical operators (and, or, not)
#       using nested if and cascading if-elif-else statements.
# ==============================================================================

import random

# ------------------------------------------------------------------------------
# STEP 1: Named Constants
# ------------------------------------------------------------------------------
MIN_HEIGHT_INCHES = 48        # Minimum height required for the Cyclone Roller Coaster
CHILD_PRICE = 20.00           # Ages under 12
TEEN_PRICE = 35.00            # Ages 12 - 17
ADULT_PRICE = 50.00           # Ages 18 - 64
SENIOR_PRICE = 30.00          # Ages 65 and up

print("=" * 60)
print("     🎡 WELCOME TO ADVENTURE ISLAND SMART KIOSK 🎢")
print("=" * 60)

# ------------------------------------------------------------------------------
# STEP 2: Collect Visitor Information
# ------------------------------------------------------------------------------
visitor_name = input("Enter visitor name: ")
age = int(input("Enter age: "))
height = float(input("Enter height in inches: "))
is_matinee = input("Are you visiting before 2:00 PM? (yes/no): ").lower()

# ------------------------------------------------------------------------------
# STEP 3: Multi-Way 'if-elif-else' — Ticket Tier & Base Pricing
# ------------------------------------------------------------------------------
if age < 12:
    category = "Child Pass"
    base_price = CHILD_PRICE
elif age < 18:
    category = "Youth / Student Pass"
    base_price = TEEN_PRICE
elif age < 65:
    category = "General Adult Pass"
    base_price = ADULT_PRICE
else:
    category = "Senior Gold Pass"
    base_price = SENIOR_PRICE

# ------------------------------------------------------------------------------
# STEP 4: Nested 'if' Statements — Matinee Early-Bird Discount
# (Solves multi-condition decision WITHOUT using 'and')
# ------------------------------------------------------------------------------
discount_amount = 0.0

if is_matinee == "yes":
    # Outer condition matched; now check inner condition (ticket category)
    if category == "General Adult Pass":
        discount_amount = 10.00
    elif category == "Youth / Student Pass":
        discount_amount = 5.00
    else:
        discount_amount = 0.00
else:
    discount_amount = 0.00

# Compute final ticket price after discount
final_ticket_price = base_price - discount_amount

# ------------------------------------------------------------------------------
# STEP 5: Two-Way 'if-else' — Safety Check for The Cyclone Roller Coaster
# ------------------------------------------------------------------------------
if height >= MIN_HEIGHT_INCHES:
    roller_coaster_status = "APPROVED: Eligible to ride the Cyclone Coaster!"
else:
    roller_coaster_status = "RESTRICTED: Under 48 inches. Eligible for Kiddie Land rides only."

# ------------------------------------------------------------------------------
# STEP 6: One-Way 'if' Statement — Minor Supervision Notice
# ------------------------------------------------------------------------------
supervision_notice = ""
if age < 12:
    supervision_notice = "NOTICE: Visitors under 12 must be accompanied by an adult."

# ------------------------------------------------------------------------------
# STEP 7: Random Lucky Scratcher / Door Prize
# ------------------------------------------------------------------------------
lucky_number = random.randint(1, 4)

if lucky_number == 1:
    prize = "FREE Popcorn Coupon!"
elif lucky_number == 2:
    prize = "FREE Souvenir Drink Cup!"
elif lucky_number == 3:
    prize = "FREE Arcade Token Pack!"
else:
    prize = "Better luck next visit!"

# ------------------------------------------------------------------------------
# STEP 8: Formatted Output / Kiosk Summary
# ------------------------------------------------------------------------------
print("\n" + "=" * 60)
print("             ADVENTURE ISLAND VISITOR PASS")
print("=" * 60)
print(f"Guest Name:           {visitor_name}")
print(f"Age:                  {age} years old")
print(f"Height:               {height:.1f} inches")
print(f"Ticket Category:      {category}")
print(f"Base Admission:       ${base_price:6.2f}")
print(f"Early-Bird Discount: -${discount_amount:6.2f}")
print(f"Final Total Due:      ${final_ticket_price:6.2f}")
print("-" * 60)
print(f"Cyclone Coaster:      {roller_coaster_status}")

if supervision_notice != "":
    print(f"Safety Alert:         {supervision_notice}")

print(f"Lucky Spin (Rolled {lucky_number}): {prize}")
print("=" * 60)
print("       Enjoy your day of thrills and excitement! 🎢")
print("=" * 60)
