from gra.Models import CharacterBase
import random
from gra.Engine import Heal
import time
from gra.Inventory import Ekwipunek

delay = 0

def MeleeAttack(attacker :CharacterBase.Character, deffender :CharacterBase.Character):
    chance = random.randint(1,100)
    isCritical = chance <= attacker.CritChance
    power = attacker.Power
    if isCritical :
        power = attacker.Power * attacker.CritMultiplier
    power = power - (power/deffender.Defense)

    #power = round(power, 2)

    InflictDamage(power, deffender)
    if deffender.HP > 0:
        Timesleep()
        print(f'{deffender.Name} ma {round(deffender.HP,2)} życia!')



def InflictDamage(damage: float,deffender :CharacterBase.Character):
    deffender.HP = deffender.HP - damage
    Timesleep()
    print(f'{deffender.Name} otrzymał {round(damage,2)} obrażeń!')


def RangeAttack(Attacker: CharacterBase.Character, Deffender: CharacterBase.Character):
    Attacker.RangePower = Attacker.RangePower - (Attacker.RangePower/Deffender.Defense)
    InflictDamage(Attacker.RangePower, Deffender)
    Timesleep()
    if Deffender.HP > 0:
        print(f'{Deffender.Name} zostało {round(Deffender.HP,2)} życia ')



def Attackk(Attacker : CharacterBase.Character, Defender: CharacterBase.Character):
    chance = random.randint(1,100)
    if chance <= Attacker.MeleeChance:
        MeleeAttack(Attacker, Defender)
    else:
        RangeAttack(Attacker,Defender)

def AttackChoice(Attacker :CharacterBase.Character, Defender :CharacterBase.Character):
    Timesleep()
    print('szybki atak - 1')
    print('Kusza - 2')
    print('Ekwipunek - 3')
    wybór = int(input('Wybierz akcję: '))


    if 1 == wybór:
        MeleeAttack(Attacker, Defender)
    elif 2 == wybór:
        RangeAttack(Attacker,Defender)
    elif 3 == wybór:
        Ekwipunek.OpenInv(Attacker, Defender)
    else:
        print('Podano nieprawidłową liczbę')
        AttackChoice(Attacker, Defender)

def Timesleep():
    time.sleep(delay)


