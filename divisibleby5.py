#Take an integer A as input. You have to tell whether A is divisible by both 5 and 11 or  not 
A = int(input("Enter the number:"))
if(A%5==0 and A%11==0):
    print("The number is divisble by both 5 and 11")
else:
    print("The number is not divisible by 5 and 11")
