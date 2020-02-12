import unittest
from src.Query import CloudQuery, DbmsQuery

"""
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


class DbmsQueryTest(unittest.TestCase):
    def test_parse_props_array(self):
        test = DbmsQuery("MATCH (n:Person) RETURN ID(n), n.name AS name, n.age AS age",
                         "parse_props_array",
                         "test")
        expected = [
            (15, 'name', 'Giuseppe'), (15, 'age', 19),
            (16, 'name', 'Pasquale'), (16, 'age', 17),
            (17, 'name', 'Sergio'), (17, 'age', 18),
            (18, 'name', 'Roberto'), (18, 'age', 15),
            (55, 'name', 'Luigi'), (55, 'age', 11),
            (56, 'name', 'Matteo'),
            (57, 'name', 'Francesco')
        ]

        self.assertEqual(test.run_query().get_triples(), expected)

    def test_parse_property_map(self):
        test = DbmsQuery("MATCH (n:Person) RETURN ID(n), properties(n)",
                         "parse_property_map",
                         "test")
        expected = [
            (15, 'name', 'Giuseppe'), (15, 'age', 19),
            (16, 'name', 'Pasquale'), (16, 'age', 17),
            (17, 'name', 'Sergio'), (17, 'age', 18),
            (18, 'name', 'Roberto'), (18, 'age', 15),
            (55, 'name', 'Luigi'), (55, 'age', 11),
            (56, 'name', 'Matteo'),
            (57, 'name', 'Francesco')
        ]

        self.assertEqual(test.run_query().get_triples(), expected)

    def test_parse_node_rels_with_props(self):
        test = DbmsQuery("MATCH(n:Person) OPTIONAL MATCH (n:Person)-[r]->(c:Car) RETURN n, TYPE(r), c",
                         "parse_node_rels_with_props",
                         "test")

        expected = [
            (15, 'OWNS', 19), (15, 'name', 'Giuseppe'), (15, 'age', 19),
            (19, 'brand', 'Suzuki'), (19, 'targa', '143'),
            (16, 'OWNS', 21), (16, 'name', 'Pasquale'), (16, 'age', 17),
            (21, 'brand', 'Audi'), (21, 'targa', '127'),
            (17, 'OWNS', 1), (17, 'name', 'Sergio'), (17, 'age', 18),
            (1, 'brand', 'Seat'), (1, 'targa', '124'),
            (18, 'name', 'Roberto'), (18, 'age', 15),
            (55, 'OWNS', 0), (55, 'name', 'Luigi'), (55, 'age', 11),
            (0, 'brand', 'Ford'), (0, 'targa', '123'),
            (56, 'name', 'Matteo'), (57, 'name', 'Francesco')
        ]

        self.assertEqual(test.run_query().get_triples(), expected)


class CloudQueryTest(unittest.TestCase):
    def test_run_query(self):
        query = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> " \
                "PREFIX dbp: <http://dbpedia.org/property/>" \
                "SELECT ?subject ?label " \
                "WHERE {  " \
                "  ?subject a <http://dbpedia.org/ontology/Cheese>; " \
                "  dbp:region <http://dbpedia.org/resource/Asturias> ;          " \
                "  rdfs:label ?label." \
                "}"

        dataset = "http://dbpedia.org/sparql"
        test = CloudQuery(query, dataset)
        expected = [
            ('http://dbpedia.org/resource/Casín_cheese', 'label-es', 'Queso Casín'),
            ('http://dbpedia.org/resource/Casín_cheese', 'label-en', 'Casín cheese'),
            ('http://dbpedia.org/resource/Gamonéu_cheese', 'label-es', 'Queso de Gamonéu'),
            ('http://dbpedia.org/resource/Gamonéu_cheese', 'label-it', 'Queso de Gamonéu'),
            ('http://dbpedia.org/resource/Gamonéu_cheese', 'label-en', 'Gamonéu cheese')
        ]

        self.assertEqual(test.run_query().get_triples(), expected)


if __name__ == '__main__':
    unittest.main()
