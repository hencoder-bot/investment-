print('Welcome to the Work Limiter.\nWe will determine the total number of days you are supposed to work and allow you to choose a number of given days for extra work or overtime.\nFailure to comply with the given rules will lead to a red card or dismissal.\nThe normal work days will be assigned with a blue card, and with fewer days, we will assign you a green card.\nThank you for visiting the Alternate Strategic Labour Determiner.')

# Get user inputs
total_days = int(input('Enter the total number of days you are supposed to work: '))
over_time = int(input('Enter the number of days you worked for overtime: '))

# Define normal working days per week
normal_days_per_week = 4

# Calculate total normal working days in a month (assuming 4 weeks in a month)
total_normal_days = normal_days_per_week * 4

# Calculate total days including overtime
total_days_with_overtime = total_normal_days + over_time

# Print the total days including overtime
print(f'Total days including overtime: {total_days_with_overtime}')

# Determine the card color based on the total days including overtime
if total_days_with_overtime <= 20:
    print('Green card')
elif 21 <= total_days_with_overtime <= 22:
    print('Orange card')
else:
    print('Red card')