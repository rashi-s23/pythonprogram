# Write a program to print all odd numbers from 1 to N, where you have to take N as input from user. 
n=int(input("Enter the no."))
i=1
while(i<=n):
    if(i%2!=0):
        print(i)
    i+=1