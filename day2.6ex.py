#life in weeks
#Dont change the code below 👇
age = input ('What is your current age: ')
#Dont change the  code above👆
#write your code below this line 
max_years = 90
max_months = 90*12
max_weeks = 90*52
max_days = 90*365
your_years_left = (90-int(age))
your_months = (int(age)*12)
your_months_left = max_months - your_months
your_weeks = (int(age) *52 )
your_weeks_left = max_weeks - your_weeks
your_days = (int(age)*365)
your_days_left = max_days - your_days
print(your_months)
print(f'your age is {age }years old,you are remaining with{your_years_left }years,{your_months_left }months,{your_weeks_left  }weeks, and {your_days_left }days')