"""
print(dir(1))
print(int.__add__(1, 4))

print(int.__sub__(10, 7))
"""


class SpecialInt(int):
    def __init__(self, special_int):
        self.special_int = special_int

    def __add__(self, other):
        return self.special_int + other.special_int + 10

    def __str__(self):
        return f" To jest specjalne dodawanie do sumy plus 10 {self.special_int}"


s_1 = SpecialInt(1)
s_2 = SpecialInt(2)

s = s_1 + s_2
print(s_1)
