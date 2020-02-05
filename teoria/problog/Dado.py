# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 13:59:28 2020

@author: PasqualeDeMarinis
"""

from problog import get_evaluatable

p = """
1/6::die(1); 1/6::die(2); 1/6::die(3);
1/6::die(4); 1/6::die(5); 1/6::die(6).

query(die(N)).
"""

r = get_evaluatable().create_from(p).evaluate()

print(r)