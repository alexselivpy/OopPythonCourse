class Range:
    def __init__(self, start: float, end: float) -> None:
        self.__start = start
        self.__end = end

    @property
    def start(self) -> float:
        return self.__start

    @property
    def end(self) -> float:
        return self.__end

    @property
    def length(self) -> float:
        return self.__end - self.__start

    @start.setter
    def start(self, start: float) -> None:
        self.__start = start

    @end.setter
    def end(self, end: float) -> None:
        self.__end = end

    def is_inside(self, number: float) -> bool:
        return self.__start <= number <= self.__end
