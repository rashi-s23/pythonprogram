#You are given an integer A, you need to find and return the sum of all the even numbers between 1 and A. Even numbers are those numbers that are divisible by 2. 
number=int(input("Enter the number"))
n=1
sum=0
while(n<=number):
    if(n%2==0):
        sum=sum+n
    n+=1   
    
print(sum)