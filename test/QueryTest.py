import unittest
from src.Query import CloudQuery, DbmsQuery

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
                "  dbp:region <http://dbpedia.org/resource/Asturias> ;" \
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

    def test_run_query_2(self):
        query = "PREFIX dbo: <http://dbpedia.org/ontology/>" \
                "PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> " \
                "PREFIX foaf: <http://xmlns.com/foaf/0.1/> " \
                "PREFIX : <http://dbpedia.org/resource/> " \
                "SELECT ?subject ?name ?birth ?death " \
                "WHERE { " \
                "   ?subject dbo:birthPlace :Berlin . " \
                "   ?subject dbo:birthDate ?birth . " \
                "   ?subject foaf:name ?name . " \
                "   ?subject dbo:deathDate ?death . " \
                "   FILTER (?birth < \"1900-01-01\"^^xsd:date) ." \
                "} " \
                "ORDER BY ?name LIMIT 20"

        dataset = "http://dbpedia.org/sparql"
        test = CloudQuery(query, dataset)

        expected = [
            ('http://dbpedia.org/resource/Annot_(artist)', 'name-en', '"Annot" (Annot Jacobi)'),
            ('http://dbpedia.org/resource/Annot_(artist)', 'birth', '1894-12-27'),
            ('http://dbpedia.org/resource/Annot_(artist)', 'death', '1981-10-20'),
            ('http://dbpedia.org/resource/Prince_Adalbert_of_Prussia_(1811–1873)', 'name-en', '()'),
            ('http://dbpedia.org/resource/Prince_Adalbert_of_Prussia_(1811–1873)', 'birth', '1811-10-29'),
            ('http://dbpedia.org/resource/Prince_Adalbert_of_Prussia_(1811–1873)', 'death', '1873-06-06'),
            ('http://dbpedia.org/resource/Prince_Adalbert_of_Prussia_(1811–1873)', 'name-en', '()'),
            ('http://dbpedia.org/resource/Prince_Adalbert_of_Prussia_(1811–1873)', 'birth', '1811-10-29'),
            ('http://dbpedia.org/resource/Prince_Adalbert_of_Prussia_(1811–1873)', 'death', '1873-6-6'),
            ('http://dbpedia.org/resource/Prince_Adalbert_of_Prussia_(1811–1873)', 'name-en', '(Henry William Adalbert)'),
            ('http://dbpedia.org/resource/Prince_Adalbert_of_Prussia_(1811–1873)', 'birth', '1811-10-29'),
            ('http://dbpedia.org/resource/Prince_Adalbert_of_Prussia_(1811–1873)', 'death', '1873-06-06'),
            ('http://dbpedia.org/resource/Prince_Adalbert_of_Prussia_(1811–1873)', 'name-en', '(Henry William Adalbert)'),
            ('http://dbpedia.org/resource/Prince_Adalbert_of_Prussia_(1811–1873)', 'birth', '1811-10-29'),
            ('http://dbpedia.org/resource/Prince_Adalbert_of_Prussia_(1811–1873)', 'death', '1873-6-6'),
            ('http://dbpedia.org/resource/Abraham_Mendelssohn_Bartholdy', 'name-en', 'Abraham Mendelssohn Bartholdy'),
            ('http://dbpedia.org/resource/Abraham_Mendelssohn_Bartholdy', 'birth', '1776-12-10'),
            ('http://dbpedia.org/resource/Abraham_Mendelssohn_Bartholdy', 'death', '1835-11-19'),
            ('http://dbpedia.org/resource/Ludwig_Achim_von_Arnim', 'name-en', 'Achim von Arnim'),
            ('http://dbpedia.org/resource/Ludwig_Achim_von_Arnim', 'birth', '1781-01-26'),
            ('http://dbpedia.org/resource/Ludwig_Achim_von_Arnim', 'death', '1831-1-21'),
            ('http://dbpedia.org/resource/Prince_Adalbert_of_Prussia_(1811–1873)', 'name-en', 'Adalbert of Prussia'),
            ('http://dbpedia.org/resource/Prince_Adalbert_of_Prussia_(1811–1873)', 'birth', '1811-10-29'),
            ('http://dbpedia.org/resource/Prince_Adalbert_of_Prussia_(1811–1873)', 'death', '1873-06-06'),
            ('http://dbpedia.org/resource/Prince_Adalbert_of_Prussia_(1811–1873)', 'name-en', 'Adalbert of Prussia'),
            ('http://dbpedia.org/resource/Prince_Adalbert_of_Prussia_(1811–1873)', 'birth', '1811-10-29'),
            ('http://dbpedia.org/resource/Prince_Adalbert_of_Prussia_(1811–1873)', 'death', '1873-6-6'),
            ('http://dbpedia.org/resource/Adam_Müller', 'name-en', 'Adam Müller'),
            ('http://dbpedia.org/resource/Adam_Müller', 'birth', '1779-06-30'),
            ('http://dbpedia.org/resource/Adam_Müller', 'death', '1829-01-17'),
            ('http://dbpedia.org/resource/Adam_Müller', 'name-en', 'Adam Müller'),
            ('http://dbpedia.org/resource/Adam_Müller', 'birth', '1779-06-30'),
            ('http://dbpedia.org/resource/Adam_Müller', 'death', '1829-1-17'), (
                'http://dbpedia.org/resource/Adolf_Brand', 'name-en', 'Adolf Brand'),
            ('http://dbpedia.org/resource/Adolf_Brand', 'birth', '1874-11-14'),
            ('http://dbpedia.org/resource/Adolf_Brand', 'death', '1945-2-2'),
            ('http://dbpedia.org/resource/Adolf_Christen', 'name-en', 'Adolf Christen'),
            ('http://dbpedia.org/resource/Adolf_Christen', 'birth', '1811-08-07'),
            ('http://dbpedia.org/resource/Adolf_Christen', 'death', '1883-07-13'),
            ('http://dbpedia.org/resource/Adolf_Christen', 'name-en', 'Adolf Christen'),
            ('http://dbpedia.org/resource/Adolf_Christen', 'birth', '1811-08-07'),
            ('http://dbpedia.org/resource/Adolf_Christen', 'death', '1883-7-13'),
            ('http://dbpedia.org/resource/Adolf_Damaschke', 'name-en', 'Adolf Damaschke'),
            ('http://dbpedia.org/resource/Adolf_Damaschke', 'birth', '1865-11-24'),
            ('http://dbpedia.org/resource/Adolf_Damaschke', 'death', '1935-7-30'),
            ('http://dbpedia.org/resource/Adolf_Erman', 'name-en', 'Adolf Erman'),
            ('http://dbpedia.org/resource/Adolf_Erman', 'birth', '1854-10-31'),
            ('http://dbpedia.org/resource/Adolf_Erman', 'death', '1937-6-26'),
            ('http://dbpedia.org/resource/Adolf_Gärtner', 'name-en', 'Adolf Gärtner'),
            ('http://dbpedia.org/resource/Adolf_Gärtner', 'birth', '1879-03-24'),
            ('http://dbpedia.org/resource/Adolf_Gärtner', 'death', '1958-01-09'),
            ('http://dbpedia.org/resource/Adolf_Gärtner', 'name-en', 'Adolf Gärtner'),
            ('http://dbpedia.org/resource/Adolf_Gärtner', 'birth', '1879-03-24'),
            ('http://dbpedia.org/resource/Adolf_Gärtner', 'death', '1958-1-9'),
            ('http://dbpedia.org/resource/Adolf_Heinrich_von_Arnim-Boitzenburg', 'name-en', 'Adolf Heinrich von Arnim-Boitzenburg'),
            ('http://dbpedia.org/resource/Adolf_Heinrich_von_Arnim-Boitzenburg', 'birth', '1803-04-10'),
            ('http://dbpedia.org/resource/Adolf_Heinrich_von_Arnim-Boitzenburg', 'death', '1868-01-08'),
            ('http://dbpedia.org/resource/Adolf_Heinrich_von_Arnim-Boitzenburg', 'name-en', 'Adolf Heinrich von Arnim-Boitzenburg'),
            ('http://dbpedia.org/resource/Adolf_Heinrich_von_Arnim-Boitzenburg', 'birth', '1803-04-10'),
            ('http://dbpedia.org/resource/Adolf_Heinrich_von_Arnim-Boitzenburg', 'death', '1868-1-8')
        ]
        
        self.assertEquals(test.run_query().get_triples(), expected)


if __name__ == '__main__':
    unittest.main()
