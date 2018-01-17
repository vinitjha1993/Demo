def findTrip(list,n):

    list3=[]
    found=True
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                list2 = []
                if list[i]+list[j]+list[k]==0:
                    list2.append(list[i])
                    list2.append(list[j])
                    list2.append(list[k])
                    list3.append(list2)

    print(list3)
    print("no of triplet:-",len(list3))



list=[0,-1,2,-3,-1,3,-2,-3,2]
n=len(list)
a=findTrip(list,n)


