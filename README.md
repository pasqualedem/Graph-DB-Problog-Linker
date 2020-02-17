Graph DB - Problog Linker (GDBPL)

## Presentazione

GDBPL è un software che collega database grafici come Neo4j a [Problog](https://github.com/ML-KULeuven/problog) e [ProbFOIL](https://bitbucket.org/problog/prob2foil/src/master/).

GDBPL ricava dati da un database grafico e li trasforma in un formato comprensibile da Problog e ProbFOIL,
eseguendo interrogazioni multiple può costritire un programma logico anche annotato da probabilità e integrando da altre sorgenti come file è possibile:
eseguire funzioni di Problog come:
- ragionamento;
- LFI (learning from interpretations) per imparare probabilità;
- campionamento;
- apprendimento della struttura con ProbFOIL.

GDBPL può anche calcolare le distribuzioni contenute nei dati e trasformarle in clausole logiche.
