# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 15:31:06 2020

@author: PasqualeDeMarinis
"""

from problog.tasks import sample
from problog.program import PrologString

modeltext = """
    0.3::a.
    0.5::b.
    c :- a; b.
    query(a).
    query(b).
    query(c).
"""

model = PrologString(modeltext)
result = sample.sample(model, n=3, format='dict')

print(result)