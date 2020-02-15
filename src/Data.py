# -*- coding: utf-8 -*-
## @package Data
# @author Pasquale De Marinis, Barile Roberto, Caputo Sergio
from collections import defaultdict
from problog.program import SimpleProgram
from problog.logic import Constant, Var, Term, AnnotatedDisjunction
from src.Distribution import Normal, Multinomial
from Util import get_type


## Implements class for Data representation
class Data:

    ## The constructor
    # @param: triples: list of list of (subject - predicate - object) tuples
    # @param: length: number of tuples in triples
    def __init__(self, data: [[tuple]], length):
        self.__data = data
        self.__length = length

    ## Set the triples of Data object
    # @param: triples: list of subject - predicate - object tuples
    def set_triples(self, triples):
        self.__data = triples

    def get_data(self):
        return self.__data

    def to_examples(self, examples=[]):
        term_dict = {}
        prop = Term('prop')
        for possible_world in self.__data:
            example = []
            for triple in possible_world:
                if term_dict.get(triple[1]) is None:
                    term_dict[triple[1]] = get_type(triple[1])
                if term_dict.get(triple[0]) is None:
                    term_dict[triple[0]] = get_type(triple[0])
                example.append((prop(term_dict[triple[0]], term_dict[triple[1]]), triple[2]))
                examples.append(example)
        return examples
      
    def learn_distributions(self, properties=dict()):

        for possible_world in self.__data:
            for triple in possible_world:
                prop_name = triple[1]
                value = triple[2]
                if properties is not None and prop_name in properties.keys():
                    prop = properties[prop_name]
                    prop.get_distribution().add(value)
                else:
                    if type(value) is float:
                        new_prop = Property(prop_name, Normal())
                        new_prop.get_distribution().add(value)
                        properties[prop_name] = new_prop
                    else:
                        new_prop = Property(prop_name, Multinomial())
                        new_prop.get_distribution().add(value)
                        properties[prop_name] = new_prop

        return properties

    ## Parse a list of triples into a SimpleProgram
    # @return: program: a SimpleProgram that contains a list of clauses prop(subj, pred, obj)
    def parse(self, program=SimpleProgram()):
        prop = Term('prop')
        term_dict = dict()
        for row in self.__data:
            for triple in row:
                if term_dict.get(triple[1]) is None:
                    term_dict[triple[1]] = get_type(triple[1])(triple[1])
                if term_dict.get(triple[0]) is None:
                    term_dict[triple[0]] = get_type(triple[0])(triple[0])
                if term_dict.get(triple[2]) is None:
                    term_dict[triple[2]] = get_type(triple[2])(triple[2])
                pred = term_dict[triple[1]]
                subj = term_dict[triple[0]]
                obj = term_dict[triple[2]]
                program += prop(subj, pred, obj)

        return program


class PropertyMap(dict):
    ## create a simple program from property clauses
    def to_simple_program(self, program=SimpleProgram()):
        for prop in self.values():
            program += prop.to_atom()
        return program


class Property:

    def __init__(self, name, distribution):
        self.__name = name
        self.__distribution = distribution

    ## create a list of clauses from property
    def to_atom(self):
        prop = Term('prop')
        true = Term('true')
        name = get_type(self.__name)
        clauses = []
        sub = Term('_generic_individual_')
        dic = self.__distribution.get_parameters()
        values = dic.keys()
        for value in values:
            t_value = get_type(value)
            clauses.append(prop(sub, name, t_value, p=dic[value]))

        return AnnotatedDisjunction(clauses, true)

    def get_distribution(self):
        return self.__distribution
