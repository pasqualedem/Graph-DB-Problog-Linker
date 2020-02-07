from py2neo import Graph
#pip install py2neo

graph = Graph(password="test")
#Neo4j in esecuzione su cui è creato un grafo vuoto (in esecuzione, cliccare start) avente password test

graph.run("MATCH(n) DETACH DELETE n") #Cancello tutti i nodi in caso il grafo non è vuoto

graph.run("CREATE (p:Person {name: 'Giuseppe', age:19})")
graph.run("CREATE CONSTRAINT on (p:Person) ASSERT p.name IS UNIQUE")

graph.run("CREATE (p:Person {name: 'Pasquale', age:17})")
graph.run("CREATE CONSTRAINT on (p:Person) ASSERT p.name IS UNIQUE")

graph.run("CREATE (p:Person {name: 'Sergio', age:18})")
graph.run("CREATE CONSTRAINT on (p:Person) ASSERT p.name IS UNIQUE")

graph.run("CREATE (p:Person {name: 'Roberto', age:15})")
graph.run("CREATE CONSTRAINT on (p:Person) ASSERT p.name IS UNIQUE")

graph.run("CREATE (p:Person {name: 'Luigi', age:11})")
graph.run("CREATE CONSTRAINT on (p:Person) ASSERT p.name IS UNIQUE")

graph.run("MATCH (p:Person {name: 'Luigi'}), (q:Person {name: 'Roberto'}) CREATE (p)-[:KNOWS]->(q)")
graph.run("MATCH (p:Person {name: 'Sergio'}), (q:Person {name: 'Pasquale'}) CREATE (p)-[:KNOWS]->(q)")
graph.run("MATCH (p:Person {name: 'Pasquale'}), (q:Person {name: 'Giuseppe'})  CREATE (p)-[:KNOWS]->(q)")
graph.run("MATCH (p:Person {name: 'Giuseppe'}), (q:Person {name: 'Sergio'})  CREATE (p)-[:KNOWS]->(q)")
graph.run("MATCH (p:Person {name: 'Luigi'}), (q:Person {name: 'Giuseppe'})  CREATE (p)-[:KNOWS]->(q)")

graph.run("CREATE (:Person {name:'Matteo'})-[:KNOWS]->(:Person {name:'Francesco'})")

graph.run("CREATE (p:Car {brand: 'Ford', targa: '123'})")
graph.run("CREATE CONSTRAINT on (c:Car) ASSERT c.targa IS UNIQUE")

graph.run("CREATE (p:Car {brand: 'Seat', targa: '124'})")
graph.run("CREATE CONSTRAINT on (c:Car) ASSERT c.targa IS UNIQUE")

graph.run("CREATE (p:Car {brand: 'Suzuki', targa: '143'})")
graph.run("CREATE CONSTRAINT on (c:Car) ASSERT c.targa IS UNIQUE")

graph.run("CREATE (p:Car {brand: 'Fiat', targa: '125'})")
graph.run("CREATE CONSTRAINT on (c:Car) ASSERT c.targa IS UNIQUE")

graph.run("CREATE (p:Car {brand: 'Audi', targa: '127'})")
graph.run("CREATE CONSTRAINT on (c:Car) ASSERT c.targa IS UNIQUE")

graph.run("MATCH (p:Person {name: 'Luigi'}), (q:Car {targa: '123'}) CREATE (p)-[:OWNS]->(q)")
graph.run("MATCH (p:Person {name: 'Sergio'}), (q:Car {targa: '124'}) CREATE (p)-[:OWNS]->(q)")
graph.run("MATCH (p:Person {name: 'Pasquale'}), (q:Car {targa: '127'}) CREATE (p)-[:OWNS]->(q)")
graph.run("MATCH (p:Person {name: 'Giuseppe'}), (q:Car {targa: '143'}) CREATE (p)-[:OWNS]->(q)")
graph.run("MATCH (p:Person {name: 'Roberto'}), (q:Car {targa: '125'}) CREATE (p)-[:OWNS]->(q)")

result = graph.run("MATCH (b:Person {name: 'Luigi'})-[:KNOWS]->(a:Person)-[:OWNS]->(c:Car)) RETURN a.name, a.age")

while result.forward():
    print(result.current)