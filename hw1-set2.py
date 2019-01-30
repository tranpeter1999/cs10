#Peter Tran
#1104985
#This program calculates a user's loans

annualInterest = float(input("Enter annual interest rate: "));
numYears = int(input("Enter the number of years: "));
loanAmt = float(input("Enter loan amount: "));

monthlyInterest = annualInterest/1200;
monthlyPay = loanAmt * monthlyInterest / (1 - 1 / (1 + monthlyInterest) ** (numYears*12))

print("The monthly payment is ${:,.2f}".format(monthlyPay));
print("The total payment is ${:,.2f}".format(monthlyPay*numYears*12));

#termination
print("\n\nPress enter to quit the program");

##run1
##Enter annual interest rate: 7.25
##Enter the number of years: 5
##Enter loan amount: 120000.95
##The monthly payment is $2,390.34
##The total payment is $143,420.54
##
##
##Press enter to quit the program

##run2
##Enter annual interest rate: 5
##Enter the number of years: 10
##Enter loan amount: 10000
##The monthly payment is $106.07
##The total payment is $12,727.86
##
##
##Press enter to quit the program

##run3
##Enter annual interest rate: 10
##Enter the number of years: 3
##Enter loan amount: 500
##The monthly payment is $16.13
##The total payment is $580.81
##
##
##Press enter to quit the program

##run4
##Enter annual interest rate: 2
##Enter the number of years: 30
##Enter loan amount: 100000
##The monthly payment is $369.62
##The total payment is $133,063.01
##
##
##Press enter to quit the program

##run5
##Enter annual interest rate: 8
##Enter the number of years: 10
##Enter loan amount: 20000
##The monthly payment is $242.66
##The total payment is $29,118.62
##
##
##Press enter to quit the program
