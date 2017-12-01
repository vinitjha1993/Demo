def insertion_sort(list):  # check it                        insertion_sort_String()
    for i in range(1, len(list) - 1):
        item = list[i]
        j = i - 1
        while j >=0 and list[j] > item:
            list[j + 1] = list[j]
            j = j - 1

        list[j + 1] = item


string = "aayi"
l = list(string)
lis=[]
for i in range(len(l)):
    b=ord(l[i])
    lis.append(b)

#ord(b)
insertion_sort(lis)
s=''.join(chr(i) for i in lis)
print(s,"")