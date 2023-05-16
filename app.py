print('Welcome Traveler!')
print('Along with your brother, you are an avid explorer from another dimension.')
print('You have just set foot on Teyvat.')
print('After your arrival, however, you encounter an unexpected disaster which causes the separation of you and your brother.')
print('You have to cross three regions--Monstadt, Liyue, and Inazuma, and find clues about your brother. You may find hilichurls, or monsters, along the way')
print('Lets start with your name:')
name = input()
print('Good luck and may your journey begin.')

class Main:
    def __init__(self, name, region, status, weapon):
        self.name = name
        self.region = region
        self.status = status
        self.weapon = weapon
    def __str__(self):
        return f'{self.name}, {self.region}, {self.status}, {self.weapon}'
    Traveler = ('Traveler, unknown, main playable protagonist, sword')
    print(Traveler)

class NPC_1(Main):
    def __init__(self, name, region, status, weapon, element):
        super().__init__(name, region, status, weapon)
        self.element = element
    def __str__(self):
        return f'{self.name}, {self.region}, {self.status}, {self.weapon}, {self.element}'
    Chongyun = ('Chongyun, Liyue, npc, claymore, cryo/ice')
    print(Chongyun)

class NPC_2(NPC_1):
    def __init__(self, name, region, status, weapon, element):
        super().__init__(name, element, region, status, weapon)
    def show(self):
        print('Name:', self.name, 'Element:', self.element, 'Region:', self.region, 'Status:', self.status, 'Weapon', self.weapon)
    def __str__(self):
        return f'{self.name}, {self.region}, {self.status}, {self.weapon}, {self.element}'
    Yoimiya = ('Yoimiya, Inazuma, npc, bow, pyro/fire')
    print(Yoimiya)

class NPC_3(NPC_2):
    def __init__(self, name, region, status, weapon, element):
        super().__init__(name, element, region, status, weapon)
    def show(self):
        print('Name:', self.name, 'Element:', self.element, 'Region:', self.region, 'Status:', self.status, 'Weapon', self.weapon)
    def __str__(self):
        return f'{self.name}, {self.region}, {self.status}, {self.weapon}, {self.element}'
    Jean = ('Jean, Monstadt, npc, sword, anemo/wind')
    print(Jean)