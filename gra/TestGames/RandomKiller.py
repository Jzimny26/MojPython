from gra.Engine import Attack

from gra.Models import Characters
from gra.Engine import Heal


def Graj():
    Player = Characters.Character('Geralt', 400, 80, 30)
    Player.CritChance = 35



    MonsterName = 'Strzyga'
    MonsterHP = 150
    MonsterPower = 20
    MonsterDefense = 8

    killedMonsters = 0

    Monster = Characters.Character(MonsterName, MonsterHP, MonsterPower, MonsterDefense)

    while Player.HP > 0:
        Attack.MeleeAttack(Player, Monster)
        if Monster.HP > 0:
            Attack.MeleeAttack(Monster,Player)
        else:
            Heal.Healing(Player)
            killedMonsters = killedMonsters + 1
            Monster = Characters.Character(MonsterName, MonsterHP, MonsterPower, MonsterDefense)














    print(f'{Player.Name} zabił {killedMonsters} potworów typu {MonsterName}!')

