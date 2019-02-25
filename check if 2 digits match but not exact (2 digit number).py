x = int(input("Enter 2 numbers: "))
y = int(input())

if(x+y)%11 == 0 and (x-y)%11 != 0:
    print("True")
else:
    print("False")
