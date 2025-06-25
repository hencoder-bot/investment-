print('Welcome to Treasure Island\nYour mission is to find the hidden tresasure in the island')
doors = input('select the door you want to use....... right or left \n');{"right","left"}
if doors == "right":
    print("Game over")
elif doors == "left":
 activities=input('select whach activity you would like to have on your quest........ swim or wait \n');{"swim","wait"}
if activities== "swim":
    print('game over')
elif activities == "wait":
 final_door = input('Your are abaut to grab your treasur.. which door will you like to use........ red,blue or yellow \n');{"red","blue","yellow"}
if final_door== "red":
 print('Game over , you fell in a burning bush...')
elif final_door ==  "blue":
 print('Game over, you fell in high moving running river')
elif final_door== "yellow":
 print("Congragulations you win...check for your treasure below")
 print("""
    *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-""_ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
""")
else:
  print("You choose the door that doesnt exist")
 
#corrections
print('welcome to treasure island')
print('Your mission is to find the treasure')
choise1=input('You\'re at a crossroad, where do you want to go? Type "left" or "right".').lower()
if choise1 == "left":
  choises2=input('you\'ve come to a lake. there is an island in the middle of the lake.Type "wait" to wait foe a boat. Type "swim"to swim across').lower()
if choises2 == "wait":
  chioses3 = input("You arrive at the Island unharead. there is a house with 3 doors. one red, one yellow and one blue.Which colour do you choose?").lower()
  if chioses3 == "red":
    print("its a room full of fire Game over")
  elif chioses3 == "yellow":
    print("You found the treasure youo win")
  elif chioses3 == "blue":
    print("You enter a room of beasts. Game over.")
else:
  print("you choose the door that doesnt exista. Game over")


  



    



