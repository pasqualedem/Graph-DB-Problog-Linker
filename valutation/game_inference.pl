% MATCH (n:RollDice)<-[:GameStep]-(g:Game) MATCH (m:MoneyToss)<-[:GameStep]-(g:Game)  WHERE n:RollDice OR n:MoneyToss RETURN ID(g), n.number as number, m.side as side

win(game,true) :- number(game,N), N>3, side(game,head).

query(win(game,true)).