class char:
    def __init__(self, name, element):
        self.name = name
        self.element = element

class Main(char):
    def __init__(self, name, element, region, status):
        super().__init__(name, element)
        self.region = region
        self.status = status
    def show(self):
        print('Name:', self.name, 'Element:', self.element, 'Region:', self.region, 'Status:', self.status)
    
    Lumine = char('Lumine', 'anemo', 'Teyvat', 'main playable protagonist')

class Player_1(Main):
    def __init__(self, name, element, region, status):
        super().__init__(name, element, region, status)
    def show(self):
        print('Name:', self.name, 'Element:', self.element, 'Region:', self.region, 'Status:', self.status)
    
    Chongyun = char('Chongyun', 'cryo', 'Liyue', 'playable four star')

class Player_2(Player_1):
    def __init__(self, name, element, region, status, privileges):
        super().__init__(name, element, region, status)
        self.privileges = privileges
    def show(self):
        print('Name:', self.name, 'Element:', self.element, 'Region:', self.region, 'Status:', self.status, 'Privileges', sel)