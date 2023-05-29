'''
/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */
'''
from calendar import Calendar
from datetime import datetime

# Function using calendar module
def is_friday_13th(month, year):
    result = False
    
    obj = Calendar()
    for day in obj.itermonthdays2(year, month):
        if day[0] == 13:
            if day[1] == 4:
                result = True
            break

    return result

# A little bit faster function using datetime module
def is_friday_13th_2(month, year):
    return datetime(year, month, 13).weekday() == 4

def main():
    print(is_friday_13th(8, 2001))
    print(is_friday_13th(11, 2010))
    print(is_friday_13th(1, 2023))
    print(is_friday_13th(2, 2023))
    print(is_friday_13th(10, 2023))
    print("------------------------")
    print(is_friday_13th_2(8, 2001))
    print(is_friday_13th_2(11, 2010))
    print(is_friday_13th_2(1, 2023))
    print(is_friday_13th_2(2, 2023))
    print(is_friday_13th_2(10, 2023))
    
if __name__ == "__main__":
    main()