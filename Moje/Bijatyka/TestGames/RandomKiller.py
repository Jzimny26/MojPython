import random

from gra.Engine import Attack, Heal
from gra.Models import CharacterBase, Potion, Weapon

def GenerujPotwora():
    MonsterName = 'Strzyga'
    MonsterHP = random.randint(50, 200)
    MonsterPower = random.randint(10, 30)
    MonsterRange = 0
    MonsterDefense = random.randint(0, 15)
    Monster = CharacterBase.Character(MonsterName, MonsterHP, MonsterPower, MonsterRange, MonsterDefense)
    return Monster

def GenerujMiksturki(iloscMiksturek: int):
    potionName = "Superancka mikstura"
    potionDescription = "Mikstura ktora cos robi"
    potions = []
    for x in range(iloscMiksturek):
        hp = random.randint(1,100)
        power = random.randint(1,30)
        mikstura = Potion.Potion(potionName,
                                 1,
                                 potionDescription,
                                 hp,
                                 power)
        potions.append(mikstura)

    return potions

def GenerujGracza():
    """
    Generuje standardowego gracza o imieniu Geralt
    :return: Zwraca obiekt typu Character
    """
    Player = CharacterBase.Character('Geralt', 400, 80, 30, 15)
    Player.CritChance = 35

    iloscMiksturek = random.randint(1,10)
    miksturki = GenerujMiksturki(iloscMiksturek)

    Player.Equipment += miksturki

    return Player

def UseEq(player: CharacterBase.Character):
    if len(player.Equipment) > 0 :
        itemek = player.Equipment.pop(0)
        czyToJestMiksturka = isinstance(itemek, Potion)
        czyToJestMiecz = isinstance(itemek, Weapon)
        if czyToJestMiksturka :
            itemek.UsePotion(player)
            print(f"###### UŻYTO POTKI I DODANO {itemek.HP} ZYCIA ORAZ {itemek.Power} MOCY")
        if czyToJestMiecz :
            print("Zajebiscie, uzyles miecza!")


def TryToUsePotion(player: CharacterBase.Character):
    chance = random.randint(0, 100)
    if chance <= 35 :
        UseEq(player)

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
            Attack.MeleeAttack(Monster, Player)
        else:
            #Heal.Healing(Player)
            TryToUsePotion(Player)
            killedMonsters = killedMonsters + 1
            Monster = GenerujPotwora()
    return killedMonsters

def Graj():
    Player = GenerujGracza()
    Monster = GenerujPotwora()
    killedMonsters = Rozgrywka(Player, Monster)
    print(f'{Player.Name} zabił {killedMonsters} potworów typu {Monster.Name}!')