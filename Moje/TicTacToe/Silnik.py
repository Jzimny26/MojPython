tabela = [
    ["O","O","X"],
    ["X","O","O"],
    ["X","X","O"]
]

seria = 3
symbol = "O"

import PlanszaObiekt, Gracz
class SilnikGry:
    def __init__(self, RozmiarMapy, Gracz1: Gracz.Player, Gracz2: Gracz.Player):
        self.Mapa = PlanszaObiekt(RozmiarMapy)
        self.Gracz1 = Gracz1
        self.Gracz2 = Gracz2

    def SprawdzWygrana(self,SeriaDanych, Symbol):
        temp = 0
        for i in SeriaDanych:
            if i == Symbol:
                temp += 1
            else:
                temp = 0

            if temp >= seria:
                return True

        return False

    def PobierzKolumne(self, wiersz, kolumna):
        WierszStart = wiersz - (seria - 1)
        WierszKoniec = wiersz + seria
        Wynik = []

        for i in range(WierszStart,WierszKoniec):
            if i >= 0:
                try:
                    Symbol = self.Mapa[i][kolumna]
                    Wynik.append(Symbol)
                except IndexError:
                    Wynik.append('')

        return Wynik

    def PobierzWiersz(self, wiersz, kolumna):
        KolumnaStart = kolumna - (seria - 1)
        KolumnaKoniec = kolumna + seria
        Wynik = []

        for i in range(KolumnaStart, KolumnaKoniec):
            if i >= 0:
                try:
                    Symbol = self.Mapa[wiersz][i]
                    Wynik.append(Symbol)
                except IndexError:
                    Wynik.append('')

        return Wynik

    def PobierzUkosZLewejDoPrawej(self, wiersz, kolumna):
        KolumnaStart = kolumna - (seria - 1)
        WierszStart = wiersz - (seria - 1)
        KolumnaKoniec = kolumna + seria

        Wynik = []

        for i in range(KolumnaStart, KolumnaKoniec):
            if i >= 0 and WierszStart >= 0:
                try:
                    Symbol = self.Mapa[WierszStart][i]
                    Wynik.append(Symbol)
                except IndexError:
                    Wynik.append('')
            WierszStart += 1

        return Wynik

    def PobierzUkosZPrawejDoLewej(self, wiersz, kolumna):
        KolumnaStart = kolumna + (seria - 1)
        WierszStart = wiersz - (seria - 1)
        KolumnaKoniec = kolumna - seria
        Wynik = []

        for i in range(KolumnaStart,KolumnaKoniec,-1):
            if i >= 0 and WierszStart >= 0:
                try:
                    Symbol = self.Mapa[WierszStart][i]
                    Wynik.append(Symbol)
                except IndexError:
                    Wynik.append('')
            WierszStart += 1

        return Wynik

    def SprawdzWynik(self, Wiersz, Kolumna, Symbol):
        return self.SprawdzWygrana(self.PobierzKolumne(Wiersz, Kolumna), Symbol) or \
               self.SprawdzWygrana(self.PobierzWiersz(Wiersz, Kolumna), Symbol) or \
               self.SprawdzWygrana(self.PobierzUkosZPrawejDoLewej(Wiersz, Kolumna), Symbol) or \
               self.SprawdzWygrana(self.PobierzUkosZLewejDoPrawej(Wiersz, Kolumna), Symbol)

    def WykonajRuch(self, Gracz: Gracz.Player, Y: int,X: int):
        self.Mapa[Y][X] = Gracz.Symbol

    def CzyMoznaWykonacRuch(self, Y: int,X: int):
        return True
# testowo = PobierzKolumne(tabela,2,0)
# print(testowo)
# wygrana = SprawdzWygrana(testowo,"X")
# print(wygrana)

# test = PobierzWiersz(tabela,1,1)
# print(test)
# wygrana = SprawdzWygrana(test,"O")
# print(wygrana)

test = SprawdzWynik(tabela,1,1,symbol)
print(test)

#if wiersz or kolumna or skos1 or skos 2
#return True