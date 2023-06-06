import random 

class Weapon:
    def __init__(self, name, rarity, damage, type):
        self.name = name
        self.rarity = rarity
        self.damage = damage
        self.type = type
    def __str__(self):
        return f'{self.name}, {self.rarity}, {self.damage}, {self.type}'

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
        self.damage = 0
        self.weapon = 0
    def damage_taken(self, damage_amount):
        if damage_amount > self.hp:
            self.hp -= damage_amount
            self.hp = 0
    def weapon(self):
        weapon = {'Aquila Favonia':Aquila_Favonia, 'Deathmatch':Deathmatch, 'Aqua Simulacra':Aqua_Simulacra}
        print(random.choice(weapon))
    def dodge(self):
        self.hp += Enemy.damage
        print(f'{self.name} successfully dodged {Enemy.name}\'s attack')
    def damage(self):
        Enemy.hp -= self.damage
        print(f'{self.damage} damage done to {Enemy.name}')

class Enemy:
    def __init__(self, name):
        self.name = name
        self.hp = 70
        self.damage = 0
    def damage_taken(self, damage_amount):
        if damage_amount > self.hp:
            self.hp -= damage_amount
            self.hp = 0
    def damage(self):
        Traveler.hp -= self.damage
        print(f'{self.damage} damage done to {Traveler.name}')

class Hilichurl(Enemy):
    def __init__(self):
        super().__init__(name='Hilichurl', hp='60', damage='15') 

class Hilichurl_Shooter(Enemy):
    def __init__(self):
        super().__init__(name='Hilichurl Shooter', hp='70', damage='25')

class Unusual_Hilichurl(Enemy):
    def __init__(self):
        super().__init__(name='Unusual Hilichurl', hp='85', damage='20')
                                                                        

        