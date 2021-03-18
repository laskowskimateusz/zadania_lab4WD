class Ciagi:
    def __init__(self):
        self.a1 = 0
        self.r = 0
        self.n = 0
        self.ciag = []
        self.suma = 0

    def wyswietl_dane(self):
        print('Ciag =', self.ciag)
        print('a1 =', self.a1)
        print('r =', self.r)
        print('n =', self.n)

    def pobierz_elementy(self, *elementy):
        self.ciag = []
        for x in elementy:
            self.ciag.append(x)

    def pobierz_parametry(self, a1, r, n):
        self.a1 = a1
        self.r = r
        self.n = n
        self.ciag = [a1]

    def policz_sume(self):
        an = self.a1+(self.n-1)*self.r
        self.suma = ((self.a1+an)/2)*self.n

    def policz_elementy(self):
        if self.a1 != 0 and self.r != 0:
            for x in range(self.n):
                self.ciag.append(self.ciag[-1]+self.r)


przyklad1 = Ciagi()
przyklad1.pobierz_elementy(2, 4, 6, 8, 10)
przyklad1.wyswietl_dane()

przyklad1.pobierz_parametry(1, 2, 10)
przyklad1.wyswietl_dane()

przyklad1.policz_sume()
print('Suma =', przyklad1.suma)

przyklad1.policz_elementy()
przyklad1.wyswietl_dane()
