from Engine import Attack, Heal
from Models import Characters
from TestGames import RandomKiller

import time

Player = Characters.Character('Geralt', 250, 30, 35, 15)

Monster = Characters.Character('Strzyga', 60, 20, 0, 5)

print(f'Gracz o imieniu {Player.Name} ma {Player.HP} HP i {Player.Defense} punktów tarczy')

print(f"Gracz o imieniu {Monster.Name} ma {Monster.HP} HP i {Player.Defense} punktów tarczy, oraz 2% lifesteal'a")

Player.CritChance = 30

# while Player.HP > 0:
#     Attack.AttackChoice(Player, Monster)
#     if Monster.HP > 0:
#         time.sleep(2)
#         Attack.MeleeAttack(Monster,Player)
#         Heal.Lifesteal(Monster,Player)
#     elif Monster.HP <= 0 and Player.HP > 0:
#         Attack.Timesleep()
#         print(f'{Monster.Name} Nie żyje')
#         Attack.Timesleep()
#         print(f'Zwycięża {Player.Name}!')
#         break
#     elif Monster.HP > 0 and Player.HP <= 0:
#         Attack.Timesleep()
#         print(f'{Monster.Name} Nie żyje')
#         Attack.Timesleep()
#         print(f'Zwycięża {Player.Name}!')
#         break


def CzyJestWieksze(jeden, dwa):
    result = False
    if jeden > dwa:
        result = True
    return result

def PrzedstawSie(imie, nazwisko):
    tekscik = f'Cześć!\nNazywam się {imie} {nazwisko}!\nMiło Cię poznać!\n\n\n'
    return tekscik

print(CzyJestWieksze(5,3))
print(CzyJestWieksze(10,100))
print(CzyJestWieksze(50,51))
print(CzyJestWieksze(60,60))

print(PrzedstawSie('Sebastian', 'Krupa'))
print(PrzedstawSie('Jakub', 'Zimny'))


#RandomKiller.Graj()
