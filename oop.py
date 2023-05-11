class char:
    def __init__(self, name, element):
        self.name = name
        self.element = element

class Main_char:
    def __init__(self, name, element, region, status, weapon):
        super().__init__(name, element)
        self.region = region
        self.status = status
        self.weapon = weapon
    def show(self):
        print('Name:', self.name, 'Element:', self.element, 'Region:', self.region, 'Status:', self.status, 'Weapon', self.weapon)
    
    Lumine = char('Lumine', 'anemo/wind', 'Teyvat', 'main playable protagonist', 'sword')

class Player_1_Main:
    def __init__(self, name, element, region, status, weapon):
        super().__init__(name, element, region, status, weapon)
    def show(self):
        print('Name:', self.name, 'Element:', self.element, 'Region:', self.region, 'Status:', self.status, 'Weaapon', self.weapon)
    
    Chongyun = char('Chongyun', 'cryo/ice', 'Liyue', 'playable four star', 'claymore')

class Player_2_Player_1:
    def __init__(self, name, element, region, status, weapon):
        super().__init__(name, element, region, status, weapon)
    def show(self):
        print('Name:', self.name, 'Element:', self.element, 'Region:', self.region, 'Status:', self.status, 'Weapon', self.weapon)

    Yoimiya = char('Yoimiya', 'pyro/fire', 'Inazuma', 'playable five star', 'bow')