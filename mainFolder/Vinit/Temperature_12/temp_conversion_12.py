class Temp:

    ''' Celsius to Fahrenheit:   (°C × 9/5) + 32 = °F
Fahrenheit to Celsius:   (°F − 32) x 5/9 = °C'''

    @staticmethod
    def temp_CtoF(c):
        f=(c*9/5)+32
        print(f)



    @staticmethod
    def temp_FtoC(fr):
        c=(fr-32)*5/9
        print(c)
