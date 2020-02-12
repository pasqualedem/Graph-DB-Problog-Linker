"""
from src.Query import DbmsQuery


dbmsQuery = DbmsQuery("MATCH (n:Person) RETURN ID(n), n.name AS name, n.age AS age",
                      "parse_props_array",
                      "test")

print(dbmsQuery.run_query())

dbmsQuery = DbmsQuery("MATCH (n:Person) RETURN ID(n), properties(n)",
                      "parse_property_map",
                      "test")

print(dbmsQuery.run_query())

dbmsQuery = DbmsQuery("MATCH(n:Person) OPTIONAL MATCH (n:Person)-[r]->(c:Car) RETURN n, TYPE(r), c",
                      "parse_node_rels_with_props",
                      "test")

print(dbmsQuery.run_query().__triples)

dbmsQuery = DbmsQuery("MATCH(n:Person) OPTIONAL MATCH (n:Person)-[r]->(c:Car) RETURN ID(n), properties(n), TYPE(r), "
                      "ID(c), properties(c)",
                      "parse_node_rels_with_props_map",
                      "test")

print(dbmsQuery.run_query())

dbmsQuery = DbmsQuery("MATCH(n:Person) OPTIONAL MATCH (n:Person)-[r]->(c:Car) RETURN "
                      "size(keys(n)), ID(n), n.name AS name, n.age AS age,"
                      "TYPE(r),"
                      "size(keys(c)), ID(c), c.brand as brand, c.targa as targa",
                      "parse_node_rels_with_props_array",
                      "test")

print(dbmsQuery.run_query())

dbmsQuery = DbmsQuery("MATCH(n:Person) OPTIONAL MATCH (n:Person)-[r]->(c:Car) RETURN ID(n), TYPE(r), ID(c)",
                      "parse_node_rels",
                      "test")

print(dbmsQuery.run_query())
"""

from src.Query import CloudQuery


class Test:
    def __init__(self):
        self.query = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> " \
                     "PREFIX dbp: <http://dbpedia.org/property/>" \
                     "SELECT ?subject ?label " \
                     "WHERE {  " \
                     "  ?subject a <http://dbpedia.org/ontology/Cheese>; " \
                     "  dbp:region <http://dbpedia.org/resource/Asturias> ;          " \
                     "  rdfs:label ?label." \
                     "}"

        self.dataset = "http://dbpedia.org/sparql"
        self.t = CloudQuery(self.query, self.dataset)

    def run(self):
        data = self.t.run_query()


test = Test()
test.run()
