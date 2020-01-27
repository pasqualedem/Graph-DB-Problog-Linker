A.A 19 - 20

1.	Nel contesto della parte sulla conoscenza (multi-)relazionale, problemi che coinvolgano ragionamento / predizione in presenza di incertezza relazionale
es. learning (ILP, PILP) anche con modelli grafici/reticolari, recommendation

2.	Task di reinforcement learning: Q-learning, SARS
es. in piccoli giochi

3.	Predizione su linked data: applicazioni del ML a dataset estratti dal LOD Cloud (annotati attraverso ontologie)
es. combinando strumenti di rappresentazione e ragionamento con algoritmi ML da librerie standard

4.	Realizzazione di un piccolo sistema di apprendimento [da esempi] di regole di classificazione rappresentate con clausole definite (ad es. atomo come coppia attributo:valore) su cui sia possibile poi fare ragionamento.
Realizzabile estendendo gli algoritmi implementati in Python ritrovabili tra le risorse online nel sito del libro di testo oppure con altri algoritmi di sequential covering
opzionale: con discretizzazione (classe-attributo) di attributi ordinali o numerici (e.g. basata su  information gain)

5.	Estensione (e valutazione) di algoritmi di classificazione lazy (instance-based) o di clustering applicabili a individui che occorrono in ontologie RDF/OWL
Implementati in Java (ad es. usando OWLAPI) o Python (con OWLReady2) sfruttando  diverse misure di distanza/similarità
es. norme di Minkowski con ponderazione, Mahalanobis
opzionale: previa fase di feature selection/extraction

A.A 18 - 19

6.	Usare tecniche di apprendimento automatico (selezionate da opportune librerie) per determinare le distribuzioni usate in modelli logico-probabilistici per il Web Semantico: test di inferenze che sfruttino il modello risultante

7.	Case based reasoning: system di supporto ad attività di help-desk tecnico
es. ispirandosi a specifici modelli reali come quelli di stackoverflow e simili

8.	Case based reasoning: sistema di ricerca per similarità su grafi di conoscenza che metta insieme ragionamento e apprendimento automatico

9.	Funzionalità simile a quella delle predictive emoji keyboard (lista di suggerimenti per l'inserimento) che produca un modello di predizione esplicito anche editabile
•	che possa trattare l'incertezza (ad es. per ordinare i suggerimenti)
•	che possa agganciare altre basi di conoscenza che ammettano interrogazione/ragionamento

10.	KBS che producono e consumano conoscenza nell'ambito del Web dei Dati o il Web delle Cose
In tale ambito si possono trovare molti problemi da approfondire che richiedono competenze sia sul ragionamento sia sull'induzione/apprendimento (anche sotto incertezza) e la nuvola dei linked data offre moltissimi dataset per sperimentare praticamente quanto realizzato:
•	induzione (da esempi) di nuovi concetti / scoperta di nuovi assiomi
•	(soft) clustering / conceptual clustering
•	applicazione di forme diverse di machine learning a linked data
•	data linking, link prediction
•	ontology matching / alignment

11.	Modifica di un sistema di apprendimento esistente (come DL-Foil o DL-Focl) implementando, in alternativa alla copertura sequenziale, la beam-search o il simulated annealing
