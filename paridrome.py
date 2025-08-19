A = int(input("Enter a number: "))
original = A
reverse_num = 0
while A > 0:
    digit = A % 10
    reverse_num = reverse_num * 10 + digit
    A //= 10
if original == reverse_num:
    print("Yes")
else:
    print("No")