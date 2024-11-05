# Tyler Hegy
# UWYO COSC 1010
# Submission Date: 11/04/2024
# HW 03
# Lab Section: 12
# Sources, people worked with, help given to: Stack Overflow
# Comments: Used stack overflow for help using the list() function which is used in the day of the week calculation

def leap_year(year):
    if year%400==0:
        leap=True
    elif year%4==0 and year%100!=0:
        leap=True
    else:
        leap=False
    return leap

def jan_first(year):
    y = year-1
    day_first = f'{(36+y+(y/4)-(y/100)+(y/400))%7}'
    day_first=day_first[0]
    return day_first

def valid_date(month,day,year,leap):
    month_days={'January': '31', 'February': '28', 'March': '31', 'April': '30', 'May': '31', 'June': '30', 'July': '31',
             'August': '31', 'September': '30', 'October': '31', 'November': '31', 'December': '31'}
    month_count={'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August',
             '09':'September','10':'October','11':'November','12':'December'}
    if leap==True:
                month_days['February']=29
    if month not in month_count:
        valid=False
    elif day<=0 or day>int(month_days[month_count[month]]):
        valid=False
    elif year<=0:
        valid=False
    else:
        valid=True
    return valid

def week_day(month,day,day_first,leap,valid):
    month_days={'January': '31', 'February': '28', 'March': '31', 'April': '30', 'May': '31', 'June': '30', 'July': '31',
             'August': '31', 'September': '30', 'October': '31', 'November': '31', 'December': '31'}
    month_count={'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August',
             '09':'September','10':'October','11':'November','12':'December'}
    month_names=['January','February','March','April','May','June','July','August','September','October','November','December']
    week_days=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    day_value=0

    if leap==True:
                month_days['February']=29

    if valid==False:
        Week_Day='Invalid Date'
    else:
        for i in range(1, int(month)):  # Iterate through months before the given month
            day_value += int(month_days[list(month_days.keys())[i - 1]])
    
        day_value += day - 1
        week_value=(day_value+int(day_first))%7
        Week_Day=week_days[week_value]
    return Week_Day

date = input("Input a date in the MM/DD/YYYY format: ")
month=(date[:2])
day=int(date[3:5])
year=int(date[6:])

leap = leap_year(year)
valid = valid_date(month,day,year,leap)
day_first = jan_first(year)
Week_Day = week_day(month,day,day_first,leap,valid)
print(f'{date} is a {Week_Day}')
