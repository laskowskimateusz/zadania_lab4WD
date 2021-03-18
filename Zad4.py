class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed

    def wyswietl_produkt(self):
        print("Nazwa produktu", self.nazwa_produktu)
        print("Ilosc", self.ilosc)
        print("Jednostka miary", self.jednostka_miary)
        print("Cena jed", self.cena_jed)

    def ile_produktu(self):
        print(self.ilosc, self.jednostka_miary)

    def ile_kosztuje(self):
        print(self.ilosc * self.cena_jed, 'zł')


ziemniaki = NaZakupy('Ziemniaki', 5, 'kg', 2)
ziemniaki.wyswietl_produkt()
ziemniaki.ile_produktu()
ziemniaki.ile_kosztuje()

woda = NaZakupy('Woda', 12, 'L', 2)
woda.wyswietl_produkt()
woda.ile_produktu()
woda.ile_kosztuje()
