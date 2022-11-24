#taking input from user in dd/mm/yyyy
birth_date = input('Enter your birth date in the following format DD/MM/YYYY:')
current_date = input('Enter your current date in the following format DD/MM/YYYY:')
birth_day = int(birth_date.split('/')[0])
birth_month = int(birth_date.split('/')[1])
birth_year = int(birth_date.split('/')[2])

#splitting the input to use in logical operations
current_year = int(current_date.split('/')[2])
current_month = int(current_date.split('/')[1])
current_day = int(current_date.split('/')[0])

#empty variable to add all the days survived
days_survived = 0

#Days survived this year
for i in range(1,current_month):
    if i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12:
        days_survived+=31
    elif i==2:
        days_survived+=28
    else:
        days_survived+=30
days_survived+=current_day

#Days in the years(including leap years)
for j in range(birth_year+1,current_year):
    if j % 400 == 0  or (j % 4 == 0 and j % 100 != 0):
        days_survived=days_survived+366
    else:
        days_survived=days_survived+365

#days survived in the birth year
for k in range(birth_month,13):
    if k==1 or k==3 or k==5 or k==7 or k==8 or k==10 or k==12:
        days_survived+=31
    elif k==2:
        days_survived+=28
    else:
        days_survived+=30

#subtracting days before date of birth
days_survived-=birth_day
print(days_survived)