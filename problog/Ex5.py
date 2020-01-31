# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 13:58:16 2020

@author: PasqualeDeMarinis
"""

from problog.engine import DefaultEngine
from problog.logic import Term

# ADDING CLAUSES AS AN EXTENSION OF THE DATABASE

m1 = """
0.3::a(1).
query(a(X)).
"""
db = DefaultEngine().prepare(PrologString(m1))
print (get_evaluatable().create_from(db).evaluate())

m2 = """
0.4::a(2).
"""
db2 = db.extend()
for statement in PrologString(m2):
    db2 += statement

print (get_evaluatable().create_from(db2).evaluate())
print (get_evaluatable().create_from(db).evaluate())