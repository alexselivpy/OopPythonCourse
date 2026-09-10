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

    def get_intersection(self, other: Range) -> Range | None:
        if self.__end <= other.__start or self.__start >= other.__end:
            return None

        if self.__start >= other.__start:
            start = self.__start
        else:
            start = other.__start

        if self.__end <= other.__end:
            end = self.__end
        else:
            end = other.__end

        return Range(start, end)

    def get_union(self, other: Range) -> Range | list[Range]:
        if self.__end < other.__start:
            return [Range(self.__start, self.__end), Range(other.__start, other.__end)]

        if self.__start > other.__end:
            return [Range(other.__start, other.__end), Range(self.__start, self.__end)]

        if self.__start <= other.__start:
            start = self.__start
        else:
            start = other.__start

        if self.__end >= other.__end:
            end = self.__end
        else:
            end = other.__end

        return Range(start, end)

    def get_complement(self, other: Range) -> Range | list[Range] | None:
        if self.__end <= other.__start or self.__start >= other.__end:
            return Range(self.__start, self.__end)

        if self.__start >= other.__start and self.__end <= other.__end:
            return None

        result_list = []

        if self.__start < other.__start:
            result_list.append(Range(self.__start, other.__start))

        if self.__end > other.__end:
            result_list.append(Range(other.__end, self.__end))

        return result_list

    def __repr__(self):
        return f"({self.__start}; {self.__end})"
