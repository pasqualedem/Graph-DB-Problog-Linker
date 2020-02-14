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
    # @param: triples: list of subject - predicate - object tuples
    # @param: length: number of tuples in triples
    def __init__(self, triples, length):
        self.__triples = triples
        self.__length = length

    ## doc
    #
    def set_property_types(self, property_types):
        self.__property_types = property_types

    ## Set the triples of Data object
    # @param: triples: list of subject - predicate - object tuples
    def set_triples(self, triples):
        self.__triples = triples

    def get_triples(self):
        return self.__triples

    def learn_distributions(self, properties):

        for prop_name, value in self.__triples:
            if prop_name in properties.keys():
                prop = properties[prop_name]
                if prop.distribution is not None:
                    prop.distribution.add(value)
                else:
                    if type(value) is float:
                        normal = Normal()
                        normal.add(value)
                        properties[prop_name].distribution = normal
                    else:
                        multinomial = Multinomial()
                        multinomial.add(value)
                        properties[prop_name].distribution = multinomial

        return PropertyMap(properties)

    ## Parse a list of triples into a SimpleProgram
    # @return: program: a SimpleProgram that contains a list of clauses prop(subj, pred, obj)
    def parse(self):
        program = SimpleProgram()
        prop = Term('prop')
        const_dict = dict()
        for triple in self.__data:
            if const_dict[triple[1]] is None:
                const_dict[triple[1]] = Constant(triple[1])
            if const_dict[triple[0]] is None:
                const_dict[triple[0]] = Constant(triple[0])
            if const_dict[triple[2]] is None:
                const_dict[triple[2]] = Constant(triple[2])
            pred = const_dict[triple[1]]
            subj = const_dict[triple[0]]
            obj = const_dict[triple[2]]
            program += prop(subj, pred, obj)

            return program


class PropertyMap(dict):

    def __init__(self, properties):
        self.__properties = properties

    ## create a simple program from property clauses
    def to_simple_program(self):
        program = SimpleProgram()
        for property in self.__properties:
            program += property.to_atom()
        return program


class Property:

    def __init__(self, name, distribution, type):
        self.__name = name
        self.distribution = distribution
        self.type = type

    ## create a list of clauses from property
    def to_atom(self):
        prop = Term('prop')
        I = Var('I')
        clauses = []

        dic = self.distribution.get_parameters()
        values = dic.keys()
        for value in values:
            clauses.append(prop(I, self.__name, Constant(value), p=dic[value]))

        return AnnotatedDisjunction(clauses)
