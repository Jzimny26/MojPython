import CharacterBase
from Engine import MechanikaWalki

name = input('podaj imie: ')
postac = CharacterBase.Character(name, 100, 20)
print(f'Twoja postac nazywa sie {postac.Name}')

postac2 = CharacterBase.Character('Zly', 50, 50)

def przedstawSie():
    print(postac.Name)

def Walka():
    pass


MechanikaWalki.Bitka(postac,postac2)




