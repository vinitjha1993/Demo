def insertion_sort_int(list):  # insertion_sort_int()
    for i in range(1, len(list)):
        item = list[i]
        j = i - 1
        while j >= 0 and list[j] > item:
            list[j + 1] = list[j]
            j = j - 1

        list[j + 1] = item
    return list




lis=[]
count=0
def check_prime(n):                            #check for prime no
    if n>=2:
        f=0
        for j in range(2,n):
            if n%j==0:
                f+=1
                break
        if f==0:
            return 0   #prime
        else:
            return 1    #not prime


def anag(m,n):                                  #check for anagram
    x = [int(d) for d in str(m)]
    y=[int(d) for d in str(n)]
    if len(x)==len(y):
        a=insertion_sort_int(x)
        b=insertion_sort_int(y)
            #a=''.join(sorted(m))
            #b=''.join(sorted(n))
        if a==b:
            return 1
        else:
            return  0



def palin(n):                    #check for palindrome
    if n>9:
        temp=n
        rev=0
        while(n>0):
            rem=n%10
            rev=rev*10+rem
            n=n//10
        if(temp==rev):
            return 0  #print("The number is a palindrome!")
        else:
            return 1  #print("The number isn't a palindrome!")

lis2=[]
for i in range(0,1000):                                   #check for prime and palindrome
    if check_prime(i)==0:
        count+=1
        lis.append(i)
        if palin(lis[count-1])==0:
            lis2.append(lis[count-1])
print("prime no:-",lis)
print("prime and plaindrome:-",lis2)




def prime_anagram(lis):                               #check for prime and Anagram
    #print(lis)
    for i in range(0,len(lis)):
        if check_prime(int(lis[i]))==0:
            for j in range(i+1,len(lis)):
                str1=str(lis[i])
                str2=str(lis[j])
                if anag(str1,str2)==1:
                    print("prime and anagram no are",lis[i],lis[j])

prime_anagram(lis)


