def bubble_str(list):  # bubble_string
    for i in range(0, (len(list) - 2) + 1):
        for j in range(0, (len(list) - 2 - i) + 1):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
string = "my name is vinit"
b = string.split()
print(b)
bubble_str(b)
print(b)