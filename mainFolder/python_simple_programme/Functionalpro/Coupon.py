import random
N=int(input("enter no of coupons"))
l=[]
count=0
def rand_no():
    ran_no=random.randint(1, N)           #generate random no.
    return ran_no
i=0
while i!=N:
    no=rand_no()
    if no in l:                         #check whether no exist in list or not
        count+=1                        #increase count if exist
    else:
        l.append(no)                     #append the no. if not exist and count also
        count+=1
        i+=1

print(l)
print("{count} no of times required to generate diff coupon".format(count=count))













