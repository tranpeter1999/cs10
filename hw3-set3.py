def sumOfDoubleEvenPlace(cardNum:str) -> (int):
	sum = 0
	
	for i in cardNum[-2::-2]:
		sum = sum + getDigit(int(i))
		
	return sum

def sumOfOddPlace(cardNum:str) -> (int):
	sum = 0
	
	for i in cardNum[-1::-2]:
		sum = sum + int(i)
		
	return sum

def getDigit(num:int) -> (int):
	num = 2*num
	
	if num >= 10:
		sum = 0
		
		for i in range(2):
			sum = sum + int(str(num)[i])
			
		return sum
	return num

def isValid(cardNum:str) -> (bool):
	print(sumOfDoubleEvenPlace(cardNum), sumOfOddPlace(cardNum))
	return (sumOfDoubleEvenPlace(cardNum) + sumOfOddPlace(cardNum))%10 == 0

def main():
	inp = ""
	
	while inp != "-1":
		inp = input("Enter credit card number (-1 to quit): ")
		
		if inp == "-1":
			break
			
		print(isValid(inp) and "Card number is valid!" or "Card number is not valid!")
	
	

if __name__ == "__main__":
	main()