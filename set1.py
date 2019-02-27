#Peter Tran
#1104985
#this program is a lottery program that allows the user to enter a 2 digit number (0-9 included)
#the program then generates a random int from 0-99 and compares it to user's guess

from random import randint

choice = 0
ans = 0

while choice != -1:
    choice = int(input("Enter your guess from 0 to 99 (-1 to quit): "))

    if choice == -1:
        break
    
    ans = randint(0,99)

    if choice < 0 or choice > 99:
        print("Out of bounds!")
    else:
        print("You chose:", choice)
        print("The answer was:", ans)

        temp1 = (choice//10)*11
        temp2 = (choice%10)*11
        
        if choice == ans:
            print("You win $10,000!")
        elif ((temp1-ans)%10 == 0 and temp2//10 == ans//10) or ((temp2-ans)%10 == 0 and temp1//10 == ans//10):
            print("You win $3,000!")
        elif (temp1-ans)%10 == 0 or (temp2-ans)%10 == 0 or temp1//10 == ans//10 or temp2//10 == ans//10:
            print("You win $1,000!")
        else:
            print("You don't win...")

input("Press enter to terminate program")

##Enter your guess from 0 to 99 (-1 to quit): 5
##You chose: 5
##The answer was: 66
##You don't win...
##Enter your guess from 0 to 99 (-1 to quit): 10
##You chose: 10
##The answer was: 91
##You win $1,000!
##Enter your guess from 0 to 99 (-1 to quit): 10
##You chose: 10
##The answer was: 89
##You don't win...
##Enter your guess from 0 to 99 (-1 to quit): 10
##You chose: 10
##The answer was: 16
##You win $1,000!
##Enter your guess from 0 to 99 (-1 to quit): 10
##You chose: 10
##The answer was: 14
##You win $1,000!
##Enter your guess from 0 to 99 (-1 to quit): 10
##You chose: 10
##The answer was: 3
##You win $1,000!
##Enter your guess from 0 to 99 (-1 to quit): -10
##Out of bounds!
##Enter your guess from 0 to 99 (-1 to quit): -1
##Press enter to terminate program



#EXPLANATION FOR CASE CHECKING WITH MATHS
    #case 1 : exact match
        #choice == ans is an exact match
    #case 2 : 2 digit matches, but in wrong order
        #this is the most involved case since it requires us to lay down some ground work
        
        #we calculate temp1 and temp2
        #temp1 = (choice//10)*11 which will give you a 2 digit number
        #with the digits replaced by the first digit (i.e. choice = 15, temp1 = 11 (choice//10 = 1*11 = 11))
        #temp2 = (choice%10)*11 which will give you a 2 digit number
        #with the digits replaced by the second digit (i.e. choice = 15, temp2 = 55 (choice%10 = 5*11 = 55))

        #the reason we calculate temp1 and temp2 is so that we can compare the cases for first digit and second digit easily
        #for example, with choice = 15, we generate temp1 = 11 and temp2 = 55
        #if the ans = 51, when we compare temp1's digits, we don't have to reorganize the digits in any way. we can compare each digit directly
        #51 and 11 have the 2nd digit matching, and 51 and 55 have the 1st digit matching. because we have both a 1st digit match and a 2nd digit match EXACTLY, we know that there are 2 matches but they're out of order

        #so in short, to know that 2 digit matches but are out of order, we simply check that the ones place of choice matches with the tens place of ans and that the ones place of ans matches with the tens place of choice

        #in order to check digit matching (pseudocode)
            #to check 1st digit matching
                #number1 = 15
                #number2 = 19
        
                #if number1//10 == number2//10
                    #MATCH!

                #reasoning
                    #if we int divide by 10, we ignore the ones place and get the tens place (1st digit). we then simply check if they match
            #to check 2nd digit matching
                #number1 = 15
                #number2 = 95
        
                #if (number1-number2)%10 == 0
                    #MATCH!

                #reasoning
                    #if we subtract 1 number from the other, we cause the ones place (2nd digit) to be directly related to each other. if the ones place subtract from each other and = 0, then the ones places have to match
    #case 3 : 1 digit matches, any order
        #we set up the ground work for this case back in case 2 by calculating temp1 and temp2

        #now all we have to do is check if there are any digit matches, regardless of what place they are in
    #case 4 : no matches
        #default (else) case, if the above cases don't pass, then we assume this case

        
