# -*- coding: utf-8 -*-
## @package Data
# @author Pasquale De Marinis, Barile Roberto, Caputo Sergio
from collections import defaultdict
from problog.program import SimpleProgram
from problog.logic import Constant, Var, Term, AnnotatedDisjunction
from Distribution import Normal, Multinomial, Continuous, Discrete
from Util import get_type, ClauseBuilder


##
# Class that implements the data representation
class Data:

    ## The constructor
    # @param: triples: list of list of (subject - predicate - object) tuples
    # @param: length: number of tuples in triples
    # @param: triple_mode: if true atoms will be prop(subj, pred, obj) else will be pred(subj, obj)
    def __init__(self, data: [[tuple]], length, triple_mode=False):
        self.__triple_mode = triple_mode
        self.__data = data
        self.__length = length

    ## Set the triples of Data object
    # @param: triples: list of subject - predicate - object tuples
    def set_triples(self, triples):
        self.__data = triples

    ## Set the triple mode truthness of Data object
    # @param: triple_mode: if true atoms will be prop(subj, pred, obj) else will be pred(subj, obj)
    def set_triple_mode(self, triple_mode):
        self.__triple_mode = triple_mode

    ## Get the triple mode truthness of Data object
    def get_triple_mode(self):
        return self.__triple_mode

    ## Get the triples of Data object
    # @returns triples
    def get_data(self):
        return self.__data

    ## Create examples from triples
    # @returns list of examples
    def to_examples(self, examples=[]):
        cb = ClauseBuilder(self.__triple_mode)
        term_dict = {}
        for possible_world in self.__data:
            example = []
            for triple in possible_world:
                if term_dict.get(triple[1]) is None:
                    term_dict[triple[1]] = get_type(triple[1])
                if term_dict.get(triple[0]) is None:
                    term_dict[triple[0]] = get_type(triple[0])
                example.append((cb.get_clause(term_dict[triple[0]], term_dict[triple[1]]), triple[2]))
                examples.append(example)
        return examples

    ## Learn the property distribution for each property in properties
    # @param: properties: dictionary of properties
    # @return properties: dictionary of properties with their distributions
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
    # @return: program: a SimpleProgram that contains a list of clauses prop(subj, pred, obj) or pred(subj, obj)
    def parse(self, program=SimpleProgram()):
        cb = ClauseBuilder(self.__triple_mode)
        term_dict = dict()
        for row in self.__data:
            for triple in row:
                if term_dict.get(triple[1]) is None:
                    term_dict[triple[1]] = get_type(triple[1])
                if term_dict.get(triple[0]) is None:
                    term_dict[triple[0]] = get_type(triple[0])
                if term_dict.get(triple[2]) is None:
                    term_dict[triple[2]] = get_type(triple[2])
                pred = term_dict[triple[1]]
                subj = term_dict[triple[0]]
                obj = term_dict[triple[2]]
                program += cb.get_clause(subj, pred, obj)

        return program


##
# Implements class for simple program creation
class PropertyMap(dict):

    ## Create a simple program from property clauses
    # @return program
    def to_simple_program(self, program=SimpleProgram(), triple_mode=False):
        for prop in self.values():
            program += prop.to_clause(triple_mode)
        return program


##
# Represents a property with the related distribution probability
class Property:

    ## The constructor
    def __init__(self, name, distribution, subj_name="__generic_individual__"):
        self.__subj_name = subj_name
        self.__name = name
        self.__distribution = distribution

    ## create a clause from property and his distribution
    # @param: triple_mode: if true atoms will be prop(subj, pred, obj) else will be pred(subj, obj)
    # @return annotated disjunction of the clauses or a fact if distributions is Continuous
    def to_clause(self, triple_mode=False):
        if issubclass(type(self.__distribution), Continuous):
            return self.__to_fact()
        elif issubclass(type(self.__distribution), Discrete):
            return self.__to_annotated_disjunction(triple_mode)
        else:
            raise Exception

    ## create a fact with a continuous distribuction as probability
    def __to_fact(self):
        mu, sigma = self.__distribution.get_parameters()
        distribuction = Term(type(self.__distribution).name)(Constant(mu), Constant(sigma))
        return Term(self.__name, p=distribuction)

    ## create an annoteted disjunction from property
    def __to_annotated_disjunction(self, triple_mode):
        cb = ClauseBuilder(triple_mode)
        true = Term('true')
        name = get_type(self.__name)
        clauses = []
        sub = get_type(self.__subj_name)
        dic = self.__distribution.get_parameters()
        values = dic.keys()
        for value in values:
            t_value = get_type(value)
            clauses.append(cb.get_clause(sub, name, t_value, prob=dic[value]))

        return AnnotatedDisjunction(clauses, true)

    ## Get the distribution of the property
    # @return distribution
    def get_distribution(self):
        return self.__distribution
