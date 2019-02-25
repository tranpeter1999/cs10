x = int(input("Enter 2 numbers: "))
y = int(input())

#EXACT MATCH
#x == y

#2 DIGITS MATCH
if(x+y)%11 == 0 and (x-y)%11 != 0:
    print("True")
else:
    print("False")

#1 DIGIT MATCH
#19
#95

    #19
        #19%10  -> 9  *11 -> 99
        #19//10 -> 1  *11 -> 11

#     (((19 %10)*11)-95)%10 == 0 or |((19 %10)*11)-95| < 10
#  or (((19//10)*11)-95)%10 == 0 or |((19//10)*11)-95| < 10
    
#or
    
#19
#59   (x-y)%10 == 0
    
#or
    
#25
#21   |x-y| < 10

#NO MATCH
#else
