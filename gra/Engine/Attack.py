from gra.Models import Characters
import random

def MeleeAttack(attacker :Characters.Character, deffender :Characters.Character):
    chance = random.randint(1,100)
    isCritical = chance <= attacker.CritChance
    power = attacker.Power
    if isCritical :
        power = attacker.Power * attacker.CritMultiplier

    power = power - (power/deffender.Defense)

    #power = round(power, 2)


    InflictDamage(power, deffender)
    print(f'{deffender.Name} zostało {round(deffender.HP,2)} życia!')
    print(f'A tak naprawdę zostało {deffender.HP} życia!')


def InflictDamage(damage: float,deffender :Characters.Character):
    deffender.HP = deffender.HP - damage
    print(f'{deffender.Name} otrzymał {round(damage,2)} obrażeń!')
