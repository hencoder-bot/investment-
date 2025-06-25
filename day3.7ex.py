#CODING EXERCISE PIZZA ORDER PROGRAME
#nstructtions
#you have got a job at python pizza. Your first job is to build an automatic pizza order program
#bassed on a users orders .work out the final bill
#small pizza--->$15
#medium pizza--->$20
#large pizza----->$25
#peparoni for small pizza---->+$2
#peparoni for medium pizza and large pizza----->+$3
#extra cheese for large pizza---->+$1
#Dont change the code below👇
print('Welcome to Python Deliveries!')
sieze = input('What sieze pizza do you want? S, M, or L \n')
add_peparoni = input('Do you want peparoni? Y or N \n')
extra_cheese = input('Do youo want extra cheese? Y or N \n')
#Dont change the code above👆
if sieze == 'S':
    price  = 15
    peparoni = 2
    cheese = 1
    if add_peparoni =='Y':
        general = price + peparoni
        if extra_cheese == 'Y':
            general= price + peparoni + cheese
elif sieze == 'M':
    price = 20
    peparoni = 3
    cheese = 1
    if add_peparoni == 'Y':
        general = price + peparoni
        if extra_cheese == 'Y':
            general= price + peparoni + cheese
elif sieze == 'L':
    price = 25
    peparoni = 3
    cheese = 1
    if add_peparoni=='Y':
        general = price + peparoni
        if extra_cheese == 'Y':
            general= price + peparoni + cheese
print(f'Your final bill is ${general}')

#CORRECTIONS POSSIBLE
print('Welcome to Python Deliveries!')
sieze = input('What sieze pizza do you want? S, M, or L \n')
add_peparoni = input('Do you want peparoni? Y or N \n')
extra_cheese = input('Do youo want extra cheese? Y or N \n')
bill = 0 
if sieze =='S':
    bill += 15
elif sieze == 'M':
    bill += 20
elif sieze == 'L':
    bill += 25
else:
    bill +=25

    if add_peparoni == 'Y':
        if sieze == 'S':
            bill += 2
        else:
            bill += 3

            if extra_cheese == 'Y':
                bill += 1

print(f'Your final bill is ${bill}')











