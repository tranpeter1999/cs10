#Peter Tran
#1104985
#this program checks whether an inputted string is a palindrome or not (including spaces)

def isPalindrome(s:str)->(bool):
	return s == s[::-1]
	
def main():
	userInput = 0
	while userInput != "-1":
		userInput = input("Enter a String (-1 to quit): ")
		
		if userInput == "-1":
			break
			
		if isPalindrome(userInput):
			print(userInput, "is a palindrome")
		else:
			print(userInput, "is not a palindrome")
		print() #create space between inputs
	
	input("Press Enter to quit")

if __name__ == "__main__":
	main()

##run 1
##Enter a String (-1 to quit): noon
##noon is a palindrome
##
##Enter a String (-1 to quit): print
##print is not a palindrome
##
##Enter a String (-1 to quit): racecar
##racecar is a palindrome
##
##Enter a String (-1 to quit): speed
##speed is not a palindrome
##
##Enter a String (-1 to quit): -1
##Press Enter to quit

##run 2
##Enter a String (-1 to quit): 
## is a palindrome
##
##Enter a String (-1 to quit): -1
##Press Enter to quit

##run 3
##Enter a String (-1 to quit): 10801
##10801 is a palindrome
##
##Enter a String (-1 to quit): mom
##mom is a palindrome
##
##Enter a String (-1 to quit): dad
##dad is a palindrome
##
##Enter a String (-1 to quit): 10802
##10802 is not a palindrome
##
##Enter a String (-1 to quit): -1
##Press Enter to quit

##run 4
##Enter a String (-1 to quit): bro
##bro is not a palindrome
##
##Enter a String (-1 to quit): orb
##orb is not a palindrome
##
##Enter a String (-1 to quit): bro orb
##bro orb is a palindrome
##
##Enter a String (-1 to quit): -1
##Press Enter to quit

##run 5
##Enter a String (-1 to quit): -1
##Press Enter to quit


