# -*- coding: utf-8 -*-
## @package Data
# Implements class for Data representation
# @author Pasquale De Marinis, Barile Roberto, Caputo Sergio
from collections import defaultdict


##
# Implements class for Data representation
class Data:

    ## The constructor
    # @param: triples: list of subject - predicate - object tuples
    # @param: length: number of tuples in triples
    def __init__(self, triples, length):
        self.__triples = triples
        self.__length = length

    ## Set the triples of Data object
    # @param: triples: list of subject - predicate - object tuples
    def set_triples(self, triples):
        self.__triples = triples

    def get_triples(self):
        return self.__triples

    ## Create a nested dictionary to count how many times a value appears for property
    def learn_tagging_probabilities(self):
        triple_names = defaultdict(dict)

        for prop, value in self.__triples:
            if prop not in triple_names.keys():
                triple_names[prop][value] = 1
            else:
                if value in triple_names[prop].keys():
                    triple_names[prop][value] = triple_names[prop][value] + 1
                else:
                    triple_names[prop][value] = 1
        return triple_names

