#imie, HP, Sila ataku,
from gra.Models import ItemBase

class Character:
    def __init__(self, Name, HP: float, Power, RangePower, Defense: int):
        self.Name = Name
        self.HP = HP
        self.Power = Power
        self.CritChance = 15
        self.CritMultiplier = 2.0
        self.Defense = Defense
        self.HealChance = 20
        self.HealAmount = 15
        self.RangePower = RangePower
        self.MeleeChance = 50
        self.Equipment = []

    def AddItemToEquipment(self, Item: ItemBase):
        self.Equipment.append(Item)



