#Write a program to print all even numbers from 1 to N, where you have to take N as input from the user. 
n=int(input("Enter the no.:"))
i=1
while(i<=n):
    if(i%2==0):
        print(i)
    i+=1