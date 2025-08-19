# Read three angles of triangles and determine their types(Right triangle, Obtuse 
a= int(input("Enter the 1 no:"))
b=int(input("Enter the 2 no:"))
c=int(input("Enter the 3 no :"))
if(a==90 or b==90 or c==90):
    print(" right triangle")
elif(a>90 or b>90 or c>90):
    print("Obtuse triangle")
elif(a<90 or b<90 or c<90):
    print("Acute triangle")
