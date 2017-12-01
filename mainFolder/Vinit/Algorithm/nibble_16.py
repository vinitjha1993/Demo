class Binary:
    @staticmethod
    def toBinary(n):
        print("decimal no is:-         ",n)
        list=[]
        var=0
        dec=n
        if n==0:
            raise Exception('number should be 0<N<=256!')
        elif n<=256:
            while dec>0:
                r=dec%2
                list.append(r)
                dec=dec//2
            list.reverse()

            print("binary no before swapping:- ",list)
            #print(len(list))

            length=len(list)
            if length<8:
                num=length%8
                req=8-num
                for i in range(req):
                    list.insert(0,var)
                print("1 byte of binary no:-       ",list)

            list2=[]
            len_list2=len(list)//2
            for i in range(len_list2):
                list2.append(list[i])
            print("list2:-                     ",list2)

            j=4
            for i in range(4):
                list[i]=list[j]
                j+=1
            print("swapped last half of the list:-",list)
            i=4
            for k in range(4):
                list[i]=list2[k]
                i+=1
            print("list after swapping         ",list)

            decimal_no=0
            l = 7
            for i in range(8):
                decimal_no=decimal_no+list[l]*pow(2,i)
                l-=1
            print(decimal_no)


        else:
            raise Exception('number should be 0<N<=256!')

Binary.toBinary(256)