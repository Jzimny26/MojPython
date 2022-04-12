import PlanszaObiekt, Gracz, Silnik
import os

class Rozgrywka:
    def __init__(self, RozmiarMapy, Gracz1: Gracz.Player, Gracz2: Gracz.Player):
        self.Mapa = PlanszaObiekt.PlanszaObiekt(RozmiarMapy)
        self.Gracz1 = Gracz1
        self.Gracz2 = Gracz2

# plansza = PlanszaObiekt.PlanszaObiekt(3,'<3')
# plansza.RysujPlansze()
#
# fajniejsza = PlanszaObiekt.PlanszaObiekt(10)
# fajniejsza.RysujPlansze()
# plansza.RysujPlansze()
# for i in range(0,100):
#     print(Gracze[i])
clear = lambda: os.system('cls')

Gracz1 = Gracz.Player('Kuba', '@')
Gracz2 = Gracz.Player('Seba', 'X')
Gracze = [Gracz1, Gracz2]

biezacygracz = -1
IloscGraczy = len(Gracze) -1
Tura = 0
GameOn = True

SilnikGry = Silnik.SilnikGry(3,Gracz1,Gracz2)

while GameOn:
    clear()
    biezacygracz += 1
    SilnikGry.Mapa.RysujPlansze()
    Tura += 1
    if biezacygracz > IloscGraczy:
        biezacygracz = 0
    print(f'Tura gracza {Gracze[biezacygracz].Nazwa}')
    SilnikGry.RuchGracza(Gracze[biezacygracz])
    GameOn = not SilnikGry.KoniecGry


SilnikGry.Mapa.RysujPlansze()
print(f'Wygrał Gracz {Gracze[biezacygracz].Nazwa} w turze {Tura}!')