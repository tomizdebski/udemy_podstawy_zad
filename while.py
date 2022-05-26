lista_do_przeszukania = [12, 53, 60, 49, 30]
flaga = False
wartość = 60

idx = 0
while idx  < len(lista_do_przeszukania):
    if lista_do_przeszukania[idx] == wartość:
        flaga = True
        break
    idx += 1
if flaga:
    print('Znaleziono element {}'.format(wartość))

