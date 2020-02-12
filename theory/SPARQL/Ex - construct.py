# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 13:06:39 2020

@author: PasqualeDeMarinis
"""

from SPARQLWrapper import SPARQLWrapper, XML, N3
from rdflib import Graph

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("""
    PREFIX dbo: <http://dbpedia.org/ontology/>
    PREFIX schema: <http://schema.org/>
    CONSTRUCT {
      ?lang a schema:Language ;
      schema:alternateName ?iso6391Code . 
    }
    WHERE {
      ?lang a dbo:Language ;
      dbo:iso6391Code ?iso6391Code .
      FILTER (STRLEN(?iso6391Code)=2) # to filter out non-valid values
    }
""")

sparql.setReturnFormat(XML)
results = sparql.query().convert()
print(results.serialize(format='xml'))