from math import sqrt


class Figure:
    sides_count = 0
    def __init__(self, __color, *args):
        if self.__is_valid_sides(args):
            self.__sides = list(args)
        elif len(args) == 1:
            self.__sides = []
            for i in range(self.sides_count):
                self.__sides.append(*args)
        else:
            self.__sides = []
            for i in range(self.sides_count):
                self.__sides.append(1)
        self.__color = self.__is_valid_color(*__color)
        self.filled = False
    def get_color(self):
        return list(self.__color)
    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            self.__color = (r, g, b)
            self.filled = True
            return r, g, b
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = self.__is_valid_color(r, g, b)
    def __is_valid_sides(self, *args):
        for i in list(*args):
            if i > 0 and isinstance(i, int) and len(list(*args)) == self.sides_count:
                continue
            else:
                break
        else:
            return True
    def get_sides(self):
        return self.__sides
    def __len__(self):
        return sum(self.__sides)
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1
    def __init__(self, __color, *args):
        super().__init__(__color, *args)
        self.__radius = self.get_sides()[0] / (2 * 3.14)
    def get_square(self):
        area = 3.14 * self.__radius**2
        print(area)

class Triangle(Figure):
    sides_count = 3
    def get_square(self):
        p = 1/2*(sum(self.get_sides()))
        return sqrt(p * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2]))

class Cube(Figure):
    sides_count = 12
    def __init__(self, __color, *args):
        if len(args) > 1:
            args = [1]
        super().__init__(__color, *args)
    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)
circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())
print(len(circle1))
print(cube1.get_volume())








