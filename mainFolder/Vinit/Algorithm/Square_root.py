import math
import sys
class Square_r:
    @staticmethod
    def sqrt():
        c=int(input("enter non negative number"))
        t=c
        while math.fabs(t-(c/t))>(sys.float_info.epsilon*t):
            t = ((c / t) + t) / 2
        print("square root of",c,"is",t)


Square_r.sqrt()

