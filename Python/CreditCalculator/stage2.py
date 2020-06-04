credit_principal = 'Credit principal: 1000'
final_output = 'The credit has been repaid!'
first_month = 'Month 1: paid out 250'
second_month = 'Month 2: paid out 250'
third_month = 'Month 3: paid out 500'

# write your code here
months = 0
payment = 0
principal = int(input("Enter the credit principal:\n"))
select = input('What do you want to calculate?\ntype "m" - for count of months,\ntype "p" - for monthly payment\n')
if select == "m":
    payment = int(input("Enter monthly payment:\n"))
    months = (principal / payment)
    if principal % payment != 0:
        months = int(months) + 1
    if months == 1:
        print("It takes " + str(months) + " month to repay the credit")
    else:
        print("It takes " + str(months) + " months to repay the credit")
elif select == "p":
    months = int(input("Enter count of months:\n"))  
    payment = int(principal/months)
    if principal % months == 0:
        print("Your monthly payment = " + str(payment))
    else:
        payment = payment + 1
        last_payment = principal - (payment * (months - 1))
        print("Your monthly payment = " + str(payment) + " with last month payment = " + str(last_payment))
