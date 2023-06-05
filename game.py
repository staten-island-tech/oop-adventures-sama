from classes import *

def start_game():
    print('Welcome Traveler!')
    print('Along with your brother, you are an avid explorer from another dimension.')
    print('You have just set foot on Teyvat.')
    print('After your arrival, however, you encounter an unexpected disaster which causes the separation of you and your brother.')
    print('You must complete this journey fight these hilichurls, or monsters, along the way.')
    name = input('Lets start with your name:')
    name = Traveler(name)
    print('Good luck and may your journey begin.')

game_over = True
while (game_over is True):
    if Traveler.hp < 1 and Enemy.hp > 0:
        print('Defeated')
    elif Enemy.hp < 1 and Traveler.hp > 0:
        print('Victory!!')
    elif Traveler.hp < 1 and Enemy.hp < 1:
        print('Draw')
start_game()