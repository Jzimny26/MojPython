from gra.Models import ItemBase, CharacterBase

class Potion(ItemBase):
    def __init__(self, Name, Weight: float, Description, HP, Power):
        """

        :param Name:
        :param Weight:
        :param Description:
        :param HP:
        :param Power:
        """
        self.ItemBase.__init__(self, Name, Weight, Description)
        self.HP = HP
        self.Power = Power

    def UsePotion(self, Character: CharacterBase):
        Character.HP += self.HP
        Character.Power += self.Power