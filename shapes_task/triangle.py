from shapes_task.shape import Shape
from typing import override
import math


class Triangle(Shape):
    def __init__(self, x1: float, y1: float,
                 x2: float, y2: float,
                 x3: float, y3: float) -> None:
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__x3 = x3
        self.__y3 = y3

    @staticmethod
    def __get_segment_length(x1: float, y1: float, x2: float, y2: float) -> float:
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    @override
    def get_width(self) -> float:
        return (max(self.__x1, self.__x2, self.__x3) -
                min(self.__x1, self.__x2, self.__x3))

    @override
    def get_height(self) -> float:
        return (max(self.__y1, self.__y2, self.__y3) -
                min(self.__y1, self.__y2, self.__y3))

    @override
    def get_area(self) -> float:
        return (abs(self.__x1 * (self.__y2 - self.__y3) +
                    self.__x2 * (self.__y3 - self.__y1) +
                    self.__x3 * (self.__y1 - self.__y2)) / 2)

    @override
    def get_perimeter(self) -> float:
        a = self.__get_segment_length(self.__x1, self.__y1, self.__x2, self.__y2)
        b = self.__get_segment_length(self.__x2, self.__y2, self.__x3, self.__y3)
        c = self.__get_segment_length(self.__x3, self.__y3, self.__x1, self.__y1)
        return a + b + c

    def __repr__(self) -> str:
        return f"Triangle({self.__x1!r}, {self.__y1!r}, {self.__x2!r}, {self.__y2!r}, {self.__x3!r}, {self.__y3!r})"

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
