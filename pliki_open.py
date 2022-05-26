with open('simple.txt', 'r') as file:
    for line in file:
        print(line, end='')
    line = file.readlines()
    print(line)
