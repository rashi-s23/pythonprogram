# You are given two integers A and B. You have to find the value of A^B. 
A = int(input("Enter A: "))
B = int(input("Enter B: "))
result = 1
for i in range(B):
    result *= A

print(result)