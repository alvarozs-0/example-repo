"""
Financial Calculator 

This program allows the user to choose between two financial calculators:
1. Investment Calculator - calculates total return on investment with simple or compound interest.
2. Bond Calculator - calculates monthly repayments on a home loan.

The user is prompted for relevant inputs, and results are calculated and displayed.
"""


import math

#Pseudocode

#ask the user to enter either "investment" or "bond" from the menu
#if the user enters "investment":
    #ask the user for the amount of money they are depositing
    #ask the user for the interest rate (as a percentage)
    #ask the user for the number of years they plan on investing
    #ask the user to input if they want "simple" or "compound" interest
    #if the user enters "simple"
        #calculate the total amount when simple interest is applied
    #else if the user enters "compound"
        #calculate the total amount when compound interest is applied
    #print the total amount
#else if the user enters "bond":
    #ask the user for the present value of the house
    #ask the user for the interest rate
    #ask the user for the number of months to repay bond
    #calculate how much money the user will have to repay each month
    #print the result
#else 
    #print appropriate error message


# Python code

# Calculator menu
print(
    "Investment - to calculate the amount of interest you'll earn on your investment \n" 
    "Bond       - to calculate the amount you'll have to pay on a home loan.\n"
)
# Ask the user to enter either "investment" or "bond" from the menu
user_choice = input('Enter either "investment" or "bond" from the menu above to proceed: ')
user_choice = user_choice.lower()

# Investment calculator or home loan repayment calculator based on user's selection
if user_choice == "investment":
    # Ask the user for the amount of money they are depositing
    deposit_amount = float(input("Enter the amount of money you are depositing: "))
    # Ask the user for the interest rate (as a percentage)
    interest_rate_percentage  = float(input("Enter the interest rate (as a percentage): "))
    # Get interest_rate = interest_rate_percentage/100
    interest_rate = interest_rate_percentage/100
    # Ask the user for the number of years they plan on investing
    number_of_years = int(input("Enter the number of years you plan on investing: "))
    # Ask the user to input if they want "simple" or "compound" interest
    interest = input('Do you want "simple" or "compound" interest? ')
    interest = interest.lower()

    
    # Calculate simple or compound interest based on user's desire
    if interest == "simple":
        # Calculate total amount when simple interest is applied
        total_amount = deposit_amount*(1+interest_rate*number_of_years)
        print(f"Total amount after {number_of_years} years with a simple interest of {interest_rate_percentage}: {round(total_amount,2)}")

    elif interest == "compound":
        # Calculate total amount when compound interest is applied
        total_amount = deposit_amount*math.pow((1+interest_rate),number_of_years)
        print(f"Total amount after {number_of_years} years with a compound interest of {interest_rate_percentage}: {round(total_amount,2)}")

    else:
        print(f"{interest} is not a valid interest type.")

elif user_choice == "bond":
    # Ask the user for the present value of the house
    house_present_value = float(input("Enter the present value of the house: "))
    # Ask the user for the interest rate
    interest_rate_percentage = float(input("Enter the interest rate (as a percentage): "))
    # Get interest_rate = interest_rate_percentage/100
    interest_rate = interest_rate_percentage/100
    # Ask the user for the number of months to repay bond
    number_of_months = int(input("Enter the number of months you plan to take to repay the bond: "))
    
   
    # Calculate how much money the user will have to repay each month
    monthly_interest_rate = interest_rate/12
    repayment_per_month = (monthly_interest_rate*house_present_value)/(1-(1+monthly_interest_rate)**(-number_of_months))

    # Print the result
    print(f"You will have to repay {round(repayment_per_month,2)} every month for {number_of_months} months")
# Invalid input
else:
    print(f"{user_choice} is not a valid input")