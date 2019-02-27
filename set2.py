#Peter Tran
#1104985
#this program calculates stock transactions using a while loop
stockName = 0;

while stockName != "-1":
    #input
    stockName = input("Enter Stock name (-1 to quit): ");
    if stockName == "-1":
        break
    
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
    print("Joe purchased and sold stock from " + stockName);
    print("The amount of money Joe paid is                           ${:12,.2f}".format(purchaseCost));
    print("The amount of commission paid to broker for purchase is   ${:12,.2f}".format(brokerPurchaseCommission));
    print("The amount of money Joe sold for is                       ${:12,.2f}".format(saleAmount));
    print("The amount of commission paid to broker for sale is       ${:12,.2f}".format(brokerSaleCommission));

    total = saleAmount - brokerSaleCommission - purchaseCost - brokerPurchaseCommission

    if total >= 0:
        print("Joe made                                                  ${:12,.2f}\n\n".format(total));
    else:
        print("Joe lost                                                  ${:12,.2f}\n\n".format(total));

input("Press enter to terminate program")

##Enter Stock name (-1 to quit): Schmoe, Inc.
##Enter Number of shares: 10000
##Enter Purchase price: 33.92
##Enter Selling price: 35.92
##Enter Commision: 0.04
##Joe purchased and sold stock from Schmoe, Inc.
##The amount of money Joe paid is                           $  339,200.00
##The amount of commission paid to broker for purchase is   $   13,568.00
##The amount of money Joe sold for is                       $  359,200.00
##The amount of commission paid to broker for sale is       $   14,368.00
##Joe lost                                                  $   -7,936.00
##
##
##Enter Stock name (-1 to quit): Apple
##Enter Number of shares: 100
##Enter Purchase price: 35.23
##Enter Selling price: 155.97
##Enter Commision: 0.07
##Joe purchased and sold stock from Apple
##The amount of money Joe paid is                           $    3,523.00
##The amount of commission paid to broker for purchase is   $      246.61
##The amount of money Joe sold for is                       $   15,597.00
##The amount of commission paid to broker for sale is       $    1,091.79
##Joe made                                                  $   10,735.60
##
##
##Enter Stock name (-1 to quit): Jagex Ltd.
##Enter Number of shares: 15
##Enter Purchase price: 11.99
##Enter Selling price: 5.99
##Enter Commision: 0.04
##Joe purchased and sold stock from Jagex Ltd.
##The amount of money Joe paid is                           $      179.85
##The amount of commission paid to broker for purchase is   $        7.19
##The amount of money Joe sold for is                       $       89.85
##The amount of commission paid to broker for sale is       $        3.59
##Joe lost                                                  $     -100.79
##
##
##Enter Stock name (-1 to quit): Macrohard
##Enter Number of shares: 253
##Enter Purchase price: 25.23
##Enter Selling price: 28.19
##Enter Commision: 0.05
##Joe purchased and sold stock from Macrohard
##The amount of money Joe paid is                           $    6,383.19
##The amount of commission paid to broker for purchase is   $      319.16
##The amount of money Joe sold for is                       $    7,132.07
##The amount of commission paid to broker for sale is       $      356.60
##Joe made                                                  $       73.12
##
##
##Enter Stock name (-1 to quit): Amazone
##Enter Number of shares: 10000
##Enter Purchase price: 12.30
##Enter Selling price: 144.29
##Enter Commision: 0.09
##Joe purchased and sold stock from Amazone
##The amount of money Joe paid is                           $  123,000.00
##The amount of commission paid to broker for purchase is   $   11,070.00
##The amount of money Joe sold for is                       $1,442,900.00
##The amount of commission paid to broker for sale is       $  129,861.00
##Joe made                                                  $1,178,969.00
##
##
##Enter Stock name (-1 to quit): -1
##Press enter to terminate program
