import random

lis=[]
count=0
count2=0
n=int(input("enter number of times to flip coin"))


for i in range(n):
    n2 = random.random()
    if n2<0.5:
        lis.append("head")
    else:
        lis.append("tails")


print(lis)

p=(lis.count("head")/n)*100
p2=(lis.count("tails")/n)*100
print("percentage of heads is", p)
print("percentage of tails is",p2)