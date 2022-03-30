import time
from gra.Models import Characters
from gra.Engine import Attack
from gra.Engine import Heal


def HealthPotion(Player :Characters.Character):
    Player.HP = Player.HP + Player.HealAmount
    Attack.Timesleep()
    print(f'{Player.Name} użył eliskiru Jaskółka')
    print(f'{Player.Name} ma {Player.HP} HP!')


def DamagePotion(Player: Characters.Character):
    Player.Power = Player.Power + 15
    print(f'{Player.Name} użył Eliksiru na zwiększenie obrażeń')

def OpenInv():
    Player = Characters.Character('Geralt', 300, 30, 35, 15)
    Attacker = Player

    MonsterName = 'Strzyga'
    MonsterHP = 70
    MonsterPower = 20
    MonsterDefense = 5
    MonsterRangePower = 0

    Monster = Characters.Character(MonsterName, MonsterHP, MonsterPower,MonsterRangePower, MonsterDefense)
    Defender = Monster

    print('Jaskółka - 1')
    print('Eliksir obrażeń - 2')
    print('powrót do wyboru ataku - 3')
    wybor = int(input('Wybierz przedmiot którego chcesz użyć: '))
    if wybor == 1:
        HealthPotion(Player)
    elif wybor == 2:
        DamagePotion(Player)
    elif wybor == 3:
        Attack.AttackChoice(Attacker,Defender)
    else:
        print('Podano nieprawidłową liczbę')
        OpenInv()


