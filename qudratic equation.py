 
a=float(input("Enter the value of a:"))
b=float(input("Enter the value of b:"))
c=float(input("Enter the value of c:"))

d=(b**2)-(4*a*c)

sol1=(-b-d**0.5)/(2*a)
sol2=(-b+d**0.5)/(2*a)
print('The solution are {0} and {1}'.format(sol1,sol2))
