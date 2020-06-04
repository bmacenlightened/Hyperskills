import math
import sys

args = sys.argv
active_args = {}

for a in range(1, len(args)):
    splits = args[a].split("=")
    if splits[0] in ('--payment', '--interest', '--principal'):
        active_args[splits[0]] = float(splits[1])
    elif splits[0] == '--periods':
        active_args[splits[0]] = int(splits[1])
    else:
        active_args[splits[0]] = splits[1]

mode = active_args.get('--type')
payment = active_args.get('--payment', 0)
interest = active_args.get('--interest', 0)
principal = active_args.get('--principal', 0)
periods = active_args.get('--periods', 0)
nominal_interest = interest / 12 / 100

if mode == "annuity":
    if principal and payment and interest:
        periods = math.ceil(math.log(payment / (payment - nominal_interest * principal), 1 + nominal_interest))
        years = math.ceil(periods) // 12
        months = math.ceil(periods) % 12
        if months == 0:
            print(f'You need {years} years to repay this credit!')
        else:
            print(f'You need {years} years and {months} months to repay this credit!')
        print(f'Overpayment = {math.ceil(((years * 12 + months) * payment) - principal)}')
    elif principal and periods and interest:
        annuity = math.ceil(principal * nominal_interest * pow((1 + nominal_interest), periods) / (pow((1 + nominal_interest), periods) - 1))
        print(f'Your annuity payment = {annuity}!')
        print(f'Overpayment = {math.ceil((periods * annuity) - principal)}')
    elif payment and periods and interest:
        principal = math.ceil(payment / (nominal_interest * pow((1 + nominal_interest), periods) / (pow((1 + nominal_interest), periods) - 1)))
        print(f'Your credit principal = {principal}!')
        print(f'Overpayment = {math.ceil((periods * payment) - principal)}')
    else:
        print("Incorrect parameters")
elif mode == 'diff':
    if payment:
        print("Incorrect parameters")
    elif principal and periods and interest:
        overpayment = - principal
        for i in range(1, periods + 1):
            payment = math.ceil(principal / periods + nominal_interest * (principal - principal * (i - 1) / periods))
            print(f"Month {i}: paid out {payment}")
            overpayment += payment
        print(f"\nOverpayment = {int(overpayment)}")
    else:
        print("Incorrect parameters")
else:
    print('Incorrect parameters')