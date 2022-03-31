from Models import ItemBase

class Potion(ItemBase):
    def __init__(self, Name, Weight: float, Description, HP, Power):
        self.ItemBase.__init__(self, Name, Weight, Description)
        self.HP = HP
        self.Power = Power