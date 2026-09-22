from shapes_task.shape import Shape
from typing import override


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.__width = width
        self.__height = height

    @override
    def get_width(self) -> float:
        return self.__width

    @override
    def get_height(self) -> float:
        return self.__height

    @override
    def get_area(self) -> float:
        return self.__width * self.__height

    @override
    def get_perimeter(self) -> float:
        return 2 * (self.__width + self.__height)

    def __repr__(self) -> str:
        return f"Rectangle({self.__width!r},{self.__height!r})"

    def __hash__(self) -> int:
        return hash((self.__width, self.__height))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return (self.__width == other.__width and
                self.__height == other.__height)
