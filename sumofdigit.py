# read n , print sum of digits in N

n = int(input("Enter the digits:"))
s = 0

while(n>0):
    digit = n%10 #reminder
    n=n//10 #quotient 
    s += digit
    print(s)
