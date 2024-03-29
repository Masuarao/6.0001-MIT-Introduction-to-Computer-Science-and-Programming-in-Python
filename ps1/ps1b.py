# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 18:23:46 2024

@author: Wilson
"""
import sys

def Savings_Next_Month(savings_this_month,portion_saved,annual_salary, 
                       interest_rate):
    # Calculate savings plus interest first 
    savings_next_month = savings_this_month*(1+interest_rate/12)
    
    # Add salary savings
    savings_next_month = savings_next_month + annual_salary/12*portion_saved
    
    return savings_next_month

def Input_Verifier(value):
    if value <= 0:
        print("Please enter a positive value!")
        sys.exit()

        

# Initialise Variables   
total_cost = 0          # Cost of dream home  
annual_salary = 0       # Annual Salary
current_savings = 0     # Your current savings
portion_saved = 0       # Portion of salary saved each month for downpayment
months = 0              # Months needed to save for dream home downpayment
semi_annual_raise = 0   # Percentage wages increased per 6 month

# Set Variables
portion_down_payment = 0.25     # Percentage cost of downpayment @ 25%
r = 0.04                        # Savings annual return rate     @ 4%

# Receive user inputs
annual_salary = input("Enter your annual salary: ")
annual_salary = int(annual_salary)      # Convert user input to integer
Input_Verifier(annual_salary)           # Salary has to be non-negative

portion_saved = input("Enter the percent of your salary to save, as a decimal" \
                      + ": ")
portion_saved = float(portion_saved)    # Convert user input to float
Input_Verifier(portion_saved)           # Portion saved must be non-negative

total_cost = input("Enter the cost of your dream home: ")
total_cost = int(total_cost)            # Convert user input to integer
Input_Verifier(total_cost)              # Total cost must be positive

semi_annual_raise = input("Enter the cost of your semi-annual raise, as a decimal: ")
semi_annual_raise = float(semi_annual_raise)    # Convert input to float
Input_Verifier(semi_annual_raise)               # Require a positive raise increase

# Count number of months
while current_savings < (total_cost*portion_down_payment):
    months += 1     # Months incremented as long as savings is smaller than
                    # the downpayment 
                    
    # Call function to calculate next month's savings
    current_savings = Savings_Next_Month(current_savings, portion_saved, 
                                         annual_salary, r)
    # Get a raise next month after every 6 months
    if (months%6 == 0):
        annual_salary = annual_salary*(1+semi_annual_raise)

# Display number of months needed to the user 
print("Number of months:",months)
    