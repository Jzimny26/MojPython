import Gracz

class PlanszaObiekt:

    def __init__(self, rozmiar, DomyslnySymbol = "_"):
        self.Plansza = []
        self.DomyslnySymbol = DomyslnySymbol
        self.UtworzPlansze(rozmiar)


    def UtworzPlansze(self, rozmiar):
        self.Plansza = [[self.DomyslnySymbol for y in range(rozmiar)]
                   for x in range(rozmiar)]

    def RysujPlansze(self):
        print(len(self.Plansza))
        for wiersz in self.Plansza:
            print(wiersz)






