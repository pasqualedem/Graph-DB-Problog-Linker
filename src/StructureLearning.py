# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 17:14:20 2020

@author: PasqualeDeMarinis
"""
import random

from probfoil.data import DataFile
from probfoil.probfoil import ProbFOIL2, ProbFOIL
from probfoil.score import accuracy, precision, recall
import time

from problog.util import init_logger


class StructureLearner:
    def __init__(self, *data, log_file=None, seed=None):
        self.__data = DataFile(*data)
        self.__learner = None
        self.__hypothesis = None
        self.__rules = None
        if log_file is not None:
            self.__log_file = open(log_file, 'w')
        else:
            self.__log_file = None

        if seed:
            self.__seed = seed
        else:
            self.__seed = str(random.random())
        random.seed(self.__seed)

    def set_data(self, *data):
        self.__data = DataFile(*data)

    def set_log_file(self, log_file):
        self.__log_file = open(log_file, 'w')

    def learn(self, significance=None, max_rule_length=None, beam_size=5, m_estimator=1, deterministic=False):
        log_name = 'structure_learner'
        if self.__log_file is not None:
            log = init_logger(verbose=True, name=log_name, out=self.__log_file)
            log.info('Random seed: %s' % self.__seed)

        if deterministic:
            learn_class = ProbFOIL
        else:
            learn_class = ProbFOIL2

        self.__learner = learn_class(self.__data, logger=log_name, p=significance, l=max_rule_length,
                                     beam_size=beam_size, m=m_estimator)

        time_start = time.time()
        self.__hypothesis = self.__learner.learn()
        self.__rules = self.__hypothesis.to_clauses(self.__hypothesis.target.functor)

        # First rule is failing rule: don't consider it if there are other rules.
        if len(self.__rules) > 1:
            del self.__rules[0]
        return time.time() - time_start

    def get_learned_rules(self):
        return self.__rules

    def accuracy(self):
        return accuracy(self.__hypothesis)

    def precision(self):
        return precision(self.__hypothesis)

    def recall(self):
        return recall(self.__hypothesis)

    def get_statistics(self):
        return self.__learner.statistics()
