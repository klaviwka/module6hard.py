import math


class Figure:
    sides_count = 0

    def __init__(self, color=(0, 0, 0), *sides):
        self.__sides = self._validate_sides(sides)
        self.__color = self._validate_color(color)
        self.filled = False

    def __is_valid_color(self, r, g, b):
        return all(isinstance(value, int) and 0 <= value <= 255 for value in (r, g, b))

    def _validate_color(self, color):
        if self.__is_valid_color(*color):
            return color
        else:
            raise ValueError("Цвет должен быть в диапазоне от 0 до 255 для каждого компонента.")

    def _validate_sides(self, sides):
        if len(sides) != self.sides_count:
            return [1] * self.sides_count
        return sides

    def get_color(self):
        return list(self.__color)

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def get_sides(self):
        return list(self.__sides)

    def set_sides(self, *sides):
        if len(sides) == self.sides_count:
            self.__sides = sides
        elif self.sides_count == 12:
            pass
        elif self.sides_count == 1:
            self.__sides = (sides[0],) if sides else (self.__sides[0],)

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color=(0, 0, 0), radius=1):
        super().__init__(color, radius)

    def get_square(self):
        return math.pi * (self.get_sides()[0] ** 2)


class Cube(Figure):
    sides_count = 12

    def __init__(self, color=(0, 0, 0), side_length=1):
        super().__init__(color, *([side_length] * self.sides_count))

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
