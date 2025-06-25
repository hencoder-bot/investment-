print('THE LOAN PAYMENT SYSTEM @ OPROHEN THE DATA SCIENTIST\nWelcome to the Loan Payment System, Relieve yourself from being cheated by different loan lending companies ...\nDiscover the hidden tricks the lending Companies are using to cheat you with an aim of assisting and helping you.\nDiscover the fastest way to pay your loan in the shortest period and save the extra cash. the different money lenders steal from you....\nWELCOME TO THE LOAN PAYMENT SYSTEM FOLLOW THE PROMPTS BELOW AS WE HELP YOU OUT')
print('In consideration of Simple Interest, here is the best way we can help you out')

# Get user inputs
principal = float(input('How much is the amount of loan are you willing to get or have gotten already? '))
interest_rate = float(input('What is the agreed interest rate of your loan (in %)? '))
interest_rate /= 100  # Convert percentage to decimal
time = float(input('How long do you want to pay the loan (in years)? '))
fav_pay_amount = input('Would you want us to give you the amount to help you pay the loan in the shortest period? Yes or No? ')

# Calculate simple interest7t
simple_interest = principal * interest_rate * time
total_amount = principal + simple_interest

print(f"\nThe simple interest on your loan is: {simple_interest}")
print(f"The total amount to be paid after {time} years is: {total_amount}")

if fav_pay_amount.lower() == 'no':
    monthly_payment = float(input('May we know how much you are comfortable with paying your loan considering per month? '))
    # Calculate the number of months needed to pay off the loan
    months_needed = total_amount / monthly_payment
    print(f"You will need approximately {months_needed:.2f} months to pay off the loan.")
else:
    # Calculate the monthly payment needed to pay off the loan in the given period
    monthly_payment = total_amount / (time * 12)
    print(f"You need to pay approximately {monthly_payment:.2f} per month to pay off the loan in {time} years.")

# Ask user for payment system preference
payment_system = input('Which payment system would you like to use? (monthly/bi-weekly): ').strip().lower()

if payment_system == 'monthly':
    # Calculate monthly payment
    monthly_payment = total_amount / (time * 12)
    print(f"You need to pay approximately {monthly_payment:.2f} per month to pay off the loan in {time} years.")
    print("You can also consider using a bi-weekly payment system to pay off your loan faster.")
elif payment_system == 'bi-weekly':
    # Calculate monthly payment
    monthly_payment = total_amount / (time * 12)
    # Calculate bi-weekly payment
    bi_weekly_payment = monthly_payment / 2
    print(f"With a bi-weekly payment system, you need to pay approximately {bi_weekly_payment:.2f} every two weeks.")
    # Calculate the total number of bi-weekly payments
    total_bi_weekly_payments = time * 26  # 26 bi-weekly payments per year
    print(f"The total number of bi-weekly payments over {time} years is: {total_bi_weekly_payments}")
    total_months = total_bi_weekly_payments / 2
    print(f"This is equivalent to approximately {total_months:.2f} months.")
    # Calculate savings over monthly system
    total_monthly_payments = time * 12
    savings = (total_monthly_payments - total_months) * monthly_payment
    print(f"By using the bi-weekly payment system, you will save approximately {savings:.2f} over the monthly payment system.")
else:
    print("Invalid selection. Please choose either 'monthly' or 'bi-weekly'.")

print('Notes on Bi-Weekly Payment System according to "The Automatic Millionaire"\nThe bi-weekly payment system involves making half of your monthly mortgage payment every two weeks.\nThis results in 26 half-payments per year, which is equivalent to 13 full monthly payments instead of 12.\nThis extra payment helps reduce the principal balance faster, thereby reducing the total interest paid over the life of the loan and shortening the loan term.\n Advantages of Bi-Weekly Payment System:\n Faster Loan Repayment: By making an extra payment each year, you reduce the principal balance more quickly, which shortens the loan term.\n Reduced Interest Costs: Paying down the principal faster reduces the amount of interest you pay over the life of the loan.\n Easier Budgeting: Smaller, more frequent payments can be easier to manage and align with bi-weekly paychecks.\n Builds Equity Faster: Reducing the principal balance faster helps you build equity in your home more quickly.')