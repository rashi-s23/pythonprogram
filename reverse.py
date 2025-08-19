# read n print reverse of n 
n = int(input("enter the number:"))
ans = 0  
while(n>0):
    digit= n%10
    n = n//10

    ans = ans*10 + digit 
    print(ans)
 

