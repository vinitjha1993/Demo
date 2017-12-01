import math
t=float(input("enter temperature larger than or equal to 50"))
v=float(input("enter temperature larger than or equal to 120 & less than 3"))
if t<=50:
    if v <= 120 and v >= 3:

            b=math.pow(v,0.6)
            print("h")
            c=0.6215*t
            d=0.4275*t
            w=35.74+c+((d-35.75)*b)
    else:
            print("enter the correct value of v")
else:
    print("enter the correct value of t ")
print(w)