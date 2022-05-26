"""
-------zmienne--------
public zm
protected _zm
private   __zm
"""


class Spolka:
    def __init__(self, rodzaj, rynek, gielda):
        self.rodzaj = rodzaj
        self._rynek = rynek
        self.__gielda = gielda


class Kghm(Spolka):
    def __init__(self, rodzaj, rynek, gielda, nazwa):
        super().__init__(rodzaj, rynek, gielda)
        self.nazwa = nazwa
        print(f'Atrybut publiczny {self.rodzaj}')
        print(f'Atrybut chroniony {self._rynek}')
        #print(f'Atrybut prywatny {self.__gielda}')


spolka = Spolka('Spółka akcyjna', 'Główny', 'GPW w Warszawie')

#print(f'Atrybut publiczny {spolka.rodzaj}')
#print(f'Atrybut chroniony {spolka._rynek}')
# print(f'Atrybut prywatny {spolka.__gielda}')

kghm = Kghm('Spółka akcyjna', 'Główny', 'GPW w Warszawie', 'KGHM')

print(f'Atrybut publiczny {kghm.rodzaj}')
print(f'Atrybut chroniony {kghm._rynek}')
#print(f'Atrybut prywatny {kghm.__gielda}')

