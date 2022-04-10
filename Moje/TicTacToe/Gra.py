import PlanszaObiekt, Gracz

class Rozgrywka:
    def __init__(self, RozmiarMapy, Gracz1: Gracz.Player, Gracz2: Gracz.Player):
        self.Mapa = PlanszaObiekt.PlanszaObiekt(RozmiarMapy)
        self.Gracz1 = Gracz1
        self.Gracz2 = Gracz2


plansza = PlanszaObiekt.PlanszaObiekt(5,'<3')
plansza.RysujPlansze()

fajniejsza = PlanszaObiekt.PlanszaObiekt(10)
fajniejsza.RysujPlansze()
plansza.RysujPlansze()



