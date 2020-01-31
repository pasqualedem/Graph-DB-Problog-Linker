# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 15:23:26 2020

@author: PasqualeDeMarinis
"""

from problog.logic import Constant, Var, Term
from problog.program import PrologString
from problog.engine import DefaultEngine
from problog import get_evaluatable

p = """
movie(X) :- moviedirectedbydirector(X,_).
movie(X) :- moviestaractor(X,_).
movie(X) :- movie_base(X).
moviedirectedbydirector(X,Y) :- directordirectedmovie(Y,X).
moviestaractor(X,Y) :- actorstarredinmovie(Y,X).
directordirectedmovie(X,Y) :- directordirectedmovie_base(X,Y).
actorstarredinmovie(X,Y) :- actorstarredinmovie_base(X,Y).

book(X) :- bookwriter(X,_).
book(X) :- book_base(X).
bookwriter(X,Y) :- bookwriter_base(X,Y).

0.9375::directordirectedmovie_base(ronhoward,abeautifulmind).
0.9959243650858862::movie_base(abeautifulmind).
0.9999990106516323::book_base(abeautifulmind).

0.9277725683823577::movie_base(casinoroyale).
0.9375::directordirectedmovie_base(martincampbell,casinoroyale).
0.99951171875::actorstarredinmovie_base(danielcraig,casinoroyale).
0.999996125::bookwriter_base(casinoroyale,ianfleming).
0.999998138106335::book_base(casinoroyale).

0.9375::actorstarredinmovie_base(dannyboyle,trainspotting).
0.9375::directordirectedmovie_base(dannyboyle,trainspotting).
0.9999995231628418::book_base(trainspotting).

0.9375::bookwriter_base(sleepyhollow,washingtonirving).
0.96875::actorstarredinmovie_base(christopherwalken,sleepyhollow).

0.9763532157207491::movie_base(theadventuresofrobinhood).
0.9999999999422124::bookwriter_base(theadventuresofrobinhood,howardpyle).

moviebook(X) :- movie(X), book(X).
query(moviebook(_)).
"""
r = get_evaluatable().create_from(p).evaluate()

print(r)