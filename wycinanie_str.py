
sampel = "Python to jest super jezyk"
result = ''
for char in sampel:
    if char == ' ':
        char = '-'
        result = result + char
    else:
        result = result +char
print(result)



