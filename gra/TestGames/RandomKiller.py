import random

from gra.Engine import Attack, Heal
from gra.Models import Characters

def GenerujPotwora():
    MonsterName = 'Strzyga'
    MonsterHP = random.randint(50, 200)
    MonsterPower = random.randint(10, 30)
    MonsterRange = 0
    MonsterDefense = random.randint(0, 15)
    Monster = Characters.Character(MonsterName, MonsterHP, MonsterPower, MonsterRange, MonsterDefense)
    return Monster

def GenerujGracza():
    """
    Generuje standardowego gracza o imieniu Geralt
    :return: Zwraca obiekt typu Character
    """
    Player = Characters.Character('Geralt', 400, 80, 30, 15)
    Player.CritChance = 35
    return Player

def Rozgrywka(Player, Monster):
    """
    Funkcja rozpoczyna losową rozgrywkę. Wynikiem jest zabita ilość potworów przez danego gracza
    :param Player: Gracz główny
    :param Monster: Typ potwora uczesniczący w potyczce
    :return: Zabita ilość potworów (int)
    """
    killedMonsters = 0

    while Player.HP > 0:
        Attack.MeleeAttack(Player, Monster)
        if Monster.HP > 0:
            Attack.MeleeAttack(Monster,Player)
        else:
            Heal.Healing(Player)
            killedMonsters = killedMonsters + 1
            Monster = GenerujPotwora()
    return killedMonsters

def Graj():
    Player = GenerujGracza()
    Monster = GenerujPotwora()
    killedMonsters = Rozgrywka(Player, Monster)
    print(f'{Player.Name} zabił {killedMonsters} potworów typu {Monster.Name}!')