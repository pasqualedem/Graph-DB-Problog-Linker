import unittest
from src.query import CloudQuery, DbmsQuery


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
        expected = [[('http___dbpedia_org_resource_Casín_cheese', 'label_es', 'Queso Casín')],
                    [('http___dbpedia_org_resource_Casín_cheese', 'label_en', 'Casín cheese')],
                    [('http___dbpedia_org_resource_Gamonéu_cheese', 'label_es', 'Queso de Gamonéu')],
                    [('http___dbpedia_org_resource_Gamonéu_cheese', 'label_it', 'Queso de Gamonéu')],
                    [('http___dbpedia_org_resource_Gamonéu_cheese', 'label_en', 'Gamonéu cheese')]]
        result = test.run_query().get_data()
        self.assertEqual(result, expected)

    def test_run_query_2(self):
        query = "PREFIX dbo: <http://dbpedia.org/ontology/> " \
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

        expected = [[('http___dbpedia_org_resource_Annot__artist_', 'name_en', '"Annot" _Annot Jacobi_'),
                     ('http___dbpedia_org_resource_Annot__artist_', 'birth', '1894_12_27'),
                     ('http___dbpedia_org_resource_Annot__artist_', 'death', '1981_10_20')],
                    [('http___dbpedia_org_resource_Prince_Adalbert_of_Prussia__1811–1873_', 'name_en', '__'),
                     ('http___dbpedia_org_resource_Prince_Adalbert_of_Prussia__1811–1873_', 'birth', '1811_10_29'),
                     ('http___dbpedia_org_resource_Prince_Adalbert_of_Prussia__1811–1873_', 'death', '1873_06_06')],
                    [('http___dbpedia_org_resource_Prince_Adalbert_of_Prussia__1811–1873_', 'name_en', '__'),
                     ('http___dbpedia_org_resource_Prince_Adalbert_of_Prussia__1811–1873_', 'birth', '1811_10_29'),
                     ('http___dbpedia_org_resource_Prince_Adalbert_of_Prussia__1811–1873_', 'death', '1873_6_6')],
                    [('http___dbpedia_org_resource_Prince_Adalbert_of_Prussia__1811–1873_', 'name_en',
                      '_Henry William Adalbert_'),
                     ('http___dbpedia_org_resource_Prince_Adalbert_of_Prussia__1811–1873_', 'birth', '1811_10_29'),
                     ('http___dbpedia_org_resource_Prince_Adalbert_of_Prussia__1811–1873_', 'death', '1873_06_06')],
                    [('http___dbpedia_org_resource_Prince_Adalbert_of_Prussia__1811–1873_', 'name_en',
                      '_Henry William Adalbert_'),
                     ('http___dbpedia_org_resource_Prince_Adalbert_of_Prussia__1811–1873_', 'birth', '1811_10_29'),
                     ('http___dbpedia_org_resource_Prince_Adalbert_of_Prussia__1811–1873_', 'death', '1873_6_6')],
                    [('http___dbpedia_org_resource_Abraham_Mendelssohn_Bartholdy', 'name_en',
                      'Abraham Mendelssohn Bartholdy'),
                     ('http___dbpedia_org_resource_Abraham_Mendelssohn_Bartholdy', 'birth', '1776_12_10'),
                     ('http___dbpedia_org_resource_Abraham_Mendelssohn_Bartholdy', 'death', '1835_11_19')],
                    [('http___dbpedia_org_resource_Ludwig_Achim_von_Arnim', 'name_en', 'Achim von Arnim'),
                     ('http___dbpedia_org_resource_Ludwig_Achim_von_Arnim', 'birth', '1781_01_26'),
                     ('http___dbpedia_org_resource_Ludwig_Achim_von_Arnim', 'death', '1831_1_21')],
                    [('http___dbpedia_org_resource_Prince_Adalbert_of_Prussia__1811–1873_', 'name_en',
                      'Adalbert of Prussia'),
                     ('http___dbpedia_org_resource_Prince_Adalbert_of_Prussia__1811–1873_', 'birth', '1811_10_29'),
                     ('http___dbpedia_org_resource_Prince_Adalbert_of_Prussia__1811–1873_', 'death', '1873_06_06')],
                    [('http___dbpedia_org_resource_Prince_Adalbert_of_Prussia__1811–1873_', 'name_en',
                      'Adalbert of Prussia'),
                     ('http___dbpedia_org_resource_Prince_Adalbert_of_Prussia__1811–1873_', 'birth', '1811_10_29'),
                     ('http___dbpedia_org_resource_Prince_Adalbert_of_Prussia__1811–1873_', 'death', '1873_6_6')],
                    [('http___dbpedia_org_resource_Adam_Müller', 'name_en', 'Adam Müller'),
                     ('http___dbpedia_org_resource_Adam_Müller', 'birth', '1779_06_30'),
                     ('http___dbpedia_org_resource_Adam_Müller', 'death', '1829_01_17')],
                    [('http___dbpedia_org_resource_Adam_Müller', 'name_en', 'Adam Müller'),
                     ('http___dbpedia_org_resource_Adam_Müller', 'birth', '1779_06_30'),
                     ('http___dbpedia_org_resource_Adam_Müller', 'death', '1829_1_17')],
                    [('http___dbpedia_org_resource_Adolf_Brand', 'name_en', 'Adolf Brand'),
                     ('http___dbpedia_org_resource_Adolf_Brand', 'birth', '1874_11_14'),
                     ('http___dbpedia_org_resource_Adolf_Brand', 'death', '1945_2_2')],
                    [('http___dbpedia_org_resource_Adolf_Christen', 'name_en', 'Adolf Christen'),
                     ('http___dbpedia_org_resource_Adolf_Christen', 'birth', '1811_08_07'),
                     ('http___dbpedia_org_resource_Adolf_Christen', 'death', '1883_07_13')],
                    [('http___dbpedia_org_resource_Adolf_Christen', 'name_en', 'Adolf Christen'),
                     ('http___dbpedia_org_resource_Adolf_Christen', 'birth', '1811_08_07'),
                     ('http___dbpedia_org_resource_Adolf_Christen', 'death', '1883_7_13')],
                    [('http___dbpedia_org_resource_Adolf_Damaschke', 'name_en', 'Adolf Damaschke'),
                     ('http___dbpedia_org_resource_Adolf_Damaschke', 'birth', '1865_11_24'),
                     ('http___dbpedia_org_resource_Adolf_Damaschke', 'death', '1935_7_30')],
                    [('http___dbpedia_org_resource_Adolf_Erman', 'name_en', 'Adolf Erman'),
                     ('http___dbpedia_org_resource_Adolf_Erman', 'birth', '1854_10_31'),
                     ('http___dbpedia_org_resource_Adolf_Erman', 'death', '1937_6_26')],
                    [('http___dbpedia_org_resource_Adolf_Gärtner', 'name_en', 'Adolf Gärtner'),
                     ('http___dbpedia_org_resource_Adolf_Gärtner', 'birth', '1879_03_24'),
                     ('http___dbpedia_org_resource_Adolf_Gärtner', 'death', '1958_01_09')],
                    [('http___dbpedia_org_resource_Adolf_Gärtner', 'name_en', 'Adolf Gärtner'),
                     ('http___dbpedia_org_resource_Adolf_Gärtner', 'birth', '1879_03_24'),
                     ('http___dbpedia_org_resource_Adolf_Gärtner', 'death', '1958_1_9')],
                    [(
                        'http___dbpedia_org_resource_Adolf_Heinrich_von_Arnim_Boitzenburg',
                        'name_en',
                        'Adolf Heinrich von Arnim_Boitzenburg'),
                        (
                            'http___dbpedia_org_resource_Adolf_Heinrich_von_Arnim_Boitzenburg',
                            'birth', '1803_04_10'), (
                        'http___dbpedia_org_resource_Adolf_Heinrich_von_Arnim_Boitzenburg',
                        'death', '1868_01_08')],
                    [('http___dbpedia_org_resource_Adolf_Heinrich_von_Arnim_Boitzenburg',
                      'name_en',
                      'Adolf Heinrich von Arnim_Boitzenburg'),
                     ('http___dbpedia_org_resource_Adolf_Heinrich_von_Arnim_Boitzenburg',
                         'birth',
                         '1803_04_10'),
                     ('http___dbpedia_org_resource_Adolf_Heinrich_von_Arnim_Boitzenburg',
                         'death',
                         '1868_1_8')]]
        result = test.run_query().get_data()
        self.assertEquals(result, expected)


if __name__ == '__main__':
    unittest.main()
