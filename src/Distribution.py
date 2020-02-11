from abc import ABC
from math import *


class Distribution(ABC):
    def to_parameters(self):
        pass


class Continuous(Distribution):
    pass


class Normal(Continuous):

    def __init__(self, mean, variance):
        self.__mean = mean
        self.__variance = variance

    def to_parameters(self):
        pass
        # to implement


class Intervals(Continuous):

    def __init__(self, intervals):
        self.__intervals = intervals

    def __default_intervals(self, range, start, end):
        self.__intervals = [start]
        while start < end:
            start += range
            self.__intervals.append(start)

        self.__intervals.append(inf)

    def to_parameters(self):
        pass
        # to implement


class Discrete(Distribution):

    def __init__(self, values_probability):
        self.__values_probability = values_probability

    def to_parameters(self):
        pass
        # to implement
