year=input("enter any year")
if len(year)!=4:
   print("year should be in 4 digit only")
   year = input("enter any year")
p=int(year)
if (p % 4) == 0:
   if (p % 100) == 0:
       if (p % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))
