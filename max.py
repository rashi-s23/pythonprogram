#Read three integers and print their maximum.
a= int(input("Enter the 1 no:"))
b=int(input("Enter the 2 no:"))
c=int(input("Enter the 3 no :"))
if(a>b and a>c):
    print("a is maxi")
elif( b>c):
    print("b is maxi")
else:
    print("c is maxi")