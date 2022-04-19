# defining variables for input
l=float(input("ENTER THE LENGTH:"))
b=float(input("ENTER THE BREADTH:"))
h=float(input("ENTER THE HEIGHT:"))
u=input("ENTER THE UNIT:")
# formula
vol=l*b*h
d=((l**2)+(b**2)+(h**2))**0.5
# printing outputs
print("The volume of the rectangular prism is " +str(vol) + " cubic " + str(u))
print("Diagonal length of the rectangular cube is " +str(d) + " " + str(u))
