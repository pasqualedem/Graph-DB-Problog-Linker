# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 13:03:17 2020

@author: PasqualeDeMarinis
"""


from SPARQLWrapper import SPARQLWrapper, JSON,  N3
from rdflib import Graph


sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("""
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX : <http://dbpedia.org/resource/>

SELECT ?person ?name ?birth ?death WHERE { ?person dbo:birthPlace :Berlin . ?person dbo:birthDate ?birth . ?person foaf:name ?name . ?person dbo:deathDate ?death . FILTER (?birth < "1900-01-01"^^xsd:date) . } ORDER BY ?name
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    print(result["label"]["value"])
    
