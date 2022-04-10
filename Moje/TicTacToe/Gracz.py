class Player:
    def __init__(self, Nazwa, Symbol):
        self.Nazwa = Nazwa
        self.Symbol = Symbol

    def PrzedstawSie(self):
        print(f'Gracz {self.Nazwa} ma symbol {self.Symbol}')