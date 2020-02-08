from src.CloudQuery import CloudQuery


class Test:
    def __init__(self):
        self.query = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX dbp: <http://dbpedia.org/property/>" \
                     " SELECT ?cheese ?label WHERE {  ?cheese a <http://dbpedia.org/ontology/Cheese> " \
                     " dbp:region <http://dbpedia.org/resource/Asturias> ;          rdfs:label ?label .}"
        self.dataset = "http://dbpedia.org/sparql"
        self.t = CloudQuery(self.query, self.dataset)
        print(self.t.get_query())
        print(self.t.get_dataset())

    def run(self):
        data = self.t.run_query()
        print(data.get_triples())


test = Test()
test.run()

