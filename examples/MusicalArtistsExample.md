# Esempio inferenza con dati LOD

In questo esempio, tramite l'endpoint sparql https://dbpedia.org/sparql , è stata eseguita la seguente query:
```
PREFIX dbo: <http://dbpedia.org/ontology/>

SELECT ?subject, ?genre, REPLACE(str(?birthDate), "(\\d*)-.*", "$1") AS?birthDate
WHERE {
?subject a dbo:MusicalArtist .
?subject dbo:genre ?genre .
?subject dbo:birthDate ?birthDate .
}
LIMIT 100
```

Tale query, eseguita attraverso questo software viene convertita nella rappresentazione a triple

![](./img/musicians_triple.PNG)
