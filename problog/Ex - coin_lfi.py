# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 10:53:06 2020

@author: PasqualeDeMarinis
"""

from problog.logic import Term
from problog.program import PrologString
from problog.learning import lfi

model = PrologString("""
t(_)::l1.
t(_)::l2.
t(_)::l3.
t(_)::win.
win :- l1,l2,\+ l3.
""")

l1 = Term('l1')
l2 = Term('l2')
l3 = Term('l3')
win = Term('win')

examples = [
    [(l1, True), (l2, True), (l3, True), (win,False)],
    [(l1, True), (l2, True), (l3, False), (win,True)],
    [(l1, True), (l2, False), (l3, False), (win,False)],
    [(l1, True), (l2, True), (l3, False), (win,True)],
    [(l1, False), (l2, True), (l3, False), (win,False)]
]

score, weights, atoms, iteration, lfi_problem = lfi.run_lfi(model, examples)

print (lfi_problem.get_model())