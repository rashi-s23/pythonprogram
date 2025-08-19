#display the grade

a = int(input("Enter your percentage:"))

if(a>85):
    print("A+")
elif(a<=85  and a>=65):
    print("A")
elif(a<=65 and a>=45):
    print("B")
elif(a<=45 and a>=25):
    print("C")
else:
    print("D")

