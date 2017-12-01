import math
def dist():
    o=(0,0)
    x=input("enter value of x")
    y=input("enter value of y")
    t=(x,y)
    a=float(t[0])-float(o[0])
    b=float(t[1])-float(o[1])
    dist=math.sqrt((a*a)+(b*b))
    print(dist)

dist()