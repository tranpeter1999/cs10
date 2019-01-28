#Peter Tran
#1104985
#this program calculates stock transactions

#input
stockName = input("Enter Stock name: ");
numShares = int(input("Enter Number of shares: "));
purchasePrice = float(input("Enter Purchase price: "));
salePrice = float(input("Enter Selling price: "));
brokerCommission = float(input("Enter Commision: " ));

#calc
purchaseCost = numShares*purchasePrice;
saleAmount = numShares*salePrice;
brokerPurchaseCommission = purchaseCost*brokerCommission;
brokerSaleCommission = saleAmount*brokerCommission;

#output
print("You purchased and sold stock from " + stockName);
print("The amount of money you paid is ${:12,.2f}".format(purchaseCost));
print("The amount of commission paid to broker for purchase is ${:12,.2f}".format(brokerPurchaseCommission));
print("The amount of money you sold for is ${:12,.2f}".format(saleAmount));
print("The amount of commission paid to broker for sale is ${:12,.2f}".format(brokerSaleCommission));
print("The profit/loss is ${:12,.2f}".format(saleAmount - brokerSaleCommission - purchaseCost - brokerPurchaseCommission));


##run1
##Enter Stock name: Kaplack, Inc.
##Enter Number of shares: 10000
##Enter Purchase price: 33.92
##Enter Selling price: 35.92
##Enter Commision: 0.04
##You purchased and sold stock from Kaplack, Inc.
##The amount of money you paid is $  339,200.00
##The amount of commission paid to broker for purchase is $   13,568.00
##The amount of money you sold for is $  359,200.00
##The amount of commission paid to broker for sale is $   14,368.00
##The profit/loss is $   -7,936.00

##run2
##Enter Stock name: Apple
##Enter Number of shares: 100
##Enter Purchase price: 35.23
##Enter Selling price: 155.97
##Enter Commision: 0.07
##You purchased and sold stock from Apple
##The amount of money you paid is $    3,523.00
##The amount of commission paid to broker for purchase is $      246.61
##The amount of money you sold for is $   15,597.00
##The amount of commission paid to broker for sale is $    1,091.79
##The profit/loss is $   10,735.60

##run3
##Enter Stock name: Jagex Ltd.
##Enter Number of shares: 15
##Enter Purchase price: 11.99
##Enter Selling price: 5.99
##Enter Commision: 0.04
##You purchased and sold stock from Jagex Ltd.
##The amount of money you paid is $      179.85
##The amount of commission paid to broker for purchase is $        7.19
##The amount of money you sold for is $       89.85
##The amount of commission paid to broker for sale is $        3.59
##The profit/loss is $     -100.79

##run4
##Enter Stock name: Microfirm
##Enter Number of shares: 253
##Enter Purchase price: 25.23
##Enter Selling price: 28.19
##Enter Commision: 0.05
##You purchased and sold stock from Microfirm
##The amount of money you paid is $    6,383.19
##The amount of commission paid to broker for purchase is $      319.16
##The amount of money you sold for is $    7,132.07
##The amount of commission paid to broker for sale is $      356.60
##The profit/loss is $       73.12

##run5
##Enter Stock name: Amazone
##Enter Number of shares: 10000
##Enter Purchase price: 12.30
##Enter Selling price: 144.29
##Enter Commision: 0.09
##You purchased and sold stock from Amazone
##The amount of money you paid is $  123,000.00
##The amount of commission paid to broker for purchase is $   11,070.00
##The amount of money you sold for is $1,442,900.00
##The amount of commission paid to broker for sale is $  129,861.00
##The profit/loss is $1,178,969.00
