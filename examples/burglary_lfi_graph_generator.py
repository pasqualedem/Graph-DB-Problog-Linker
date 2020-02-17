from random import random

from py2neo import Graph

graph = Graph(password="burglary")
sides = ["head", "cross"]

for i in range(0, 100):
    print(i)
    burglary = random() < 0.1
    fire = random() < 0.1
    alarm = False
    smoke = False
    if burglary or fire:
        alarm = True
    if fire:
        smoke = True

    query = "CREATE (:Night {burglary:" + str(burglary) +", fire:" + str(fire) + ", alarm:" + str(alarm) + ", smoke:" + str(smoke) + "}) "
    graph.run(query)