#imie, HP, Sila ataku,

class Character:
    def __init__(self, Name, HP: float, Power, Defense: int ):
        self.Name = Name
        self.HP = HP
        self.Power = Power
        self.CritChance = 15
        self.CritMultiplier = 2.0
        self.Defense = Defense