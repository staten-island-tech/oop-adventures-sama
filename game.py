from classes import *

def start_game():
    print('Welcome Traveler!')
    print('Along with your brother, you are an avid explorer from another dimension.')
    print('You have just set foot on Teyvat.')
    print('After your arrival, however, you encounter an unexpected disaster which causes the separation of you and your brother.')
    print('You must complete this journey and fight these hilichurls, or monsters, along the way to find your brother.')   

while True:
    user_input = input('Do you wish to continue? (yes/no)')
        
    if user_input == 'yes':
        print('Great!')
        name = input('Lets start with your name:')
        name = Traveler(name)
        print('Good luck and may your journey begin.')
        start_game = True
    elif user_input == 'no':
        print('Some other time then :((')
        break
    else:
        print('Please type a valid answer.')

if Traveler.hp > 0:
                    enemy_attack()
                if Traveler.hp <= 0:
                    print("text for testing2")
                    break
                if enemy.health > 0 and Pers.health > 0:
                    main_attack()
                if enemy.health <= 0:
                    enemys.remove(enemy)
                    break
            elif answer == "2":
                Pers.walk()
                break
            elif answer == "3":
                Pers.reverse_walk()
                break
game_over = True
while (game_over is True):
    if Traveler.hp < 1 and Enemy.hp > 0:
        print('Defeated')
    elif Enemy.hp < 1 and Traveler.hp > 0:
        print('Victory!!')
    elif Traveler.hp < 1 and Enemy.hp < 1:
        print('Draw')
start_game()