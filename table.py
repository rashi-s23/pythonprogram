#Take a number A as input, print its multiplication table having the first 10 multiples. 
n=int(input("Enter the number"))
i=1
while(i<=10):
    print(n,"*",i,"=",n*i)
    i=i+1