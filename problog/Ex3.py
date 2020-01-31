# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 13:51:45 2020

@author: PasqualeDeMarinis
"""

from problog.engine import DefaultEngine
from problog.logic import Term


m1 = """
0.3::a(1).
query(a(X)).
"""
db = DefaultEngine().prepare(PrologString(m1))
print("FIRST RESULT")
print (get_evaluatable().create_from(db).evaluate())

m2 = """
0.4::a(2).
"""

#ADDING CLAUSES

print("SECOND RESULT")
for statement in PrologString(m2):
    db += statement

print (get_evaluatable().create_from(db).evaluate())