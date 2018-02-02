def insertion_sort_str(list):  # insertion_sort_int()
    for i in range(1, len(list)):
        item = list[i]
        j = i - 1
        while j >= 0 and list[j] > item:
            list[j + 1] = list[j]
            j = j - 1

        list[j + 1] = item

string = "vinit kumar jha"
b = string.split()
print(b)
insertion_sort_str(b)
print(b)