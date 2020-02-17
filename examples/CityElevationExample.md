# Calcolo delle distribuzione dell'elevazione delle città e campionamento

In questo esempio, tramite endpoint sparql, è stata eseguita la seguente query:

PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbr: <http://dbpedia.org/resource/>

SELECT ?subject, ?elevation 
WHERE {
?subject a dbo:City .
?subject dbo:elevation ?elevation
}

Il risultato di tale query è:

![] (./img/sparql_query_result)
