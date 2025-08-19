#check if the number is divisible by 3 and last number is 4
a= int(input("Enter the number:"))

if(a%3==0 and a%10==4):
    print("The no is divisible by 3 and last number is 4")
else:
    print("The no is not divisible by 3 and last number is 4")