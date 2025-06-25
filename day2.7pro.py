#TIP CALCULATOR PROJECT
('Welcome to the tip calculator.')
t_b = input('What is the total bill?  ')
p_t = input('What percentage tip would you like to give? 10, 12, or 15?  ')
n_p = input(' How many people to split the bill?  ')
p = 100
a = float(p_t)/ float(p)
b = float(a) * float(t_b)
e_p = float(b) / float(n_p)
a_e_p = print(round(e_p,2)) 
print(f'Each person will pay {a_e_p}')
#print(round(e_p,2))------> rounding to 2 decimal points


#SOUCECODE ACCORDING TO LESSON
print('Welcome to the tip calculator!')
bill = float(input('What was the total bill?  $'))
tip = int(input('hOW many tip would you like to give? 10, 20 ,15? '))
people = int(input('How many people to split the bill?'))
tip_as_percentage = tip / 100 
total_tip_amount = bill * tip_as_percentage
total_bill = bill + bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person,2)
print(f'Each person should pay: {final_amount}$')
 
