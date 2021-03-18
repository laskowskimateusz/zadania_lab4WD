class Robaczek:
    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok

    def idz_w_gore(self, ile=1):
        self.y += self.krok*ile

    def idz_w_dol(self, ile=1):
        self.y -= self.krok*ile

    def idz_w_lewo(self, ile=1):
        self.x -= self.krok*ile

    def idz_w_prawo(self, ile=1):
        self.x += self.krok*ile

    def pokaz_gdzie_jestes(self):
        print('x =', self.x, 'y =', self.y)


robak1 = Robaczek(5, 5, 1)
robak1.pokaz_gdzie_jestes()
robak1.idz_w_gore()
robak1.pokaz_gdzie_jestes()
robak1.idz_w_dol(2)
robak1.pokaz_gdzie_jestes()
robak1.idz_w_lewo(4)
robak1.pokaz_gdzie_jestes()
robak1.idz_w_prawo(7)
robak1.pokaz_gdzie_jestes()
