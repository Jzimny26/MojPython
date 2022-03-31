
from gra.Models import Characters
from gra.Engine import Attack



def HealthPotion(Player :Characters.Character):
    Player.HP = Player.HP + Player.HealAmount
    Attack.Timesleep()
    print(f'{Player.Name} użył eliskiru Jaskółka')
    print(f'{Player.Name} ma {Player.HP} HP!')


def DamagePotion(Player: Characters.Character):
    Player.Power = Player.Power + 15
    print(f'{Player.Name} użył Eliksiru na zwiększenie obrażeń')

def OpenInv(Player: Characters.Character, Monster: Characters.Character):

    print('Jaskółka - 1')
    print('Eliksir obrażeń - 2')
    print('powrót do wyboru ataku - 3')
    wybor = int(input('Wybierz przedmiot którego chcesz użyć: '))
    if wybor == 1:
        HealthPotion(Player)
        Attack.AttackChoice(Player)
    elif wybor == 2:
        DamagePotion(Player)
        Attack.AttackChoice(Player, Monster)
    elif wybor == 3:
        Attack.AttackChoice(Player, Monster)
    else:
        print('Podano nieprawidłową liczbę')
        OpenInv(Player, Monster)







