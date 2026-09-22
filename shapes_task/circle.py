from shapes_task.shape import Shape
from typing import override
import math


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.__radius = radius

    @override
    def get_width(self) -> float:
        return 2 * self.__radius

    @override
    def get_height(self) -> float:
        return 2 * self.__radius

    @override
    def get_area(self) -> float:
        return math.pi * self.__radius * self.__radius

    @override
    def get_perimeter(self) -> float:
        return 2 * math.pi * self.__radius

    def __repr__(self) -> str:
        return f"Circle({self.__radius!r})"

    def __hash__(self) -> int:
        return hash(self.__radius)

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.__radius == other.__radius
