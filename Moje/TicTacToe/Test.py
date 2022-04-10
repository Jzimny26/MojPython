

Plansza = []

def UtworzPlansze(rozmiar):
    Plansza = [["_" for y in range(rozmiar)]
               for x in range(rozmiar)]
    # # initialize multi-array
    # b = [[None for y in range(2)]
    #      for x in range(2)]

    # for wiersz in range(rozmiar):
    #     for kolumna in range(rozmiar):
    #         print(wiersz)
    #         print(kolumna)
    #         Plansza[wiersz][kolumna] = '_'


def RysujPlansze():
    for wiersz in Plansza:
        print(wiersz)

UtworzPlansze(3)
RysujPlansze()
