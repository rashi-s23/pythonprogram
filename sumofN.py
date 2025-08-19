# Take an integer N as input. Your task is to calculate and print the sum of the digits of the 
N = int(input("Enter a number: "))
digit_sum = 0

while N > 0:
    digit_sum += N % 10   
    N //= 10              
print(digit_sum)