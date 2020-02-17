% MATCH (n:RollDice)<-[:GameStep]-(g:Game) MATCH (m:MoneyToss)<-[:GameStep]-(g:Game)  WHERE n:RollDice OR n:MoneyToss RETURN ID(g), n.number as number, m.side as side, g.win as win
mode(side(+,+)).
mode(number(+,+)).

base(side(game,headcross)).
base(number(game,num)).
base(win(game,boolean)).

learn(win/2).

example_mode(auto).
