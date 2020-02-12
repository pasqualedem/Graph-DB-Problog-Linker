# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:03:58 2020

@author: PasqualeDeMarinis
"""


from problog import get_evaluatable


model = """
% urnball_poisson.pl
:- use_module('posson.py').

num_balls(X) :-
    findall(N, between(1,3,N), L),
    poisson_probs(L, 2, Probs),
    select_weighted(0, Probs, L, X, _).

0.9::color(Ball, blue); 0.1::color(Ball, green).

draw_ball(D, C) :-
    num_balls(TBs),
    findall(Bs, between(1,TBs,Bs), L),
    select_uniform(D, L, B, _),
    color(B, C).

    query(num_balls(_)).
    evidence(draw_ball(0, green)).
    query(draw_ball(1, green)).
"""
rappr = get_evaluatable().create_from(model)
r = rappr.evaluate()
print(r)
