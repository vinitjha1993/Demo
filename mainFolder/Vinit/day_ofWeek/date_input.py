from day_ofWeek import day_week
date=int(input("enter day"))
month=int(input("enter month"))
year=int(input("enter year"))

day=day_week.Day.inp(date,month,year)      #0 for sunday, 1 for monday
print(day)
