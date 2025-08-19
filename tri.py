# 3 integer angles of  triagngle tell whether thhe tri is valid or not

s1=int(input("Enter the side 1:"))
s2=int(input("Enter the side 2:"))
s3=int(input("Enter the side 3:"))
if(s1+s2+s3 == 180 ):
    print("The triangle is valid") 
else:
    print("The triangle is not valid")
