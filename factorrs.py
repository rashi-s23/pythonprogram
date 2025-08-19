#print all the factors/divisors of given +ve number
num=int(input("Enter the no.:"))
count=1
while(count<=num):
    if(num%count==0):
        print(count)
    count +=1
        