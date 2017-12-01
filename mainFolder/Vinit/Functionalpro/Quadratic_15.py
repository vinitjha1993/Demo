'''::::::::::a*x*x+b*x+c:::::::'''
import cmath
a=int(input("enter value of a"))
b=int(input("enter value of b"))
c=int(input("enter value of c"))

d=b*b-4*a*c
sq=cmath.sqrt(d)

x1=(sq-b)/(2*a)
x2=(sq+b)/(2*a)*-1
print(x2)
print(x1)
