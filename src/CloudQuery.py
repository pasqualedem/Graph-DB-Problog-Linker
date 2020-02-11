# -*- coding: utf-8 -*-
## @package CloudQuery
# Implements class for SPARQL query
# @author Pasquale De Marinis, Barile Roberto, Caputo Sergio
from src.IGraphDBQuery import IGraphDBQuery
from SPARQLWrapper import SPARQLWrapper, JSON  # pip install sparqlwrapper
from src.Data import Data


##
# Implements class to operate with SPARQL query
class CloudQuery(IGraphDBQuery):

    ## The constructor
    # @param: query: query to run on endpoint
    # @param: dataset: endpoint
    def __init__(self, query, dataset):
        self.__query = query
        self.__dataset = dataset
        self.__sparql = SPARQLWrapper(dataset)

    def run_query(self):
        self.__sparql.setReturnFormat(JSON)
        results = self.__sparql.query().convert()
        triples = []
        length = 0
        for results in results["results"]["bindings"]:
            triples.append((results["s"]["value"], results["p"]["value"], results["o"]["value"]))
            length = length + 1
        data = Data(triples, length)
        return data

    ## Set query for CloudQuery object
    # @param: query: query to run on endpoint
    def set_query(self, query):
        self.__query = query
        self.__sparql.setQuery(query)

    def get_query(self):
        return self.__query

    def get_dataset(self):
        return self.__dataset

