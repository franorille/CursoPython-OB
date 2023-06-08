def bisiesto(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 != 0):
        print("el año", year, "es bisiesto")
    else:
        print("el año", year, "no es bisiesto")


bisiesto(2004)
bisiesto(2006)
bisiesto(2000)
bisiesto(1993)
bisiesto(1996)
