from src.IGraphDBQuery import IGraphDBQuery
from SPARQLWrapper import SPARQLWrapper, JSON  # pip install sparqlwrapper
from src.Data import Data


class DbmsQuery(IGraphDBQuery):

    def __init__(self, query, dataset):
        self.__query = query
        self.__dataset = dataset
        self.__sparql = SPARQLWrapper(dataset)

    def run_query(self):
        self.__sparql.setReturnFormat(JSON)
        results = self.__sparql.query().convert()
        triple = []
        length = 0
        for results in results["results"]["bindings"]:
            triple.append(results["p"]["value"])
            triple.append(results["o"]["value"])
            triple.append(results["s"]["value"])
            length = length + 1
        data = Data(triple, length)
        return data

    def set_query(self, query):
        self.__query = query
        self.__sparql.setQuery(query)

    def get_query(self):
        return self.__query

    def get_dataset(self):
        return self.__dataset

