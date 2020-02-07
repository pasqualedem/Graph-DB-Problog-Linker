from src.IGraphDBQuery import IGraphDBQuery
from py2neo import Graph


def parse_features_array(query_result):
    triples = []
    while query_result.forward():
        id = query_result.current[0]
        property_number = len(query_result.current)

        for i in range(1, property_number):
            triple = (id,)
            if query_result.current[i] is None:
                continue
            triple += (query_result.current.keys()[i], query_result.current[i])
            triples.append(triple)

    return triples


def parse_node(query_result):
    triples = []
    while query_result.forward():
        id = query_result.current[0].identity
        property_map = query_result.current[0]

        for key in property_map.keys():
            triple = (id,)
            triple += (key, property_map.get(key))
            triples.append(triple)

    return triples


def parse_property_map(query_result):
    triples = []
    while query_result.forward():
        id = query_result.current[0]
        property_map = query_result.current[1]

        for key in property_map.keys():
            triple = (id,)
            triple += (key, property_map.get(key))
            triples.append(triple)

    return triples


def parse_node_rels_with_props(query_result):
    triples = []
    while query_result.forward():
        first_node = query_result.current[0]
        relationship = query_result.current[1]
        second_node = query_result.current[2]

        if relationship is not None:
            triple = (first_node.identity, relationship, second_node.identity)
            triples.append(triple)

        if first_node is not None:
            for key in first_node.keys():
                triple = (first_node.identity,)
                triple += (key, first_node.get(key))
                if triple not in triples:
                    triples.append(triple)

        if second_node is not None:
            for key in second_node.keys():
                triple = (second_node.identity,)
                triple += (key, second_node.get(key))
                if triple not in triples:
                    triples.append(triple)

    return triples


def parse_node_rels_with_props_map(query_result):
    triples = []
    while query_result.forward():
        first_node_id = query_result.current[0]
        first_node_property_map = query_result.current[1]
        relationship = query_result.current[2]
        second_node_id = query_result.current[3]
        second_node_property_map = query_result.current[4]

        if relationship is not None:
            triple = (first_node_id, relationship, second_node_id)
            triples.append(triple)

        if first_node_property_map is not None:
            for key in first_node_property_map.keys():
                triple = (first_node_id,)
                triple += (key, first_node_property_map.get(key))
                if triple not in triples:
                    triples.append(triple)

        if second_node_property_map is not None:
            for key in second_node_property_map.keys():
                triple = (second_node_id,)
                triple += (key, second_node_property_map.get(key))
                if triple not in triples:
                    triples.append(triple)

    return triples


def parse_node_rels(query_result):
    triples = []
    while query_result.forward():
        first_node_id = query_result.current[0]
        relationship = query_result.current[1]
        second_node_ip = query_result.current[2]
        if relationship is not None:
            triple = (first_node_id, relationship, second_node_ip)
            triples.append(triple)

    return triples


def parse_node_rels_with_features_array(query_result):
    triples = []
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

        for i in range(first_node_first_attribute_index, first_node_property_number + first_node_first_attribute_index):
            triple = (first_node_id,)
            if query_result.current[i] is None:
                continue
            triple += (query_result.current.keys()[i], query_result.current[i])
            triples.append(triple)

        if query_result.current[second_node_first_attribute_index] is not None:
            for i in range(second_node_first_attribute_index,
                           second_node_property_number + second_node_first_attribute_index):
                triple = (second_node_id,)
                if query_result.current[i] is None:
                    continue
                triple += (query_result.current.keys()[i], query_result.current[i])
                triples.append(triple)

    return triples


"""
Takes a Neo4j query result in several formats and generates triples
Triples represent nodes relations and node properties (both optional)
It generates quadruples for probabilistic queries 
"""


class DbmsQuery(IGraphDBQuery):
    def __init__(self, query, parse, password):
        self.__query = query
        self.__parse = parse
        self.__password = password
        self.__graph = Graph(password=self.__password)

    def run_query(self):
        possibles = globals().copy()
        possibles.update(locals())
        function = possibles.get(self.__parse)
        return function(self.__run_query())

    def __run_query(self):
        return self.__graph.run(self.__query)

    def set_query(self, query):
        self.__query = query
