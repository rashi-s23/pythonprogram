#check if the number is divisible by 7 or last number is 5
a=int(input("Enter the number:"))
if(a%7==0 or a%10==5):
    print("The number is divisible by 7 or the last number is 5")
else:
    print("The number is not  divisible by 7 or the last number is not 5 ")