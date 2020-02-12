# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 13:07:16 2020

@author: PasqualeDeMarinis
"""

from SPARQLWrapper import SPARQLWrapper, N3
from rdflib import Graph

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("""
    DESCRIBE <http://dbpedia.org/resource/Asturias>
""")

sparql.setReturnFormat(N3)
results = sparql.query().convert()
g = Graph()
g.parse(data=results, format="n3")
print(g.serialize(format='n3'))