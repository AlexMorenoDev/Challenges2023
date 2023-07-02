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