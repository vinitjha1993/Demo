def insertion_sort_str(list):              # insertion_sort_int()
    for i in range(1, len(list)):
        item = list[i]
        j = i - 1
        while j >= 0 and list[j] > item:
            list[j + 1] = list[j]
            j = j - 1

        list[j + 1] = item
    return list

str=input("enter 1st string")
str2=input("enter 2nd string")
str=list(str)
str2=list(str2)
if len(str)==len(str2):                                #check length of string is equal
        a=insertion_sort_str(str)                       #sort the given 2 string
        c=insertion_sort_str(str2)
        print(a)
        print(c)
        if a==c:                                   #check if 2 string are equal
            print("strings are anagram")
        else:
            print("strings are not anagram")
else:
    print("string length should be same")