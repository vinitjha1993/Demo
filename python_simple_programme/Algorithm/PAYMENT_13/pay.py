class Paym:
    @staticmethod
    def take(P,Y,R):
        n=12*Y
        r=R/(12*100)
        pay_total=(P*r)/(1-(pow((1+r),-n)))
        print(pay_total)