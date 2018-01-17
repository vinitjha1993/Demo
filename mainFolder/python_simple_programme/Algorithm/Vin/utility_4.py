
class Utilit:

    @staticmethod
    def binary_search_int(list, item):                  #binary_search_int
        # print(type(lis))
        low = 0
        high = len(list)-1
        found = 0
        while low <= high:
            mid = (low + high) // 2
            if list[mid] == item:
                 #return 1
                 print("BINARY_SEARCH_INTEGER:-    102 found at",mid)# found
                 break
            elif item <=list[mid]:
                low = low
                high = mid - 1
            else:
                high = high
                low = mid + 1
        return 0


    @staticmethod
    def binary_search_str(b, item):  # binary_search_str
        low = 0
        high = len(b) - 1
        found = 0
        while low <= high:
            mid = (low + high) // 2
            if b[mid] == item:
                print("BINARY_SEARCH_STRING:-     c found at", mid)
                return 1
                # print()# found
            elif item < b[mid]:
                low = low
                high = mid - 1
            else:
                high = high
                low = mid + 1
        return 0





    @staticmethod
    def insertion_sort_int(list):                                      #insertion_sort_int()
        for i in range(1, len(list)):
            item = list[i]
            j = i - 1
            while j >= 0 and list[j] > item:
                list[j + 1] = list[j]
                j = j - 1

            list[j+1] = item






    @staticmethod
    def bubble_int(list):                                                          #bubble_int
        for i in range(0,(len(list)-2)+1):
            for j in range(0,(len(list)-2-i)+1):
                if list[j]>list[j+1]:
                    temp=list[j]
                    list[j]=list[j+1]
                    list[j+1]=temp





