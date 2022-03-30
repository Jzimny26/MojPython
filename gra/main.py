from Engine import Attack
from Models import Characters
from TestGames import RandomKiller
from gra.Engine import Heal
import time
from gra.Inventory import Potions

Player = Characters.Character('Geralt', 300, 30, 35, 15)

Monster = Characters.Character('Strzyga', 70, 20, 0, 5)



print(f'Gracz o imieniu {Player.Name} ma {Player.HP} HP i {Player.Defense} punktów tarczy')

print(f'Gracz o imieniu {Monster.Name} ma {Monster.HP} HP i {Player.Defense} punktów tarczy')

Player.CritChance = 30

while Player.HP > 0:
    Attack.AttackChoice(Player, Monster)
    if Monster.HP > 0:
        time.sleep(2)
        Attack.MeleeAttack(Monster,Player)
        Heal.Lifesteal(Monster,Player)
    elif Monster.HP <= 0 and Player.HP > 0:
        print(f'{Monster.Name} Nie żyje')
        print(f'Zwycięża {Player.Name}!')
        break
    elif Monster.HP > 0 and Player.HP <= 0:
        print(f'{Monster.Name} Nie żyje')
        print(f'Zwycięża {Player.Name}!')
        break





#RandomKiller.Graj()
