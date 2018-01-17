def merge(a, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)


    for i in range(0, n1):
        L[i] = a[l + i]

    for j in range(0, n2):
        R[j] = a[m + 1 + j]


    i = 0   # Initial index of first subarray
    j = 0   # Initial index of second subarray
    k = l   # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1


    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1


    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1



def mergeSort(list, low, high):
    if low < high:

        middle = (low + high) // 2;

        mergeSort(list, low, middle);

        mergeSort(list, middle + 1, high);

        merge(list, low, middle, high);
list=[4,1,3,2]
mergeSort(list,0,len(list)-1)

print("\n\nSorted array is")
for i in range(len(list)):
    print("%d" % list[i]),
