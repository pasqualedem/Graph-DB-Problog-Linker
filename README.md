Graph DB - Problog Linker (GDBPL)

## Presentation

GDBPL is a software that links a Graph DB like Neo4j to [Problog](https://github.com/ML-KULeuven/problog) and [ProbFOIL](https://bitbucket.org/problog/prob2foil/src/master/).

GDBPL fetch data from the DB and parse it to a format undearstandable from Problog and ProbFOIL,
running multiple queries it can build a logic program and integrating from files it is possible 
to execute the functions of Problog like 
- reasoning;
- LFI (learning from interpretations) for learning probabilities;
- sampling;
- Structure Learning with ProbFOIL.

GDBPL can also calculate the distribution of the data and convert it to logic clauses.
