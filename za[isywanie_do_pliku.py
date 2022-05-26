techs = ['python', 'java', 'sql', 'r', 'scala']

with open('techs.txt', 'w') as file:
    for tech in techs:
        print(tech, file=file)

even_number = list(range(100))[::2] # inteligentne wycinanie co dwa
with open('numbers.txt', 'w') as file: # a -append w - nadpisywanie r - odczyt
    for number in even_number:
        file.write(str(number) + '\n')


technologies = []
with open('techs.txt', 'r') as file:
    for line in file:
        technologies.append(line)
    print(technologies)