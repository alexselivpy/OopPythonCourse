from shapes_task.shape import Shape
from typing import override


class Square(Shape):
    def __init__(self, side_length: float) -> None:
        self.__side_length = side_length

    @override
    def get_width(self) -> float:
        return self.__side_length

    @override
    def get_height(self) -> float:
        return self.__side_length

    @override
    def get_area(self) -> float:
        return self.__side_length * self.__side_length

    @override
    def get_perimeter(self) -> float:
        return 4 * self.__side_length

    def __repr__(self) -> str:
        return f"Square({self.__side_length!r})"

    def __hash__(self) -> int:
        return hash(self.__side_length)

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.__side_length == other.__side_length
