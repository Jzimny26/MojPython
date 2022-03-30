from gra.TestGames import RandomKiller

import random
from gra.Models import Characters
from gra.Engine import Attack
import time

def Healing(Player :Characters.Character):
        Player.HP = Player.HP + Player.HealAmount
        Attack.Timesleep()
        print(f'{Player.Name} wyleczył {Player.HealAmount} obrażeń!')


def Lifesteal(Monster :Characters.Character, Player :Characters.Character):
       if Player.HP > 0:
        Monster.HP = Monster.HP + Player.HP/50
        Attack.Timesleep()
        print(f'Potwór wyleczył {round(Player.HP/50,2)} obrażeń')






