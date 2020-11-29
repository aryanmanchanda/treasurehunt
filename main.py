print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
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
''')
print(
    "welcome to the treasure hunt:be ready to face the most deadly adventure::"
)
print("we will guide you according to the choices you made::")
choice_1 = input(
    'you are at the edge of a road it only has two turns left or right where you wanna go:: "right" or "left":: '
).lower()
if choice_1 == "left":
    choice_2 = input(
        '"you have came across a river end what will you do "swim" or "wait"::'
    ).lower()
    if choice_2 == "wait":
        choice_3 = input(
            'you reached a house on the island unharmed:you have three doors"red":"white":"green" whcich door will you choose to enter::'
        ).lower()
    if choice_3 == "red":
        print("YOU BURNT IN FIRE :GAME OVER::")
    elif choice_3 == "white":
        print("YOU WE ATTACKED BY A CROSBOW AND YOU DIED::")
    else:
        print(
            "YOU FINALLY FOUND YOUR TREASURE :HAVE FUN WITH LANA RHOADES AND SKYLAR VOX::"
        )

else:
    print("a crocodile ate you::ITS GAME OVER::")

if choice_1 == "right":
    print("GAME OVER: you met a car accident::")
