from Models import CharacterBase
def Cios(Attacker: CharacterBase.Character, Defender: CharacterBase.Character):
    Defender.HP = Defender.HP - Attacker.Dmg
    print(f'{Attacker.Name} zadał {Attacker.Dmg} obrażeń')
    print(f'{Defender.Name} zostało {Defender.HP} HP')


def SprawdzCzyZyje(Attacker:CharacterBase.Character, Defender: CharacterBase.Character):
    if Defender.HP > 0:
        return True
    print(f'{Defender.Name} poległ! Zwyciężył gracz {Attacker.Name}')
    return False



def Bitka(Gracz1: CharacterBase.Character, Gracz2: CharacterBase.Character):
     while Gracz1.HP > 0:
        Cios(Gracz1, Gracz2)
        if SprawdzCzyZyje(Gracz1, Gracz2):
            Cios(Gracz2, Gracz1)
            SprawdzCzyZyje(Gracz2, Gracz1)
        else:
            break





