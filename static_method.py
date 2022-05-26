class Student:

    lista_studentów = []

    def __init__(self, imię, nazwisko, wiek):
        self.wiek = wiek
        self.nazwisko = nazwisko
        self.imię = imię
        self.lista_studentów.append(self)

    @staticmethod
    def liczba_studentów():
        print('Liczba studentów: ', len(Student.lista_studentów))

    @classmethod
    def liczba_studentek(cls):
        print('Liczba studentów: ', len(Student.lista_studentów))


student_1 = Student('Jan', 'Kowalski', 18)
student_2 = Student('Tomasz', 'Izdebski', 40)
print(str(student_1.wiek))
Student.liczba_studentów()
Student.liczba_studentek()
