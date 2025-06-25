#LOVE CALCULATOR
#instructions
#write a program that tests the compatibility between two people 
#we are going to use the super scientific method  recommended by Buzzfeed
#take both peoples names and check for the number of times the
#the letters in the word LOVE occurs . 
# Then combine numbers to make a 2 digit number.

#for love scores less than 10 or graeter than 90 , the message should be:
#"Your score is x , you go together like coke and mentos."

#for love scores between 40 and 50, the message should be:
#"Your score is y, you are alright together."

#otherwise, the message will just be their score e.g:
#"Your score is %"


#Dont change the code below👇
print('Welcome to the Love Calculator!')
name1 = input('What is your name?  \n')
name2 = input('What is their name? \n')
#Dont change the code above👆
#Write your code below this line👇
name11 =name1.lower()
name22 = name2.lower()
#for name 1
namea = (name11).count('t')
nameb = (name11).count('r')
namec = (name11).count('u')
named = (name11).count('e')

name110=(name11).count('l')
name111=(name11).count('o')
name112=(name11).count('v')
name113=(name11).count('e')
#for name 2
namee=(name22).count('t')
namef=(name22).count('r')
nameg=(name22).count('u')
nameh=(name22).count('e')

name220=(name22).count('l')
name221=(name22).count('o')
name222=(name22).count('v')
name223=(name22).count('e')

couple1 =(namea +nameb+namec+named+name110 + name111 + name112 + name113)
couple2 = (namee+namef+nameg+nameh+name220 + name221 + name222+ name223)
perfect_match = str(couple1) + str(couple2)
perfect_match1 = int(perfect_match)
if perfect_match1 < 10 and perfect_match1 > 90:
    print(f'Your score is{perfect_match1},you go together like coke and mentos.')
else:
 if perfect_match1>=40 and perfect_match1<= 50:
    print(f'Your score is {perfect_match1}% ,you are alright together.')
 else:
    print(f'Your score is {perfect_match1}%')


    #CORRECTIONS
print('Welcome to the Love Calculator!')
name1 = input('What is your name?  \n')
name2 = input('What is their name? \n')
combined_string = name1 + name2
lower_case_string = combined_string.lower()
t =lower_case_string.count('t')
r =lower_case_string.count('r')
u =lower_case_string.count('u')
e =lower_case_string.count('e')

true = t + r + u + e

l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')
love = l + o + v + e

love_score = str(true) + str(love)
int_score = int(love_score)
#or
#love_score = int(str(true) + str(love))
print(love)
if int(love_score<18) or int(love_score>90):
   print(f'Your love score is{love_score}, you go together like cock and mantos.')
elif (love_score>=40) and (love_score<=50):
   print(f'Your score is {love_score},You are alright together.')
else:
   print(f'Your score is {love_score} ')

    

                                 