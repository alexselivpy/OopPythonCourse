from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def get_width(self):
        pass

    @abstractmethod
    def get_height(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass


class Square(Shape):
    def __init__(self, side_length: float | int) -> None:
        self.__side_length = side_length

    def get_width(self) -> float | int:
        return self.__side_length

    def get_height(self) -> float | int:
        return self.__side_length

    def get_area(self) -> float | int:
        return self.__side_length * self.__side_length

    def get_perimeter(self) -> float | int:
        return 4 * self.__side_length

    def __repr__(self) -> str:
        return f"Square({self.__side_length!r})"

    def __hash__(self) -> int:
        return hash((self.__side_length))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.__side_length == other.__side_length


class Triangle(Shape):
    def __init__(self, x1: float | int, y1: float | int,
                 x2: float | int, y2: float | int,
                 x3: float | int, y3: float | int) -> None:
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__x3 = x3
        self.__y3 = y3

    def get_width(self) -> float | int:
        return (max(self.__x1, self.__x2, self.__x3) -
                min(self.__x1, self.__x2, self.__x3))

    def get_height(self) -> float | int:
        return (max(self.__y1, self.__y2, self.__y3) -
                min(self.__y1, self.__y2, self.__y3))

    def get_area(self) -> float | int:
        return (abs(self.__x1 * (self.__y2 - self.__y3) +
                    self.__x2 * (self.__y3 - self.__y1) +
                    self.__x3 * (self.__y1 - self.__y2)) / 2)

    def get_perimeter(self) -> float | int:
        a = math.sqrt((self.__x2 - self.__x1) ** 2 + (self.__y2 - self.__y1) ** 2)
        b = math.sqrt((self.__x3 - self.__x2) ** 2 + (self.__y3 - self.__y2) ** 2)
        c = math.sqrt((self.__x1 - self.__x3) ** 2 + (self.__y1 - self.__y3) ** 2)
        return a + b + c

    def __repr__(self) -> str:
        return f"Triangle({self.__x1!r},{self.__y1!r},{self.__x2!r},{self.__y2!r},{self.__x3!r},{self.__y3!r})"

    def __hash__(self) -> int:
        return hash((self.__x1, self.__y1,
                     self.__x2, self.__y2,
                     self.__x3, self.__y3))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return (self.__x1 == other.__x1 and self.__y1 == other.__y1 and
                self.__x2 == other.__x2 and self.__y2 == other.__y2 and
                self.__x3 == other.__x3 and self.__y3 == other.__y3)


class Rectangle(Shape):
    def __init__(self, side_a: float | int, side_b: float | int) -> None:
        self.__side_a = side_a
        self.__side_b = side_b

    def get_width(self) -> float | int:
        return self.__side_a

    def get_height(self) -> float | int:
        return self.__side_b

    def get_area(self) -> float | int:
        return self.__side_a * self.__side_b

    def get_perimeter(self) -> float | int:
        return 2 * (self.__side_a + self.__side_b)

    def __repr__(self) -> str:
        return f"Rectangle({self.__side_a!r},{self.__side_b!r})"

    def __hash__(self) -> int:
        return hash((self.__side_a, self.__side_b))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return (self.__side_a == other.__side_a and
                self.__side_b == other.__side_b)


class Circle(Shape):
    def __init__(self, radius: float | int) -> None:
        self.__radius = radius
        self.__diameter = 2 * self.__radius

    def get_width(self) -> float | int:
        return self.__diameter

    def get_height(self) -> float | int:
        return self.__diameter

    def get_area(self) -> float:
        return math.pi * self.__radius ** 2

    def get_perimeter(self) -> float:
        return 2 * math.pi * self.__radius

    def __repr__(self) -> str:
        return f"Circle({self.__radius!r})"

    def __hash__(self) -> int:
        return hash((self.__radius))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.__radius == other.__radius
