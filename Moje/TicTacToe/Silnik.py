tabela = [
    ["O","O","X"],
    ["X","O","O"],
    ["X","X","O"]
]

seria = 3
symbol = "O"

def SprawdzWygrana(SeriaDanych, Symbol):
    temp = 0
    for i in SeriaDanych:
        if i == Symbol:
            temp += 1
        else:
            temp = 0

        if temp >= seria:
            return True

    return False

def PobierzKolumne(Tabela, wiersz, kolumna):
    WierszStart = wiersz - (seria - 1)
    WierszKoniec = wiersz + seria
    Wynik = []

    for i in range(WierszStart,WierszKoniec):
        if i >= 0:
            try:
                Symbol = Tabela[i][kolumna]
                Wynik.append(Symbol)
            except IndexError:
                Wynik.append('')

    return Wynik

def PobierzWiersz(Tabela, wiersz, kolumna):
    KolumnaStart = kolumna - (seria - 1)
    KolumnaKoniec = kolumna + seria
    Wynik = []

    for i in range(KolumnaStart, KolumnaKoniec):
        if i >= 0:
            try:
                Symbol = Tabela[wiersz][i]
                Wynik.append(Symbol)
            except IndexError:
                Wynik.append('')

    return Wynik

def PobierzUkosZLewejDoPrawej(Tabela, wiersz, kolumna):
    KolumnaStart = kolumna - (seria - 1)
    WierszStart = wiersz - (seria - 1)
    KolumnaKoniec = kolumna + seria

    Wynik = []

    for i in range(KolumnaStart, KolumnaKoniec):
        if i >= 0 and WierszStart >= 0:
            try:
                Symbol = Tabela[WierszStart][i]
                Wynik.append(Symbol)
            except IndexError:
                Wynik.append('')
        WierszStart += 1

    return Wynik

def PobierzUkosZPrawejDoLewej(Tabela, wiersz, kolumna):
    KolumnaStart = kolumna + (seria - 1)
    WierszStart = wiersz - (seria - 1)
    KolumnaKoniec = kolumna - seria
    Wynik = []

    for i in range(KolumnaStart,KolumnaKoniec,-1):
        if i >= 0 and WierszStart >= 0:
            try:
                Symbol = Tabela[WierszStart][i]
                Wynik.append(Symbol)
            except IndexError:
                Wynik.append('')
        WierszStart += 1

    return Wynik

def SprawdzWynik(Tabela, Wiersz, Kolumna, Symbol):
    return SprawdzWygrana(PobierzKolumne(Tabela, Wiersz, Kolumna), Symbol) or \
           SprawdzWygrana(PobierzWiersz(Tabela, Wiersz, Kolumna), Symbol) or \
           SprawdzWygrana(PobierzUkosZPrawejDoLewej(Tabela, Wiersz, Kolumna), Symbol) or \
           SprawdzWygrana(PobierzUkosZLewejDoPrawej(Tabela, Wiersz, Kolumna), Symbol)

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