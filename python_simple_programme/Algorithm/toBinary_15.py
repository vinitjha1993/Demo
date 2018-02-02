class Binary:
    @staticmethod
    def toBinary(n):
        list=[]
        var=0
        dec=n
        if n==0:
            return ''
        else:
            while dec>0:
                r=dec%2
                list.append(r)
                dec=dec//2
            list.reverse()
        print(list)
        t=len(list)
        if t<32:
            while t<32:
                list.insert(0,var)
                t+=1
        avg = len(list) //4
        out = []
        last = 0

        while last < len(list):
            out.append(list[last:last + avg])
            last += avg

        print(out)

Binary.toBinary(10)
