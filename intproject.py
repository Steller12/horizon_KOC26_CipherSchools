#taking input from user
date_of_birth=int(input("date of birth:"))
month_of_birth=int(input("month of birth:"))
year_of_birth=int(input("year of birth:"))
current_day=int(input("current day:"))
current_month=int(input("current month:"))
current_year=int(input("current year:"))
#years between year or birth and current year
year=current_year-year_of_birth
#getting month and day in positive
if current_month>month_of_birth:
    month=current_month-month_of_birth
else:
    month=month_of_birth-current_month
if current_day>date_of_birth:
    day=current_day-date_of_birth
else:
    day=date_of_birth-current_day
    month=month-1
#logic to add days for leap years one by one
for i in range(year_of_birth,current_year+1):
    if i % 400 == 0  or (i % 4 == 0 and i % 100 != 0):
        day=day+1
print("your age is",day,"days",month,"months",year,"years")