import random 
print('Welcome Traveler!')
print('Along with your brother, you are an avid explorer from another dimension.')
print('You have just set foot on Teyvat.')
print('After your arrival, however, you encounter an unexpected disaster which causes the separation of you and your brother.')
print('You must complete this journey fight these hilichurls, or monsters, along the way.')
print('Lets start with your name:')
name = input()
print('Good luck and may your journey begin.')

class Weapon:
    def __init__(self, name, rarity, damage, type):
        self.name = name
        self.rarity = rarity
        self.dmg = damage
        self.type = type
    def __str__(self):
        return f'{self.name}, {self.rarity}, {self.dmg}, {self.type}'

class Aquila_Favonia(Weapon):
    def __init__(self):
        super().__init__(name='Aquila Favonia', rarity='5 star', damage='38', type='sword')

class Deathmatch(Weapon):
    def __init__(self):
        super().__init__(name='Deathmatch', rarity='4 star', damage='31', type='polearm')

class Aqua_Simulacra(Weapon):
    def __init__(self):
        super().__init__(name='Aqua Simulacra', rarity='5 star', damage='34', type='bow')

class Traveler:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack = 0
        self.weapon = 0
    def attack(self):
        self.hp
    def weapon(self):
        weapon = {'Aquila Favonia':Aquila_Favonia, 'Deathmatch':Deathmatch, 'Aqua Simulacra':Aqua_Simulacra}
        print(random.choice(weapon))
    def dodge(self):
        self.hp += Enemy.attack
        print(f'{self.name} successfully dodged {Enemy.name}\'s attack')
    def attack(self):
        Enemy.hp -= self.attack
        print(f'{self.attack} damage done to {Enemy.name}')

class Enemy:
    def __init__(self, name):
        self.name = name
        self.hp = 70
        self.attack = 0
    def attack(self):
        Traveler.hp -= self.attack
        print(f'{self.attack} damage done to {Traveler.name}')

class Hilichurl(Enemy):
    def __init__(self):
        super().__init__(name='Hilichurl', hp='60', damage='15') 

class Hilichurl_Shooter(Enemy):
    def __init__(self):
        super().__init__(name='Hilichurl Shooter', hp='70', damage='25')

class Unusual_Hilichurl(Enemy):
    def __init__(self):
        super().__init__(name='Unusual Hilichurl', hp='85', damage='20')
                                                                        
class Game:

    def result(self):
        if Traveler.hp < 1 and Enemy.hp > 0:
            self.game_over = True
            print('Defeated')
        elif Enemy.hp < 1 and Traveler.hp > 0:
            self.game_over = True
            print('Victory!!')
        elif Traveler.hp < 1 and Enemy.hp < 1:
            self.game_over = True
        print('Draw')
        