import random

stake = int(input("enter stake"))
goal = int(input("enter goals"))
num_times = int(input("enter no. of times"))
win = 0
los = 0
t=stake
for i in range(num_times):
    t=stake
    while t>0 and t<goal:
        a = random.random()  # o for loss & 1 for win
        if a>0.5:
            t+=1
        else:
            t-=1
    if t==0:
        los+=1
    else:
        win+=1

print("win",win)
print("los",los)
