count1_1000=0
count2_500=0
count3_100=0
count4_50=0
count5_10=0
count6_5=0
count7_2=0
count8_1=0

def vend(money):
    global count1_1000
    global count2_500
    global count3_100
    global count4_50
    global count5_10
    global count6_5
    global count7_2
    global count8_1


    if money>=1000:
        money=money-1000
        count1_1000=count1_1000+1
        #print(money)
        return vend(money)

    elif money>=500:
        money=money-500
        count2_500=count2_500+1
        #print(money)
        return vend(money)

    elif money >=100:
        money = money-100
        count3_100=count3_100+1
        #print(money)
        #print(count3_100)
        return vend(money)

    elif money >=50:
        money = money-50
        count4_50=count4_50+1
        #print(money)
        return vend(money)

    elif money >=10:
        count5_10 = 0
        money = money -10
        count5_10=count5_10+1
        #print(money)
        return vend(money)

    elif money >=5:
        money = money-5
        count6_5=count6_5+1
        #print(money)
        return vend(money)

    elif money >=2:
        money = money-2
        count7_2=count7_2+1
        return vend(money)

    elif money >=1:
        money = money-1
        count8_1=count8_1+1
        return vend(money)
    print("number of 1000 notes",count1_1000)
    print("number of 500 notes", count2_500)
    print("number of 100 notes", count3_100)
    print("number of 50 notes", count4_50)
    print("number of 10 notes", count5_10)
    print("number of 5 notes", count6_5)
    print("number of 2 notes", count7_2)
    print("number of 1 notes", count8_1)

vend(3999)