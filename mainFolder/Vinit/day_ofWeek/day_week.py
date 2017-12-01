class Day:
    @staticmethod
    def inp(d,m,y):
        yr=y-((14-m))//12
        x = yr+(yr // 4)-(yr//100)+(yr//400)
        mn = (m+(12*((14-m)//12)))-2
        day = (d+x+(31*mn)// 12)%7
        return day


