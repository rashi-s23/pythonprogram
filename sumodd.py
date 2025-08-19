#Take an integer A as input. You have to print the sum of all odd numbers in the range [1, A].
number=int(input("Enter the number"))
n=1
sum=0
while(n<=number):
    if(n%2!=0):
        sum=sum+n
    n+=1       
print(sum)