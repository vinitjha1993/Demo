def insertion_sort_str(list):              # insertion_sort_int()
    for i in range(1, len(list)):
        item = list[i]
        j = i - 1
        while j >= 0 and list[j] > item:
            list[j + 1] = list[j]
            j = j - 1

        list[j + 1] = item
    return list


def binary_search_str(list, item):  # binary_search_int
    low = 0
    high = len(list) - 1
    #found = 0
    while low <= high:
        mid = (low + high) // 2
        if list[mid] == item:
            print("BINARY_SEARCH_String:- string found at", mid,"position")      #found
            break
        elif item <= list[mid]:
            low = low
            high = mid - 1
        else:
            high = high
            low = mid + 1
    return 0

string = "vinit kumar jha"
b = string.split()                   #split the string
c=insertion_sort_str(b)              #sort the string
print(c)
binary_search_str(b,'jha')


