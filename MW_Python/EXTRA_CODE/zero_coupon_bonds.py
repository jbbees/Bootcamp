# -*- coding: utf-8 -*-
"""
Zero-Coupon Bond Valuation.

This script will calculate the present value of zero-coupon bonds, compare the present value to the price of the bond, and determine the corresponding action (buy, not buy, neutral).
"""

# @TODO: Create a function to calculate present value
def present_value(future_value, discount_rate, compounding_periods, years):
    present_value = future_value / ((1 + (discount_rate/compounding_periods)) ** (compounding_periods * years))
    return present_value
    

# Intialize the zero-coupon bond parameters, assume compounding period is equal to 1
price = str(input(f'what is the price?'))
future_value = str(input(f'what is the FV?'))
discount_rate = str(input(f'what is the discount rate?'))
compounding_periods = str(input(f'what are the periods?'))
years = str(input(f'what are the years?'))

# @TODO: Call the calculate_present_value() function and assign to a variables
 
# @TODO: Determine if the bond is worth it
price = int(price)
future_value = int(future_value)
discount_rate = float(discount_rate)
compounding_periods = int(compounding_periods)
years = int(years)

bond_value = present_value(future_value, discount_rate, compounding_periods, years)
print(f'we have calculated a bond value of {bond_value}')
def smart_investment(price, bond_value):
    if price < bond_value:
        print(f'smart investment')
    elif price == bond_value:
        print(f"the investment won't return profit, or loss")
    else:
        print(f'this is a stupid investment')
print(smart_investment(price, bond_value))