from decimal import *

# practice
print(Decimal("10") + Decimal("0.2"))


class Square:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width


a = Square(10, 15)
print(a.area())


