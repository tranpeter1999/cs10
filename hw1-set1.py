#Peter Tran
#11098
#This program tells the user how much of each ingredient the user needs to make X cookies

#recipe
sugar = 1.5;
butter = 1.0;
flour = 2.75;

#input
targetCookies = float(input("How many cookies would you like to make? "));

#output
print("To make", targetCookies, "cookies, you will need: ");
print("{:.2f} cups of sugar".format(targetCookies/48*sugar));
print("{:.2f} cups of butter".format(targetCookies/48*butter));
print("{:.2f} cups of flour".format(targetCookies/48*flour));

#termination
print("\n\nPress enter to quit the program");


##run1
##How many cookies would you like to make? 56
##To make 56.0 cookies, you will need: 
##1.75 cups of sugar
##1.17 cups of butter
##3.21 cups of flour
##
##
##Press enter to quit the program

##run2
##How many cookies would you like to make? 0
##To make 0.0 cookies, you will need: 
##0.00 cups of sugar
##0.00 cups of butter
##0.00 cups of flour
##
##
##Press enter to quit the program

##run3
##How many cookies would you like to make? 10000000
##To make 10000000.0 cookies, you will need: 
##312500.00 cups of sugar
##208333.33 cups of butter
##572916.67 cups of flour
##
##
##Press enter to quit the program

##run4
##How many cookies would you like to make? -10
##To make -10.0 cookies, you will need: 
##-0.31 cups of sugar
##-0.21 cups of butter
##-0.57 cups of flour
##
##
##Press enter to quit the program

##run5
##How many cookies would you like to make? 48
##To make 48.0 cookies, you will need: 
##1.50 cups of sugar
##1.00 cups of butter
##2.75 cups of flour
##
##
##Press enter to quit the program
