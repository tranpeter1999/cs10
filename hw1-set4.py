#Peter Tran
#1104985
#This program will calculate the bill for an item

#input
quant = int(input("Enter amount sold: "));
val = float(input("Enter item cost: $"));
disc = float(input("Enter discount: %"));
tax = float(input("Enter tax: %"));

#calc
amt = quant*val;
discAmt = amt*disc/100;
subtotal = amt-discAmt;
taxAmt = subtotal*tax/100;
totalAmt = subtotal + taxAmt;

#output
print("*********BILL*********");
print("{:20}{:20,.2f}".format("Quantity Sold:",quant));
print("{:20}{:20,.2f}".format("Price per Item:",val));
print("\n" + " "*20 + "-"*20);
print("{:20}{:20,.2f}".format("Amount:",amt));
print("{:20}-{:19,.2f}".format("Discount:",discAmt));
print("\n" + " "*20 + "-"*20);
print("{:20}{:20,.2f}".format("Discounted Total:",subtotal));
print("{:20}+{:19,.2f}".format("Tax:",taxAmt));
print("\n" + " "*20 + "-"*20);
print("{:20}${:19,.2f}".format("Total amount:",totalAmt));

##run1
##Enter amount sold: 80
##Enter item cost: $100
##Enter discount: %10
##Enter tax: %14
##*********BILL*********
##Quantity Sold:                     80.00
##Price per Item:                   100.00
##
##                    --------------------
##Amount:                         8,000.00
##Discount:           -             800.00
##
##                    --------------------
##Discounted Total:               7,200.00
##Tax:                +           1,008.00
##
##                    --------------------
##Total amount:       $           8,208.00

##run2
##Enter amount sold: 12
##Enter item cost: $10.99
##Enter discount: %0
##Enter tax: %8.75
##*********BILL*********
##Quantity Sold:                     12.00
##Price per Item:                    10.99
##
##                    --------------------
##Amount:                           131.88
##Discount:           -               0.00
##
##                    --------------------
##Discounted Total:                 131.88
##Tax:                +              11.54
##
##                    --------------------
##Total amount:       $             143.42

##run3
##Enter amount sold: 10000
##Enter item cost: $300
##Enter discount: %5
##Enter tax: %8
##*********BILL*********
##Quantity Sold:                 10,000.00
##Price per Item:                   300.00
##
##                    --------------------
##Amount:                     3,000,000.00
##Discount:           -         150,000.00
##
##                    --------------------
##Discounted Total:           2,850,000.00
##Tax:                +         228,000.00
##
##                    --------------------
##Total amount:       $       3,078,000.00

##run4
##Enter amount sold: 19
##Enter item cost: $2
##Enter discount: %30
##Enter tax: %8
##*********BILL*********
##Quantity Sold:                     19.00
##Price per Item:                     2.00
##
##                    --------------------
##Amount:                            38.00
##Discount:           -              11.40
##
##                    --------------------
##Discounted Total:                  26.60
##Tax:                +               2.13
##
##                    --------------------
##Total amount:       $              28.73

##run5
##Enter amount sold: 100
##Enter item cost: $10
##Enter discount: %10
##Enter tax: %10
##*********BILL*********
##Quantity Sold:                    100.00
##Price per Item:                    10.00
##
##                    --------------------
##Amount:                         1,000.00
##Discount:           -             100.00
##
##                    --------------------
##Discounted Total:                 900.00
##Tax:                +              90.00
##
##                    --------------------
##Total amount:       $             990.00
