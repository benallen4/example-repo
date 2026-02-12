# Based on user inputs this will calculate the amount after investment or the amount repayed each month
import math
input_finance_type = input("Are you seeking Investment or Bond advice? ")
finance_type = input_finance_type.lower()
print("You have selected " + finance_type)
# Code for when they select the investment option
if finance_type == "investment":
    principal = float(input("Please enter the initial deposit amount : "))
    entered_interest_rate = float(input("Please enter the interest rate : "))
    interest_rate = entered_interest_rate / 100
    investment_period = int(input("Please enter the number of years you plan on investing : "))

    # We will now run the calculations based on the user input of interest type
    input_interest_type = input("Is this investment with Simple or Compound interest? ")
    interest_type = input_interest_type.lower()
    print("You have selected " + interest_type)
    if interest_type == "simple":
        total = principal * (1 + interest_rate * investment_period)
        print(f"You will have ${total: .2f} after {int(investment_period)} years")
    elif interest_type == "compound":
        total = principal * math.pow((1 + interest_rate), investment_period)
        print(f"You will have ${total: .2f} after {int(investment_period)} years")
    else:
        print("Wrong information entered. Please rerun the program and enter either 'Simple' or 'Compound'")

# Code for when they select the bonds option
elif finance_type == "Bond" or finance_type == "bond" or finance_type == "BOND":
    current_value = float(input("Please enter the current value of your home : "))
    entered_interest_rate = float(input("Please enter the interest rate : "))
    monthly_interest_rate = (entered_interest_rate / 100) / 12
    repayment_time = int(input("Please enter the number of months for this bond : "))
    repayment = (monthly_interest_rate * current_value) / (1 - (1 + monthly_interest_rate) ** (-repayment_time))
    print(f"You will have to repay ${repayment: .2f} per month")

else:
    print("Wrong information entered. Please rerun the program and enter either 'Investment' or 'Bond'")