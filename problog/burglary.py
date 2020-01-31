# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 10:53:06 2020

@author: PasqualeDeMarinis
"""

from problog.logic import Term
from problog.program import PrologString
from problog.learning import lfi

model = """
t(0.5)::burglary.
0.2::earthquake.
t(_)::p_alarm1.
t(_)::p_alarm2.
t(_)::p_alarm3.

alarm :- burglary, earthquake, p_alarm1.
alarm :- burglary, \+earthquake, p_alarm2.
alarm :- \+burglary, earthquake, p_alarm3.
"""

alarm = Term('alarm')
burglary = Term('burglary')
earthquake = Term('earthquake')

examples = [
    [(burglary, False), (alarm, False)],
    [(earthquake, False), (alarm, True), (burglary, True)],
    [(burglary, False)]
]

score, weights, atoms, iteration, lfi_problem = lfi.run_lfi(PrologString(model), examples)

print (lfi_problem.get_model())
