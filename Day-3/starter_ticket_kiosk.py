# ==============================================================================
# Course: Python Programming (Session 3)
# Lab Activity: Adventure Island — Smart Ticket & Ride Kiosk
# Student Name: [YOUR NAME HERE]
# Date: [TODAY'S DATE]
# Description:
#   An automated ticketing and safety check kiosk for a theme park.
#   Uses concepts from Chapter 4 (Selections / Conditionals):
#   - Relational Operators (==, !=, <, <=, >, >=)
#   - One-Way if Statements
#   - Two-Way if-else Statements
#   - Multi-Way if-elif-else Statements
#   - Nested if Statements
#   - Random number generation with random.randint()
#
#   *** IMPORTANT RULE FOR TODAY'S LAB ***
#   Do NOT use logical operators (and, or, not) since we have not covered them yet.
#   Use nested if statements or cascading if-elif-else structures instead!
# ==============================================================================

import random

# ------------------------------------------------------------------------------
# STEP 1: Named Constants
# Define standard pricing constants and safety guidelines
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
# Prompt the user for:
# - Visitor's name (str)
# - Age (int)
# - Height in inches (float)
# - Is this a Matinee visit before 2:00 PM? ("yes" / "no")
# ------------------------------------------------------------------------------
visitor_name = input("Enter visitor name: ")
age = int(input("Enter age: "))
height = float(input("Enter height in inches: "))
is_matinee = input("Are you visiting before 2:00 PM? (yes/no): ").lower()

# ------------------------------------------------------------------------------
# STEP 3: Multi-Way 'if-elif-else' — Ticket Tier & Base Pricing
# Determine the visitor's category and base ticket price based on age:
# - Age under 12: Category = "Child Pass", Base Price = CHILD_PRICE
# - Age under 18: Category = "Youth / Student Pass", Base Price = TEEN_PRICE
# - Age under 65: Category = "General Adult Pass", Base Price = ADULT_PRICE
# - Age 65 and older: Category = "Senior Gold Pass", Base Price = SENIOR_PRICE
# ------------------------------------------------------------------------------
# TODO: Write the multi-way if-elif-else structure to set 'category' and 'base_price'
category = ""
base_price = 0.0

# YOUR CODE HERE (replace the pass):
pass


# ------------------------------------------------------------------------------
# STEP 4: Nested 'if' Statements — Matinee Early-Bird Discount
# If it is a Matinee visit (is_matinee == "yes"):
#   - For Adults (category == "General Adult Pass"), give a $10.00 discount!
#   - For Youth / Student (category == "Youth / Student Pass"), give a $5.00 discount!
#   - Children and Seniors already have discounted rates, so give no additional matinee discount.
# If is_matinee != "yes":
#   - No matinee discount applies ($0.00).
#
# NOTE: Do NOT use the 'and' operator! Use a nested if structure:
# Outer 'if': checks if is_matinee == "yes"
#   Inner 'if/elif/else': checks the category and applies discount!
# ------------------------------------------------------------------------------
# TODO: Implement the nested discount logic to set 'discount_amount'
discount_amount = 0.0

# YOUR CODE HERE:


# Compute final ticket price after discount
final_ticket_price = base_price - discount_amount


# ------------------------------------------------------------------------------
# STEP 5: Two-Way 'if-else' — Safety Check for The Cyclone Roller Coaster
# Check if visitor meets the minimum height (MIN_HEIGHT_INCHES = 48 inches):
# - If height >= MIN_HEIGHT_INCHES:
#     roller_coaster_status = "APPROVED: Eligible to ride the Cyclone Coaster!"
# - Otherwise:
#     roller_coaster_status = "RESTRICTED: Under 48 inches. Eligible for Kiddie Land rides only."
# ------------------------------------------------------------------------------
# TODO: Write the two-way if-else statement for roller_coaster_status
roller_coaster_status = ""

# YOUR CODE HERE:


# ------------------------------------------------------------------------------
# STEP 6: One-Way 'if' Statement — Minor Supervision Notice
# If visitor is under 12 years old:
#   Set supervision_notice to "NOTICE: Visitors under 12 must be accompanied by an adult."
# (If not under 12, supervision_notice stays empty "")
# ------------------------------------------------------------------------------
supervision_notice = ""

# TODO: Write a one-way if statement:
# YOUR CODE HERE:


# ------------------------------------------------------------------------------
# STEP 7: Random Lucky Scratcher / Door Prize
# Adventure Island gives every guest a random lucky number from 1 to 4!
# - If lucky_number == 1: prize = "FREE Popcorn Coupon!"
# - If lucky_number == 2: prize = "FREE Souvenir Drink Cup!"
# - If lucky_number == 3: prize = "FREE Arcade Token Pack!"
# - If lucky_number == 4: prize = "Better luck next visit!"
# ------------------------------------------------------------------------------
# Generate a random integer between 1 and 4 inclusive:
lucky_number = random.randint(1, 4)
prize = ""

# TODO: Write an if-elif-else structure to set 'prize' based on 'lucky_number':
# YOUR CODE HERE:


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
print(f"Base Admission:       ${base_price:.2f}")
print(f"Early-Bird Discount: -${discount_amount:.2f}")
print(f"Final Total Due:      ${final_ticket_price:.2f}")
print("-" * 60)
print(f"Cyclone Coaster:      {roller_coaster_status}")

# One-way check for supervision notice display
if supervision_notice != "":
    print(f"Safety Alert:         {supervision_notice}")

print(f"Lucky Spin (Rolled {lucky_number}): {prize}")
print("=" * 60)
print("       Enjoy your day of thrills and excitement! 🎢")
print("=" * 60)
