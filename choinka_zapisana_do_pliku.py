with open('tree_2.txt', 'w' ) as file:
    for j in range(2):
        for i in range(10):
            print('{:>9}'.format('*' * i), end ='', file = file)
            print('{}'.format('*' * i), file = file)