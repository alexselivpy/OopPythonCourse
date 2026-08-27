class Range:
    def __init__(self, start: float, end: float):
        self.__start = start
        self.__end = end

    @property
    def start(self):
        return self.__start

    @property
    def end(self):
        return self.__end

    @start.setter
    def start(self, start):
        self.__start = start

    @end.setter
    def end(self, end):
        self.__end = end

    def get_len(self):
        return self.__end - self.__start

    def is_inside(self, number):
        return self.__start <= number <= self.__end
