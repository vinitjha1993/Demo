def check_prime(n):
    f=0

    for j in range(2,int(n)):
        if n%j==0:
            f+=1
            break
    if f==0:
        return 0   #prime
    else:
        return 1    #not prime
#n=int(input("enter "))
for i in range(2,1000):
     if check_prime(i)==0:
         print(i)
