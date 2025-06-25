#Dont change the code below👇
year = int(input('Which year do you want to check  \n'))
#Dont change the code above👆
if year % 4 == 0:
    print('it is a leap year')
elif year % 100 ==0:
    print('it is not a leap year')
elif year % 400==0:
    print('it is a leap year')
else:
    print('it is not a leap year')

#corrections
#by use of a flow chart
year = int(input('Which year do you want to check  \n'))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400==0:
            print('Not a leap year')
        else:
            print('leap year')
else:
    print('not leap year')

    
