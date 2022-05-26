eval('1 + 1')
x = 10
eval('x + 13')  # bez potrzeby konwertowania

#########################

print(list((enumerate(['Pawel', 'Tomek']))))  # tworzy liste tupli

##########################

a = list(filter(abs, [-2, -1, 0, 1, 2]))
print(a)

b = list(filter(bool, ["TO", -1, 0, 1, 2]))
print(b)

###########################

print(isinstance(1, int))  # czy 1 nalezy do int

###############

print(list(map(abs, [-2, -1, 0, 1, 2]))) # funkcja map() mapuje po koli kazdy element

names = ['tomek', 'piotr', 'zenek']
print(list(map(str.title, names)))
print(list(reversed(names)))
print(list(reversed('tom')))

########### funkcja zip()

lista_1 = [1, 2, 3]
lista_2 = [2, 3, 4]
print(list(zip(lista_1, lista_2))) # laczy dwie listy w tuple


