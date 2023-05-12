class char:
    def __init__(self, name):
        self.name = name

class Main(char):
    def __init__(self, name, region, status, weapon):
        super().__init__(name)
        self.region = region
        self.status = status
        self.weapon = weapon
    def show(self):
        print('Name:', self.name,'Region:', self.region, 'Status:', self.status, 'Weapon', self.weapon)
    
    Lumine = char('Lumine', 'Teyvat', 'main playable protagonist', 'sword')

class Player_1(Main):
    def __init__(self, name, region, status, weapon, element):
        super().__init__(name, region, status, weapon)
        self.element = element
    def show(self):
        print('Name:', self.name, 'Element:', self.element, 'Region:', self.region, 'Status:', self.status, 'Weaapon', self.weapon)
    
    Chongyun = Main('Chongyun', 'cryo/ice', 'Liyue', 'playable four star', 'claymore')

class Player_2(Player_1):
    def __init__(self, name, element, region, status, weapon):
        super().__init__(name, element, region, status, weapon)
    def show(self):
        print('Name:', self.name, 'Element:', self.element, 'Region:', self.region, 'Status:', self.status, 'Weapon', self.weapon)

    Yoimiya = Player_1('Yoimiya', 'pyro/fire', 'Inazuma', 'playable five star', 'bow')