from abc import ABC
from math import *
from statistics import mean, stdev
from Util import binary_search
from numpy import linspace, logspace
from scipy.stats import norm
import random

## return a sample of a Gauss distribution with mu and sigma value
def normal_sampling(mu, sigma):
    return random.gauss(mu, sigma)

##
# Represents a generic statistic distribution
class Distribution(ABC):
    def get_parameters(self):
        pass

    def add(self, value):
        pass


##
# Represents a generic statistic continuous distribution
class Continuous(Distribution):
    pass


##
# Represents a generic statistic discrete distribution
class Discrete(Distribution):
    pass


##
# Represents a normal distribution
class Normal(Continuous):

    ## Normal constructor
    def __init__(self):
        self.__mean = None
        self.__stdev = None
        self.__values = []

    ## get the parameters of the distribution (mu,sigma)
    # @param: recalculate: tells if recalculate mean and stdev from data
    # @returns: mean and stdev
    def get_parameters(self, recalculate=False):
        if recalculate:
            self.calculate_mean()
            self.calculate_stdev()
        return self.__mean, self.__stdev

    ## add a value to the data
    # @param: value: the value to be added
    def add(self, value: float):
        self.__values.append(value)

    ## calculate the mean from data
    # @returns: mean
    def calculate_mean(self):
        self.__mean = mean(self.__values)
        return self.__mean

    ## calculate the stdev from data
    # @returns: stdev
    def calculate_stdev(self):
        self.__stdev = stdev(self.__values)
        return self.__stdev

    ## calculate the probability from normal fdp
    # @param: x: the value in R input of the fdp
    # @param: recalculate: tells if recalculate mean and stdev from data
    # @returns: the probability calculated
    def pdf(self, x, recalculate=False):
        if recalculate:
            self.calculate_mean()
            self.calculate_stdev()
        return norm.pdf(x, loc=self.__mean, scale=self.__stdev)


##
# Represents the multinomial distribution
class Multinomial(Discrete):

    ## Multinomial constructor
    # @param: pseudocounts: a dictionary that contains pseudocounts and initialize counts member
    def __init__(self, pseudocounts: dict = None):
        if pseudocounts is not None:
            self._counts = pseudocounts
            self.__total = sum(pseudocounts.values())
        else:
            self._counts = dict()
            self.__total = 0

    ## returns the dictionary key:probability
    def get_parameters(self):
        param = dict()
        for couple in self._counts.items():
            param[couple[0]] = param[couple[1]] / self.__total
        return param

    ## adds an occurence of a value to the counts
    # @param: value: the value occurred
    def add(self, value):
        if value not in self._counts.keys():
            self._counts[value] = 1
        else:
            self._counts[value] = self._counts[value] + 1
        self.__total = self.__total + 1


##
# A continuous distribution transformed into a multinomial interspersing the domain
class Interspersed(Multinomial):

    ## Interspersed constructor
    # @param: pseudocounts: a dictionary that contains pseudocounts and initialize counts member
    def __init__(self, intervals, pseudocounts: dict = None):
        Multinomial.__init__(pseudocounts)
        self.__intervals = intervals

    # Generate linear intervals
    # @param: start: the starting interval left extreme
    # @param: end: the ending interval right extreme
    # @param: num: the number of intervals
    # @param: infinite: tells to add the intervals (-inf,start] and [end,inf)
    def __lin_intervals(self, start, end, num, infinite=True):
        self.__intervals = list(linspace(start=start, stop=end, num=num))
        if infinite:
            self.__intervals = [-inf] + self.__intervals + [inf]

    # Generate logarithmic intervals
    # @param: start: the starting interval left extreme
    # @param: end: the ending interval right extreme
    # @param: num: the number of intervals
    # @param: infinite: tells to add the intervals (-inf,start] and [end,inf)
    def __log_intervals(self, start, end, num, infinite=True):
        self.__intervals = list(logspace(start=start, stop=end, num=num))
        if infinite:
            self.__intervals = [-inf] + self.__intervals + [inf]

    ## adds an occurence of a value to the counts
    # @param: value: the value occurred
    def add(self, value: float):
        index = binary_search(self.__intervals, value)
        interval = '[' + str(self.__intervals[index]) + ', ' + str(self.__intervals[index]) + ']'
        Distribution.add(self, interval)
