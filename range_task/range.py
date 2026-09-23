from __future__ import annotations


class Range:
    def __init__(self, start: float, end: float) -> None:
        self.__start = start
        self.__end = end

    @property
    def start(self) -> float:
        return self.__start

    @start.setter
    def start(self, start: float) -> None:
        self.__start = start

    @property
    def end(self) -> float:
        return self.__end

    @end.setter
    def end(self, end: float) -> None:
        self.__end = end

    @property
    def length(self) -> float:
        return self.__end - self.__start

    def is_inside(self, number: float) -> bool:
        return self.__start <= number <= self.__end

    def get_intersection(self, other_range: Range) -> Range | None:
        start = max(self.__start, other_range.__start)
        end = min(self.__end, other_range.__end)

        if start < end:
            return Range(start, end)

        return None

    def get_union(self, other_range: Range) -> list[Range]:
        if self.__end < other_range.__start or self.__start > other_range.__end:
            return [Range(self.__start, self.__end), Range(other_range.__start, other_range.__end)]

        start = min(self.__start, other_range.__start)
        end = max(self.__end, other_range.__end)
        return [Range(start, end)]

    def get_difference(self, other_range: Range) -> list[Range]:
        if self.__end <= other_range.__start or self.__start >= other_range.__end:
            return [Range(self.__start, self.__end)]

        result_list = []

        if self.__start < other_range.__start:
            result_list.append(Range(self.__start, other_range.__start))

        if self.__end > other_range.__end:
            result_list.append(Range(other_range.__end, self.__end))

        return result_list

    def __repr__(self):
        return f"({self.__start}; {self.__end})"
