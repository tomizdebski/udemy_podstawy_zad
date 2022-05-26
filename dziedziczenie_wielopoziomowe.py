"""
###################
dziedziczenie ####
#################
"""


class Czlowiek:
    pochodzenie = 'Ziemia'
    imię = 'Tom'


class Polak(Czlowiek):
    kraj = 'Polska'
    imię = "Karol"



class Programista(Polak):
    technologia = 'Python'
    imię = "Dawid"

    def info(self):
        print(f'Pochodzenie >>>{self.pochodzenie}\n',
              f'Kraj >>>{self.kraj}\n',
              f'Technologia >>>{self.technologia}\n'
              f'Imię >>> {self.imię}')


programista_1 = Programista()
programista_1.info()
