# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:11:31 2020

@author: PasqualeDeMarinis
"""
from scipy.stats import poisson
from problog.extern import problog_export

@problog_export('+list', '+int', '-list')
def poisson_probs(values, k):
    probs = poisson.pmf(values, k)
    total = sum(probs)
    # Translate np.float to Python native floats
    return [float(prob/total) for prob in probs]