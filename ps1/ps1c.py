# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 12:35:55 2024

@author: Wilson
"""
import sys 

def Input_Verifier(value):
    """ Verifies if input is positive."""
    if value <= 0:
        print("Please enter a positive value!")
        sys.exit()

def Savings_This_Month(savings_this_month,portion_saved,annual_salary, 
                       interest_rate):
    """ Based off 4 financial metrics, calculate savings this month."""
    # Calculate savings plus interest first 
    savings_next_month = savings_this_month*(1+interest_rate/12)
    
    # Add salary savings
    savings_next_month = savings_next_month + annual_salary/12*portion_saved
    
    return savings_next_month

def Final_Savings(annual_salary, semi_annual_raise, annual_return, months, 
                  portion_saved):
    """ Based off 5 financial metrics, calculate savings at the end of savings 
        period"""    
    current_savings = 0         # Initialise current savings    
    for i in range(months):     # Apply a raise every 6 months 
        if (i%6 == 0 and i!=0):
            annual_salary = annual_salary*(1+semi_annual_raise)
        
        # Call function to calculate next month's savings
        current_savings = Savings_This_Month(current_savings, portion_saved, 
                                             annual_salary, annual_return)
        
    return current_savings

def Portion_Saved_Bisection_Search(annual_salary, semi_annual_raise, portion_down_payment,
                  annual_return, total_cost, months):
    # Initialise variables for bisection method computation
    current_portion_integer = int(10000)  # Variable for current portion saved
    upper_portion_integer = int(10000)    # Upper bound for bisection
    lower_portion_integer = 0             # Lower bound for bisection
    
    # Initialise other variables
    portion_saved = float(upper_portion_integer/100)    # Convert bisection integer to float
    downpayment = total_cost*portion_down_payment       # Downpayment
    iterations = 0                                      # Counting the number of iterations
    final_savings = Final_Savings(annual_salary, semi_annual_raise,
                      annual_return, months, portion_saved) # Set final savings using function
    
    while (final_savings > downpayment + 100) or(final_savings < downpayment - 100):
        
        # Runtime Error: Algorithm should mathematically find the value in 13 
        # iterations (log10000/log2). Exit on 14th iteration. 
        if iterations == 14:
            print("It is not possible to pay the down payment in three years.")
            sys.exit()      # Exit the program
        
        # Set current portion saved when final savings lower than downpayment
        if final_savings < downpayment:
            lower_portion_integer = current_portion_integer
            current_portion_integer = int((upper_portion_integer + lower_portion_integer)/2)
            portion_saved = float(current_portion_integer/10000)
            final_savings = Final_Savings(annual_salary, semi_annual_raise,
                              annual_return, months, portion_saved)
        
        # Set current portion saved when final savings higher than downpayment
        elif final_savings > downpayment:
            upper_portion_integer = current_portion_integer
            current_portion_integer = int((upper_portion_integer + lower_portion_integer)/2)
            portion_saved = float(current_portion_integer/10000)
            final_savings = Final_Savings(annual_salary, semi_annual_raise,
                              annual_return, months, portion_saved)
        iterations +=1  # Increment iterations
        
    return [iterations,portion_saved]
        
# Initialise Variables
annual_salary = 0       # Annual Salary
current_savings = 0     # Your current savings
# portion_saved = 0     # Portion of salary saved each month for downpayment
iterations = 0          # Initialise iterations

# Set Variables
semi_annual_raise = 0.07        # Annual raise                   @ 7%
portion_down_payment = 0.25     # Percentage cost of downpayment @ 25%
r = 0.04                        # Savings annual return rate     @ 4%
total_cost = 1000000            # Cost of dream home             @ 1 mil 
months = 36                     # Required months of saving      @ 36 months

# Receive user inputs
annual_salary = input("Enter the starting salary: ")
annual_salary = int(annual_salary)      # Convert user input to integer
Input_Verifier(annual_salary)           # Salary has to be non-negativex

# Call calculation
[iterations,portion_saved] = Portion_Saved_Bisection_Search(annual_salary, semi_annual_raise, portion_down_payment, r , 
              total_cost, months)

# Report calculations
print("Best saving rate:",portion_saved)
print("Steps in bisection search:", iterations)
    
