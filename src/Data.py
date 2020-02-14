# -*- coding: utf-8 -*-
## @package Data
# @author Pasquale De Marinis, Barile Roberto, Caputo Sergio
from collections import defaultdict
from problog.program import SimpleProgram
from problog.logic import Constant, Var, Term, AnnotatedDisjunction
from src.Distribution import Distribution, Normal, Multinomial


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

    def to_examples(self):
        term_dict = {}
        prop = Term('prop')
        examples = []
        for possible_world in self.__data:
            example = []
            for triple in possible_world:
                if term_dict.get(triple[1]) is None:
                    term_dict[triple[1]] = Constant(triple[1])
                if term_dict.get(triple[0]) is None:
                    term_dict[triple[0]] = Constant(triple[0])
                example.append((prop(term_dict[triple[0]], term_dict[triple[1]]), triple[2]))
                examples.append(example)
        return examples

    def learn_distributions(self, properties):

        for prop_name, value in self.__data:
            if prop_name in properties.keys():
                prop = properties[prop_name]
                prop.distribution.add(value)
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
    def parse(self):
        program = SimpleProgram()
        prop = Term('prop')
        const_dict = dict()
        for row in self.__data:
            for triple in row:
                if const_dict.get(triple[1]) is None:
                    const_dict[triple[1]] = Constant(triple[1])
                if const_dict.get(triple[0]) is None:
                    const_dict[triple[0]] = Constant(triple[0])
                if const_dict.get(triple[2]) is None:
                    const_dict[triple[2]] = Constant(triple[2])
                pred = const_dict[triple[1]]
                subj = const_dict[triple[0]]
                obj = const_dict[triple[2]]
                program += prop(subj, pred, obj)

        return program


class PropertyMap(dict):
    ## create a simple program from property clauses
    def to_simple_program(self):
        program = SimpleProgram()
        for property in self.values:
            program += property.to_atom()
        return program


class Property:

    def __init__(self, name, distribution):
        self.__name = name
        self.__distribution = distribution

    ## create a list of clauses from property
    def to_atom(self):
        prop = Term('prop')
        I = Var('I')
        clauses = []

        dic = self.__distribution.get_parameters()
        values = dic.keys()
        for value in values:
            clauses.append(prop(I, self.__name, Constant(value), p=dic[value]))

        return AnnotatedDisjunction(clauses)

    def get_distribution(self):
        return self.__distribution
