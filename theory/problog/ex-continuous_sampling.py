# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 16:50:31 2020

@author: PasqualeDeMarinis
"""

from problog.tasks import sample
from problog.program import PrologString

modeltext = """
    my_uniform(0,10)::a.
    0.5::b.
    c :- value(a, A), A >= 3; b.
    query(a).
    query(b).
    query(c).
"""

import random
import math

# Define a function that generates a sample.
def integer_uniform(a, b):
    return math.floor(random.uniform(a, b))

model = PrologString(modeltext)
# Pass the mapping between name and function using the distributions parameter.
result = list(sample.sample(model, n=3, format='dict', distributions={'my_uniform': integer_uniform}))