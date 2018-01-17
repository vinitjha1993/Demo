
def ask(list,low,high):
    print(list)
    if low<high:
        mid=(low+high)//2
        if high==low+1:
            print("if your no is", low,"then yes else no")
            c=input()
            if c=="yes":
                print("your no is ",low)
            else:
                print("your no is",high)
        else:
            print("yes your number in between",list[low],"and",list[mid], "or no if no. in btwn",list[mid+1],"and",list[high])
            c=input()
            if c=="yes":
                ask(list,low,mid)
            else:
                ask(list,mid+1,high)

n=int(input("give range of number"))
def no():
    list=[]
    for i in range(n):
        list.append(i)
    return list

low=0
high=n-1
list=no()
ask(list,low,high)

