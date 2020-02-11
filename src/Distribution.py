from abc import ABC
from math import *
from statistics import mean, stdev

from problog.logic import Term, AnnotatedDisjunction
from scipy.stats import norm


class Distribution(ABC):
    def to_parameters(self):
        pass

    def add(self, value):
        pass


class Continuous(Distribution):
    pass


class Normal(Continuous):

    def __init__(self, mean, stdev):
        self.__mean = mean
        self.__stdev = stdev
        self.__values = []

    def to_parameters(self):
        pass
        # to implement

    def add(self, value: float):
        self.__values.append(value)

    def mean(self):
        self.__mean = mean(self.__values)

    def stdev(self):
        self.__stdev = stdev(self.__values)

    def pdf(self, x, calculate=False):
        if calculate:
            self.mean()
            self.stdev()
        return norm.pdf(x, loc=self.__mean, scale=self.__stdev)


class Discrete(Distribution):

    def __init__(self, pseudocounts: dict = None):
        if pseudocounts is None:
            self._counts = pseudocounts
            self.__total = sum(pseudocounts.values())
        else:
            self._counts = dict()
            self.__total = 0

    def to_parameters(self):
        param = dict()
        self._counts.items()
        for couple in self._counts.items():
            param[couple[0]] = param[couple[1]] / self.__total
        return param

    def add(self, value):
        if self._counts is None:
            self._counts[value] = 1
        else:
            self._counts[value] = self._counts[value] + 1
        self.__total = self.__total + 1


class Intervals(Discrete):

    def __init__(self, intervals, pseudocounts : dict=None):
        Discrete.__init__(pseudocounts)
        self.__intervals = intervals

    def __default_intervals(self, range, start, end):
        self.__intervals = [start]
        while start < end:
            start += range
            self.__intervals.append(start)

        self.__intervals.append(inf)

    def add(self, value: float):
        if self._counts is None:
            self._counts[value] = 1
        else:
            self._counts[value] = self._counts[value] + 1
        self.__total = self.__total + 1

    def to_parameters(self):
        pass
        # to implement
