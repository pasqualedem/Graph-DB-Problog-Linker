# -*- coding: utf-8 -*-
## @package Query
# Implements class for query execution, both for DBMS (Neo4j) and SPARQL
# @author Pasquale De Marinis, Barile Roberto, Caputo Sergio

from py2neo import Graph
from src.IGraphDBQuery import IGraphDBQuery
from SPARQLWrapper import SPARQLWrapper, JSON  # pip install sparqlwrapper
from src.Data import Data


## parse to triples result of a query with return like RETURN ID(n), n.prop1, ..., n.propN
def parse_props_array(query_result):
    triples = []
    length = 0
    while query_result.forward():
        id = query_result.current[0]
        property_number = len(query_result.current)
        length = 0
        for i in range(1, property_number):
            triple = (id,)
            if query_result.current[i] is None:
                continue
            triple += (query_result.current.keys()[i], query_result.current[i])
            triples.append(triple)
            length += 1

    return triples, length


# parse to triples result of a query with return like RETURN n
def parse_node(query_result):
    triples = []
    length = 0
    while query_result.forward():
        id = query_result.current[0].identity
        property_map = query_result.current[0]

        for key in property_map.keys():
            triple = (id,)
            triple += (key, property_map.get(key))
            triples.append(triple)
            length += 1

    return triples, length


# parse to triples result of a query with return like RETURN ID(n), properties(n)
def parse_property_map(query_result):
    triples = []
    length = 0
    while query_result.forward():
        id = query_result.current[0]
        property_map = query_result.current[1]

        for key in property_map.keys():
            triple = (id,)
            triple += (key, property_map.get(key))
            triples.append(triple)
            length += 1

    return triples, length


# parse to triples result of a query with return like RETURN n, TYPE(r), m
def parse_node_rels_with_props(query_result):
    triples = []
    length = 0
    while query_result.forward():
        first_node = query_result.current[0]
        relationship = query_result.current[1]
        second_node = query_result.current[2]

        if relationship is not None:
            triple = (first_node.identity, relationship, second_node.identity)
            triples.append(triple)
            length += 1

        if first_node is not None:
            for key in first_node.keys():
                triple = (first_node.identity,)
                triple += (key, first_node.get(key))
                if triple not in triples:
                    triples.append(triple)
                    length += 1

        if second_node is not None:
            for key in second_node.keys():
                triple = (second_node.identity,)
                triple += (key, second_node.get(key))
                if triple not in triples:
                    triples.append(triple)
                    length += 1

    return triples, length


# parse to triples result of a query with return like RETURN ID(n), properties(n), TYPE(r), ID(m), properties(m)
def parse_node_rels_with_props_map(query_result):
    triples = []
    length = 0
    while query_result.forward():
        first_node_id = query_result.current[0]
        first_node_property_map = query_result.current[1]
        relationship = query_result.current[2]
        second_node_id = query_result.current[3]
        second_node_property_map = query_result.current[4]

        if relationship is not None:
            triple = (first_node_id, relationship, second_node_id)
            triples.append(triple)
            length += 1

        if first_node_property_map is not None:
            for key in first_node_property_map.keys():
                triple = (first_node_id,)
                triple += (key, first_node_property_map.get(key))
                if triple not in triples:
                    triples.append(triple)
                    length += 1

        if second_node_property_map is not None:
            for key in second_node_property_map.keys():
                triple = (second_node_id,)
                triple += (key, second_node_property_map.get(key))
                if triple not in triples:
                    triples.append(triple)
                    length += 1

    return triples, length


# parse to triples result of a query with return like RETURN ID(n), TYPE(r), ID(m)
def parse_node_rels(query_result):
    triples = []
    length = 0
    while query_result.forward():
        first_node_id = query_result.current[0]
        relationship = query_result.current[1]
        second_node_ip = query_result.current[2]
        if relationship is not None:
            triple = (first_node_id, relationship, second_node_ip)
            triples.append(triple)
            length += 1

    return triples, length


# parse to triples result of a query with return like RETURN size(keys(n)), ID(n), n.prop1, ..., n.propN, TYPE(r), size(keys(m)), ID(m), m.prop1, ..., m.propM
def parse_node_rels_with_props_array(query_result):
    triples = []
    length = 0
    while query_result.forward():
        first_node_property_number = query_result.current[0]
        first_node_id = query_result.current[1]
        first_node_first_attribute_index = 2
        relationship_index = first_node_property_number + first_node_first_attribute_index
        second_node_property_number = query_result.current[relationship_index + 1]
        second_node_id = query_result.current[relationship_index + 2]
        second_node_first_attribute_index = relationship_index + 3

        if query_result.current[relationship_index] is not None:
            triple = (first_node_id, query_result.current[relationship_index], second_node_id)
            triples.append(triple)

        if query_result.current[first_node_first_attribute_index] is not None:
            for i in range(first_node_first_attribute_index,
                           first_node_property_number + first_node_first_attribute_index):
                triple = (first_node_id,)
                if query_result.current[i] is None:
                    continue
                triple += (query_result.current.keys()[i], query_result.current[i])
                triples.append(triple)
                length += 1

        if query_result.current[second_node_first_attribute_index] is not None:
            for i in range(second_node_first_attribute_index,
                           second_node_property_number + second_node_first_attribute_index):
                triple = (second_node_id,)
                if query_result.current[i] is None:
                    continue
                triple += (query_result.current.keys()[i], query_result.current[i])
                triples.append(triple)
                length += 1

    return triples, length


##
# Implements class to operate with query on Neo4j DBMS
class DbmsQuery(IGraphDBQuery):
    ## The constructor
    # @param: query: query to run on the DBMS
    # @param: parse: name of the function for the result parsing to triples
    # @param: password: password for the Neo4j graph
    def __init__(self, query, parse, password="test"):
        self.__query = query
        self.__parse = parse
        self.__password = password
        self.__graph = Graph(password=self.__password)

    ## Run specified query
    def run_query(self):
        possibles = globals().copy()
        possibles.update(locals())
        function = possibles.get(self.__parse)
        triples, length = function(self.__graph.run(self.__query))
        data = Data(triples, length)

        return data

    ## Set query for DbmsQuery object
    # @param: query: query to run on graph
    def set_query(self, query):
        self.__query = query


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

    ## Run specified query
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
