#Take an integer N as input and print the count of digits of that number. 
N = int(input("Enter a number: "))
count = 0
while N > 0:
        N //= 10
        count += 1

# Output
print(count)