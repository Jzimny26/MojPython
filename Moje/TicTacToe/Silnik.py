import PlanszaObiekt, Gracz

class SilnikGry:
    def __init__(self, RozmiarMapy, Gracz1: Gracz.Player, Gracz2: Gracz.Player, seria = 3, DomyslnySymbol = "_"):
        self.Mapa = PlanszaObiekt.PlanszaObiekt(RozmiarMapy, DomyslnySymbol)
        self.Gracz1 = Gracz1
        self.Gracz2 = Gracz2
        self.seria = seria
        self.KoniecGry = False

    def SprawdzWygrana(self,SeriaDanych, Symbol):
        temp = 0
        for i in SeriaDanych:
            if i == Symbol:
                temp += 1
            else:
                temp = 0

            if temp >= self.seria:
                return True

        return False

    def Graj(self):
        return True

    def PobierzKolumne(self, wiersz, kolumna):
        WierszStart = wiersz - (self.seria - 1)
        WierszKoniec = wiersz + self.seria
        Wynik = []

        for i in range(WierszStart,WierszKoniec):
            if i >= 0:
                try:
                    Symbol = self.Mapa.Plansza[i][kolumna]
                    Wynik.append(Symbol)
                except IndexError:
                    Wynik.append('')

        return Wynik

    def PobierzWiersz(self, wiersz, kolumna):
        KolumnaStart = kolumna - (self.seria - 1)
        KolumnaKoniec = kolumna + self.seria
        Wynik = []

        for i in range(KolumnaStart, KolumnaKoniec):
            if i >= 0:
                try:
                    Symbol = self.Mapa.Plansza[wiersz][i]
                    Wynik.append(Symbol)
                except IndexError:
                    Wynik.append('')

        return Wynik

    def PobierzUkosZLewejDoPrawej(self, wiersz, kolumna):
        KolumnaStart = kolumna - (self.seria - 1)
        WierszStart = wiersz - (self.seria - 1)
        KolumnaKoniec = kolumna + self.seria

        Wynik = []

        for i in range(KolumnaStart, KolumnaKoniec):
            if i >= 0 and WierszStart >= 0:
                try:
                    Symbol = self.Mapa.Plansza[WierszStart][i]
                    Wynik.append(Symbol)
                except IndexError:
                    Wynik.append('')
            WierszStart += 1

        return Wynik

    def PobierzUkosZPrawejDoLewej(self, wiersz, kolumna):
        KolumnaStart = kolumna + (self.seria - 1)
        WierszStart = wiersz - (self.seria - 1)
        KolumnaKoniec = kolumna - self.seria
        Wynik = []

        for i in range(KolumnaStart,KolumnaKoniec,-1):
            if i >= 0 and WierszStart >= 0:
                try:
                    Symbol = self.Mapa.Plansza[WierszStart][i]
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
        self.Mapa.Plansza[Y][X] = Gracz.Symbol
        self.KoniecGry = self.SprawdzWynik(X, Y, Gracz.Symbol)

    def CzyMoznaWykonacRuch(self, Y: int,X: int):
        symbolWPolu = self.Mapa.Plansza[Y][X]
        symbolGracza = self.Mapa.DomyslnySymbol
        if  symbolWPolu == symbolGracza:
            return True
        return False

    def Ruch(self, Y: int, X: int):
        self.Y = -1
        self.X = -1
        while not SilnikGry.CzyMoznaWykonacRuch(self, Y, X):
            self.Y = input("podaj wiersz: ")
            self.X = input("podaj kolumne: ")
            if not  SilnikGry.CzyMoznaWykonacRuch(self, Y, X):
                print("pole zajete lub nie instnieje")

        SilnikGry.WykonajRuch(Gracz.Player,Y, X)

    def RuchGracza(self, Gracz: Gracz.Player):
        tekst = input('Podaj Y oraz X, oddzielone spacją ').split()
        Y = int(tekst[0])
        X = int(tekst[1])
        if self.CzyMoznaWykonacRuch(Y, X):
            self.WykonajRuch(Gracz, Y, X)
            return True
        else:
            print(f'{Gracz.Nazwa} nie może wykonać ruchu w polu {Y}{X}')
            return False


















# testowo = PobierzKolumne(tabela,2,0)
# print(testowo)
# wygrana = SprawdzWygrana(testowo,"X")
# print(wygrana)

# test = PobierzWiersz(tabela,1,1)
# print(test)
# wygrana = SprawdzWygrana(test,"O")
# print(wygrana)

#if wiersz or kolumna or skos1 or skos 2
#return True