# no. of digits 
n = int(input("Enter the number:"))
digit = 0

while(n>0):
    n =n/10
    digit = digit + 1
    print(digit)