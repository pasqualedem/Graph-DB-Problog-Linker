from src.IGraphDBQuery import IGraphDBQuery
from py2neo import Graph

class DbmsQuery(IGraphDBQuery):
    def __init__(self, query, password):
        self.__query = query
        self.__password = password
        self.__graph = Graph(self.__password)

    def run_query(self):
        return self.__graph.run(self.__query).to_table()

    def set_query(self, query):
        self.__query = query
