# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 10:49:37 2020

@author: PasqualeDeMarinis
"""

from problog.program import PrologString
from problog import get_evaluatable
from problog.program import PrologString
from problog import get_evaluatable

"""0.3::a.  query(a)."""

result = get_evaluatable().create_from(PrologString(model)).evaluate()