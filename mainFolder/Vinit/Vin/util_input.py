from Vin import utility_4
import datetime

lis_elap=[]

#BINARY SEARCH INTEGER:-
start=datetime.datetime.now()
lis=[1,2,3,4,100,102]
utility_4.Utilit.binary_search_int(lis,102)
stop=datetime.datetime.now()
t1=str(stop-start)
lis_elap.append(t1)
print("elapsed time:",stop-start)

#BINARY SEARCH STRING:-
start=datetime.datetime.now()
string = "vinit"
b = list(string)
utility_4.Utilit.binary_search_str(b,'t')
stop=datetime.datetime.now()
t2=str(stop-start)
lis_elap.append(t2)
print("elapsed time:",stop-start)

#INSERTION SORT INTEGER:-
start=datetime.datetime.now()
list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
utility_4.Utilit.insertion_sort_int(list)
print("INSERTION SORTED INTEGER:-",list)
stop=datetime.datetime.now()
t3=str(stop-start)
lis_elap.append(t3)
print("elapsed time:",stop-start)

#INSERTION SORT STRING:-
start=datetime.datetime.now()
utility_4.Utilit.insertion_sort_int(b)
print("INSERTION SORTED STRING:-",b)
stop=datetime.datetime.now()
t4=str(stop-start)
lis_elap.append(t4)
print("elapsed time:",stop-start)

#BUBBLE SORT INTEGER:-
start=datetime.datetime.now()
a=[1,7,3,9,4,2]
t=utility_4.Utilit.bubble_int(a)
print("BUBBLE SORTED INTEGER:-   ",a)
stop=datetime.datetime.now()
t5=str(stop-start)
lis_elap.append(t5)
print("elapsed time:",stop-start)

#BUBBLE SORT STRING:-
start=datetime.datetime.now()  #start_time
string = "vinit kumar jha"
a = string.split()
t = utility_4.Utilit.bubble_int(b)
print("BUBBLE SORTED STRING:-   ",b)
stop=datetime.datetime.now()
t6=str(stop-start)
lis_elap.append(t6)
print("elapsed time:",stop-start)             #stop_time

#ELAPSED TIME IN UNORDER:-

print("ELAPSED TIME IN UNORDER:-",lis_elap)

#ELAPSED TIME IN DESC ORDER:-

lis_elap.sort(reverse=True)
print("ELAPSED TIME IN DESC ORDER:-",lis_elap)