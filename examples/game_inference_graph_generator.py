from random import randrange

from py2neo import Graph

graph = Graph(password="test")
sides = ["head", "cross"]

for i in range(0, 1000):
    print(i)
    side_index = randrange(2)
    roll_dice_number = randrange(6) + 1

    if side_index == 0 and roll_dice_number > 3:
        query = "CREATE (:RollDice {number: " + str(roll_dice_number) + "})<-[:GameStep]-(:Game {win:True})-[:GameStep]->(:MoneyToss {side: \"" + sides[side_index] + "\"})"
    else:
        query = "CREATE (:RollDice {number: " + str(roll_dice_number) + "})<-[:GameStep]-(:Game {win:False})-[:GameStep]->(:MoneyToss {side: \"" + sides[side_index] + "\"})"

    graph.run(query)
