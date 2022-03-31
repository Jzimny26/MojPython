from Models import ItemBase

class Weapon(ItemBase):
    def __init__(self, Name, Weight: float, Description, Power):
        ItemBase.__init__(self, Name, Weight, Description)
        self.Power = Power