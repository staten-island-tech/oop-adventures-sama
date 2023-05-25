import random
print('Welcome Traveler!')
print('Along with your brother, you are an avid explorer from another dimension.')
print('You have just set foot on Teyvat.')
print('After your arrival, however, you encounter an unexpected disaster which causes the separation of you and your brother.')
print('You must complete this journey in order to find your brother. You may find hilichurls, or monsters, along the way.')
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
        super().__init__(name='Aquila Favonia', rarity='5 star', damage='48', type='sword')

class Deathmatch(Weapon):
    def __init__(self):
        super().__init__(name='Deathmatch', rarity='4 star', damage='41', type='polearm')

class Aqua_Simulacra(Weapon):
    def __init__(self):
        super().__init__(name='Aqua Simulacra', rarity='5 star', damage='44', type='bow')

class Traveler:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = 0
        weapon = {'Aquila Favonia':Aquila_Favonia, "Deathmatch":Deathmatch, 'Aqua Simulacra':Aqua_Simulacra}
        choice = random.choice(list(weapon.values()))
    
    def attack(self):
        return self.attack
    def take_dmg(self, damage):
        if self


class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.dmg = damage

class Hilichurl(Enemy):
    def __init__(self):
        super().__init__(name='Hilichurl', hp='60', damage='15') 

class Hilichurl_Shooter(Enemy):
    def __init__(self):
        super().__init__(name='Hilichurl Shooter', hp='70', damage='25')

class Unusual_Hilichurl(Enemy):
    def __init__(self):
        super().__init__(name='Unusual Hilichurl', hp='85', damage='30')







