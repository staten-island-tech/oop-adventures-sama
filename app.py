import random

print('Welcome Traveler!')
print('Along with your brother, you are an avid explorer from another dimension.')
print('You have just set foot on Teyvat.')
print('After your arrival, however, you encounter an unexpected disaster which causes the separation of you and your brother.')
print('You have to cross three regions--Monstadt, Liyue, and Inazuma, and find clues about your brother. You may find hilichurls, or monsters, along the way')
print('Lets start with your name:')
name = input()
print('Good luck and may your journey begin.')

class Item:
    def __init__(self, name, rarity):
        self.name = name
        self.rarity = rarity
    def __str__(self):
        return f'{self.name}, {self.rarity}'

class Weapon(Item):
    def __init__(self, name, rarity, damage, type):
        self.dmg = damage
        self.type = type
        super().__init__(name, rarity, damage, type)
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

class Main:
    def __init__(self, name, status, weapon):
        self.name = name
        self.status = status
        self.weapon = weapon
    def __str__(self):
        return f'{self.name}, {self.status}, {self.weapon}'
    Traveler = ( status='main playable protagonist', weapon='random.choice')

weapon_list = [Aquila_Favonia, Aqua_Simulacra, Deathmatch]
print(random.choice(weapon_list))


