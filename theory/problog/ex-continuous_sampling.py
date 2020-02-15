# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 16:50:31 2020

@author: PasqualeDeMarinis
"""

from problog.tasks import sample
from problog.program import PrologString

from problog.program import SimpleProgram, PrologString, LogicProgram, PrologFile
from problog.logic import Constant, Var, Term, AnnotatedDisjunction

import random
import math

# Define a function that generates a sample.
def integer_uniform(a, b):
    return math.floor(random.uniform(a, b))

modeltext = """
    my_uniform(0,10)::a.
    0.5::b.
    c :- value(a, A), A >= 3; b.
    query(a).
    query(b).
    query(c).
"""

modeltext_new = """
    0.5::b.
    c :- value(a, A), A >= 3; b.
    query(a).
    query(b).
    query(c).
"""



s = SimpleProgram()
unif = Term('my_uniform')(Constant(0),Constant(10))
a = Term('a', p=unif)
s += a
for clause in PrologString(modeltext_new):
    s += clause

model = PrologString(modeltext)
# Pass the mapping between name and function using the distributions parameter.
x = list(PrologString(modeltext).__iter__())
x2 = list(s.__iter__())
result = list(sample.sample(model, n=3, format='dict', distributions={'my_uniform': integer_uniform}))
result2 = list(sample.sample(s, n=3, format='dict', distributions={'my_uniform': integer_uniform}))