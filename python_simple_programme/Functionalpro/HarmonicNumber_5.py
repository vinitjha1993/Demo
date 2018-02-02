"""harmonic number"""
no=1
num=0
N=int(input("enter any number"))
if N!=0:
    for i in range(N):
        num+=1/no
        print("1/",no,"+",end="")
        no+=1
else:
    N = int(input("enter any number"))
print()
print(num)

