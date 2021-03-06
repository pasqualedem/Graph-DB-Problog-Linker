# Calcolo probabilità di vittoria di un semplice gioco

Supponiamo di avere un database Neo4j contenente gli esiti di un semplice gioco:

si vince se tirando un dado si ottiene un numero maggiore di 3, e tirando una moneta si ottiene testa, altrimenti si perde.

Tale grafo Neo4j è modellato nel seguente modo:

![](./img/graph_structure.PNG)

Inseriamo la query: 

<b>MATCH (n:RollDice)<-[:GameStep]-(g:Game) MATCH (m:MoneyToss)<-[:GameStep]-(g:Game)  WHERE n:RollDice OR n:MoneyToss RETURN ID(g), n.number as number, m.side as side</b>

![](./img/game_inference_query.JPG)

la quale restituisce l'id del nodo della giocata il numero ottenuto dal dado, e il lato ottenuto dalla moneta.
Il parsing restituirà triple del tipo:

(idgiocata, number, valore) <br>
(idgiocata, side, valore)
...

![](./img/game_inference_query_results.JPG)

Queste possono essere trasformate in fatti logici nella forma prop(idgiocata, number, valore) oppure nella forma number(idgiocata, valore).

Passando al tab "Problog" inseriamo il soggetto relativo, il nome e il tipo di distribuzioni che vogliamo calcolare:

Il software è in grado di calcolare distribuzioni normali e multinomiali, il calcolo è effettutato tramite gli stimatori di massima verosimiglianza. <br>
Inoltre è possibile suddividere il dominio di una distribuzione normale in classi, in modo tale da discretizzare la distribuzione e renderla multinomiale.

![](./img/game_inference_distributions.JPG)

Eseguendo dovrebbe aver aggiunto le relative clausole Problog.

![](./img/game_inference_clauses.JPG)

A questo punto carichiamo il file game_inference.pl il quale contiene la clausola che descrive il funzionamento della vittoria e la clausola contenente la query.

### Inferenza

Nella parte sottostante clicchiamo "inference" e scegliamo dove vogliamo che il file risultante venga salvato.

![](./img/game_inference_execution.JPG)

Il risultato è *{win(game,true): 0.256536}*

### Campionamento

Cliccando invece su Sampling, decidendo il numero di campioni che si vogliono generare, possiamo produrli e scriverli su file.

*[{win(game,true): False}, {win(game,true): False}, {win(game,true): False}, {win(game,true): True}, {win(game,true): False}, {win(game,true): False}, {win(game,true): False}, {win(game,true): True}, {win(game,true): False}, {win(game,true): False}]*

