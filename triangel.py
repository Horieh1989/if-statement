import math
a=float(input("Enter side a: "))
b=float(input("Enter side b: "))
c=float(input("Enter side c: "))
if a+b > c and a+c > b and b+c > a:
    print("This is a valid triangle")
    
else:
        print("This is not a valid triangle")
   