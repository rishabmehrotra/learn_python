from sys import exit

def gold_room():
    choice = input("> ")
    if('0' == choice or '1' in choice):
        how_much = int(choice)
    else:
        dead("Man learn to type a number...")
    if(how_much < 50):
        print("nice")
        exit(0)
    else:
        dead("You are greedy bastard")

def bear_room():
    print("There is a bear in the room")
    bear_moved = False

    while True:
        choice = input("> ")
        if(choice == 'take honey'):
            print('The bear looks at you then slaps your face off.')
        elif(choice == 'taunt bear' and not bear_moved):
            print('The bear has moved from the door.')
            print('You can go through it now.')
            bear_moved = True
        elif(choice == "taunt bear" and bear_moved):
            dead('The bear gets pissed off and chews your leg off.')
        elif(choice == 'open door' and bear_moved):
            gold_room()
        else:
            print("No idea")

def cthulhu_room():
    print('Here you see the great evil Cthulhu.')
    print('He, it, whatever stares at you and you go insane.')
    print('Do you flee for your life or eat your head?')
    choice = input('> ')
    if('flee' in choice):
        start()
    elif('head' in choice):
        dead('Well that was tasty!')
    else:
        cthulhu_room()

def dead(why):
    print(why, 'Good Job')
    exit(0)

def start():
    print('You are in a dark room.')
    print('There is a door to your right and left.')
    print('Which one do you take?')
    choice = input('> ')

    if(choice == 'left'):
        bear_room()
    elif(choice == 'right'):
        cthulhu_room()
    else:
        print("you die")
start()