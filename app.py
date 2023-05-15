class char:
    def __init__(self, name):
        self.name = name

class Main(char):
    def __init__(self, name, region, status, weapon):
        super().__init__(name)
        self.region = region
        self.status = status
        self.weapon = weapon
    def __str__(self):
        return f'{self.name}, {self.region}, {self.status}, {self.weapon}'
    Lumine = ('Lumine, Teyvat, main playable protagonist, sword')
    print(Lumine)

class Player_1(Main):
    def __init__(self, name, region, status, weapon, element):
        super().__init__(name, region, status, weapon)
        self.element = element
    def __str__(self):
        return f'{self.name}, {self.region}, {self.status}, {self.weapon}, {self.element}'
    Chongyun = ('Chongyun, Liyue, playable four star, claymore, cryo/ice')
    print(Chongyun)

class Player_2(Player_1):
    def __init__(self, name, region, status, weapon, element):
        super().__init__(name, element, region, status, weapon)
    def show(self):
        print('Name:', self.name, 'Element:', self.element, 'Region:', self.region, 'Status:', self.status, 'Weapon', self.weapon)
    def __str__(self):
        return f'{self.name}, {self.region}, {self.status}, {self.weapon}, {self.element}'
    Yoimiya = ('Yoimiya, Inazuma, playable five star, bow, pyro/fire')
    print(Yoimiya)