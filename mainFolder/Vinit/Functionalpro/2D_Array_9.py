m=int(input("enter no of rows"))
n=int(input("enter no of columns"))

a = []

print("enter elemnts")
for i in range(m):
    l1=[]
    for j in range(n):
        b=int(input())
        l1.append(b)
    a.append(l1)

print(a)
