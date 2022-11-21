date_of_birth=int(input("date of birth:"))
month_of_birth=int(input("month of birth:"))
year_of_birth=int(input("year of birth:"))
current_day=int(input("current day:"))
current_month=int(input("current month:"))
current_year=int(input("current year:"))
year=current_year-year_of_birth
if current_month>month_of_birth:
    month=current_month-month_of_birth
else:
    month=month_of_birth-current_month
if current_day>date_of_birth:
    day=current_day-date_of_birth
else:
    day=date_of_birth-current_day
if year_of_birth<2020:
    day=day+1
    if year<2016:
        day=day+1
        if year<2012:
            day=day+1
            if year<2008:
                day=day+1
                if year<2004:
                    day=day+1
                    if year<2000:
                        day=day+1
print("your age is",day,"days",month,"months",year,"years")