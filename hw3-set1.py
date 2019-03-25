#Peter Tran
#1104985
#this program calculates stock transactions with functions

def inputStock(stockName):
	stockName = input("Enter Stock name (-1 to quit): ");
	if stockName == "-1":
		return
	
	numShares = int(input("Enter Number of shares: "));
	purchasePrice = float(input("Enter Purchase price: "));
	salePrice = float(input("Enter Selling price: "));
	brokerCommission = float(input("Enter Commision: " ));
	
	return numShares, purchasePrice, salePrice, brokerCommission

def calcStock(numShares, purchasePrice, salePrice, brokerCommission):
	purchaseCost = numShares*purchasePrice;
	saleAmount = numShares*salePrice;
	brokerPurchaseCommission = purchaseCost*brokerCommission;
	brokerSaleCommission = saleAmount*brokerCommission;
	total = saleAmount - brokerSaleCommission - purchaseCost - brokerPurchaseCommission;
	
	return purchaseCost, saleAmount, brokerPurchaseCommission, brokerSaleCommission, total

def displayStock(stockName, purchaseCost, saleAmount, brokerPurchaseCommission, brokerSaleCommission, total):
	print("Joe purchased and sold stock from " + stockName);
	print("The amount of money Joe paid is                           ${:12,.2f}".format(purchaseCost));
	print("The amount of commission paid to broker for purchase is   ${:12,.2f}".format(brokerPurchaseCommission));
	print("The amount of money Joe sold for is                       ${:12,.2f}".format(saleAmount));
	print("The amount of commission paid to broker for sale is       ${:12,.2f}".format(brokerSaleCommission));
	
	if total >= 0:
		print("Joe made                                                  ${:12,.2f}\n\n".format(total));
	else:
		print("Joe lost                                                  ${:12,.2f}\n\n".format(total));

def main():
	stockName = ""
	while stockName != "-1":
		#input
		ns,pp,sp,bc = inputStock(stockName)
		
		if stockName == "-1":
			break

		#calc
		pc,sa,bpc,bsc,tot = calcStock(ns,pp,sp,bc)

		#output
		displayStock(stockName,pc,sa,bpc,bsc,tot)
		
	input("Press Enter to quit")
	
if __name__ == "__main__":
	main()