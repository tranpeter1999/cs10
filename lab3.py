#Peter Tran
#1104985
#Lab 3: Functions and Strings

#1

def texas():
	'''Prints Texas has X birds'''
	birds = 5000
	print("Texas has", birds, "birds")
	
def California():
	'''Prints California has X birds'''
	birds = 8000
	print("California has", birds, "birds")

def main():
	texas()
	California()
	
	help(texas)
	help(California)
	
	print(texas.__doc__)
	print(California.__doc__)


if __name__ == "__main__":
	main()
	
#2

def show_interest(principal:float = 10000.00, rate:float = 0.01, periods:int = 10):
	'''This calculates and displays interest using 3 arguments'''
	interest = principal*rate*periods
	print("The simple interest will be ${:.2f}".format(interest))

def main():
	#without default args
	show_interest(10000.00,0.01,10)
	
	#with default args
	show_interest()


if __name__ == "__main__":
	main()
	
#3

def getData():
	return float(input("Enter length: ")),float(input("Enter height: "))
	
def trigArea(l,h):
	return l*h/2
	
def displayData(l,h,a):
	print("The length is {:}\nThe height is {:}\nThe area is {:}".format(l,h,a))

def main():
	length,height = getData()
	
	area = trigArea(length,height)
	
	displayData(length,height,area)

if __name__ == "__main__":
	main()
	
	
#4

def get_sales():
	return float(input("Input sales: "))
	
def get_advanced_pay():
	return float(input("Input advanced pay: "))

def determine_comm_rate(s):
	if s < 10000.00:
		return .10
	if s <= 14999.99:
		return .12
	if s <= 17999.99:
		return .14
	if s <= 21999.99:
		return .16
	return .18

def main():
	#Get the amount of sales from user
	sales = get_sales()
	
	#Get the amount of advanced pay from user
	advanced_pay = get_advanced_pay()
	
	#Determine the commission rate
	comm_rate = determine_comm_rate(sales)
	
	#Calculate the pay
	pay = sales*comm_rate - advanced_pay
	
	#Display the amount of pay.
	print("They pay is ${:.2f}".format(pay))
	
	#Determine whether the pay is negative
	if pay < 0:
		print("The salesperson must reimburse\nthe company.")
		
if __name__ == "__main__":
	main()
	
#5

def getInitials(name:str):
	list = name.split()
	initial = ""
	
	for i in list:
		initial = initial + i[:1] + "." 
		
	return initial

def main():
	name = input("Enter your full name!")
	
	print("Your initials are", getInitials(name))

if __name__ == "__main__":
	main()
	
#6
def string_total(num:str):
	sum = 0
	
	for i in range(len(num)):
		sum = sum + int(num[i])
		
	return sum
	
def main():
	number_string = input("enter a sequence of digits with nothing separating them: ")
	
	total = string_total(number_string)
	
	print("The total of the digits in the string you entered is", total)

if __name__ == "__main__":
	main()