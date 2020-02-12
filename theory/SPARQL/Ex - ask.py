# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 13:05:42 2020

@author: PasqualeDeMarinis
"""



from SPARQLWrapper import SPARQLWrapper, XML

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("""
    ASK WHERE { 
        <http://dbpedia.org/resource/Asturias> rdfs:label "Asturias"@es
    }    
""")

sparql.setReturnFormat(XML)
results = sparql.query().convert()
print(results.toxml())