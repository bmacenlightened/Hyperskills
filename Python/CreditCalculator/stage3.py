import math
calc = input('What do you want to calculate?\ntype "n" - for count of months,\ntype "a" - for annuity monthly payment,\ntype "p" - for credit principal:')
principal = 0
monthly = 0
periods = 0
interest = 0
if calc == 'n' or calc == 'a':
    principal = float(input("Enter credit principal:\n"))
if calc == 'n' or calc == 'p':
    monthly = float(input("Enter monthly payment:\n"))
if calc == 'a' or calc == 'p':
    periods = int(input("Enter count of periods:\n"))
interest = float(input("Enter credit interest:\n"))

nominal_interest = interest / (100 * 12)
if periods == 0:
    periods = math.ceil(math.log(monthly/(monthly-nominal_interest*principal),1+nominal_interest))
    year = int(periods/12)
    month = periods % 12
    if month == 1:
        print(f"You need {year} years and {month} month to repay this credit!")
    else:
        print(f"You need {year} years and {month} months to repay this credit!")
if monthly == 0:
    x = (1 + nominal_interest) ** periods
    annuity = math.ceil(principal * ((nominal_interest * x) / (x - 1)))
    print(f"Your annuity payment = {annuity}!")
if principal == 0:
    x = (1 + nominal_interest) ** periods
    principal = monthly / ((nominal_interest * x) / (x - 1))
    print(f"Your credit principal = {principal}!")
    