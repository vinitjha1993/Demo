n=int(input("enter number "))
i=2
def check_prime(n):
    f=0
    for j in range(2,int(n/2)):
        if n%j==0:
            f+=1
    if f==0:
        return 0
    else:
        return 1

if check_prime(n)==0:
    print("this already a prime no, please enter non prime no ")
    n = int(input("enter number "))

while(n>=1):
    if(n%i==0):
        n=n/i
        print ('{}'.format(i))

    else:
        i+=1



