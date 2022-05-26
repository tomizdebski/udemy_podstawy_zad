import sys


class Magazyn:

    def __init__(self, lista_produktow):
        self.lista_produktow = lista_produktow

    def wyswietl_dostepne_produkty(self):
        print('Dostępne produkty: ')
        for produkt in self.lista_produktow:
            print(produkt)

    def dodaj_produkt(self):
        self.nazwa_produktu = input('Podaj nazwę produktu: >>>')
        if self.nazwa_produktu not in self.lista_produktow:
            self.lista_produktow.append(self.nazwa_produktu)
            print(f'Produkt {self.nazwa_produktu} został dodany do magazynu')

    def usun_produkt(self):
        self.nazwa_produktu = input('Podaj produkt do usunięcia: >>>')
        if self.nazwa_produktu in self.lista_produktow:
            self.lista_produktow.remove(self.nazwa_produktu)
            print('Usunięto produkt z magazynu')
        else:
            print('Podanego produktu niema na magazynie')


magazyn = Magazyn(['mleko', 'woda', 'jajka'])

while True:
    print("""
                wprowadz 1 aby wyswietlic produkt.
                wprowadz 2 zeby dodac produkt.
                wprowadz 3 zeby usunac produkt.
                wprowdz 4 zeby zakonczyc.
                """)

    wybor_urzytkownika = int(input('>>>'))
    if wybor_urzytkownika == 1:
        magazyn.wyswietl_dostepne_produkty()
    elif wybor_urzytkownika == 2:
        magazyn.dodaj_produkt()
    elif wybor_urzytkownika == 3:
        magazyn.usun_produkt()
    elif wybor_urzytkownika == 4:
        sys.exit()




