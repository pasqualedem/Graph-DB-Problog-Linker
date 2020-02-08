# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 17:14:20 2020

@author: PasqualeDeMarinis
"""

from probfoil.data import DataFile
from probfoil.probfoil import ProbFOIL2
from probfoil.score import accuracy, precision, recall
from problog.program import PrologFile
from problog.util import init_logger
import time


class StructureLearner:
    def __init__(self, learn_class=ProbFOIL2, logger='probfoil', *data):
        __data = DataFile(*(for source in data))
        __learn_class = learn_class
        __logger = logger
        __hypothesis = None

    def set_data(self, *data):
        __data = DataFile(*(for source in data))

    def learn(self):
        time_start = time.time()
        learner = self.__learn_class(self.__data, logger=self.__logger)
        __hypothesis = learner.learn()
        return time.time() - time_start

    def accuracy(self):
        return accuracy(self.__hypothesis))

    def precision(self):
        return precision(self.__hypothesis))

    def recall(self):
        return recall(self.__hypothesis))

    def get_statistics(self):
        return self.__learn_class.statistic()

def main():
    data = DataFile((PrologFile('surfing.data')))

    time_start = time.time()

    args = 'ciao'
    logger = 'probfoil'
    logfile = None
    log = init_logger()

    learn_class = ProbFOIL2
    learn = learn_class(data, logger=logger)

    hypothesis = learn.learn()
    time_total = time.time() - time_start

    rule = hypothesis
    rules = rule.to_clauses(rule.target.functor)

    # First rule is failing rule: don't print it if there are other rules.
    if len(rules) > 1:
        for rule in rules[1:]:
            print(rule)
    else:
        print(rules[0])
    print('==================== SCORES ====================')
    print('            Accuracy:\t', accuracy(hypothesis))
    print('           Precision:\t', precision(hypothesis))
    print('              Recall:\t', recall(hypothesis))
    print('================== STATISTICS ==================')
    for name, value in learn.statistics():
        print('%20s:\t%s' % (name, value))
    print('          Total time:\t%.4fs' % time_total)

    if logfile:
        logfile.close()