#WAP to check whether a year is a leap year or not.
y = int(input("Enter the year :"))
if(y%4==0 and  y%100==0):
    print("this is leap year")
else:
    print("this is not leap year")