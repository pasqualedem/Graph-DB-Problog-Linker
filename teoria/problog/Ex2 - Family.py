# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 13:26:30 2020

@author: PasqualeDeMarinis
"""
from problog.logic import Constant, Var, Term
from problog.program import PrologString
from problog.engine import DefaultEngine
from problog import get_evaluatable



p = PrologString("""
% Some simple test Prolog programs
% --------------------------------

% Knowledge bases

male(giuseppe).
male(giacomo).
male(nonno).
male(bisnonno).
male(pino).

female(maria).
female(giovanna).
female(francesca).

married(pino,francesca).
married(giuseppe,maria).

parent(francesca,giovanna).
parent(pino,giovanna).


parent(giuseppe,giacomo).
parent(maria,giacomo).
parent(giuseppe,marco).
parent(maria,marco).

parent(nonno,giuseppe).
parent(nonno,francesca).

parent(bisnonno,nonno).

child(X,Y) :- parent(Y,X).

grandchild(Y,X) :- parent(X,Z), parent(Z,Y).

ancestor(X,Y) :- parent(X,Y).
ancestor(X,Y) :- ancestor(X,Z), parent(Z,Y).

sibling(X,Y) :- parent(Z,X),parent(Z,Y), not(X=Y).

cousin(X,Y) :- grandchild(X,Z), grandchild(Y,Z).

uncle(X,Y) :- sibling(X,Z),parent(Z,Y),male(X).
uncle(X,Y) :- married(X,Z),sibling(Z,P),parent(P,Y),male(X).
aunt(X,Y) :- sibling(X,Z),parent(Z,Y),female(X).
aunt(X,Y) :- married(X,Z),sibling(Z,P),parent(P,Y),female(X).

dad(X,Y) :- parent(X,Y), male(X).
mom(X,Y) :- parent(X,Y), female(X).

query(parent(X,giacomo)).
""")

engine = DefaultEngine()
db = engine.prepare(p)    # This compiles the Prolog model into an internal format.
                          # This step is optional, but it might be worthwhile if you
                          #  want to query the same model multiple times.
query1 = Term('parent', [Var('X'), Constant('giacomo')])
results = engine.query(db, query1)

r = get_evaluatable().create_from(p).evaluate()

print(results)
print(r)