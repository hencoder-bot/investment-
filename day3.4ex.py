#BMI Calculator
#Write a prograame that interprets the body mass index(BMI) based on a users weight 
#and height.
#it should tell them the interpretation of their BMI value
#under 18.5 they are underweight
#over 18.5 but below 25 they have a normal weight
#over 25 but below 30 they are over weight
#over 30 but below 35 they ate obase
#above 35 they are clinically obase

#Dont change the code below👇
height = float(input('enter your height in m:  '))
weight = float(input('enter your weight in kg: '))
#Dont change the code above👆
#Write your code below this line
bmi = round(float(weight) / float(height**2))
print(bmi)
if bmi <18.5:
    print('You are underweight.')
elif bmi> 18.5 and bmi <= 25:
    print('You have normal weight ')
elif bmi > 25  and bmi <= 30:
    print('You have over weight ')
elif bmi >30 and bmi <= 35:
    print('You are obase ')
else:
        print('you are clinically obase')


        #corrections
height = float(input('enter your height in m:  '))
weight = float(input('enter your weight in kg: '))
bmi = round(weight / weight **2)
if bmi < 18.5:
     print(f'Your bmi is {bmi}, you are underweight.')
elif bmi <25:
     print(f'Your bmi is {bmi}, you are normal weight.')
elif bmi < 30:
     print(f'Your bmi is {bmi}, you are overweight.')
elif bmi <35:
     print(f'Your bmi is {bmi}, you are obase.')
else:
     print(f'Your bmi is {bmi}, you are clinically obase.')
     

