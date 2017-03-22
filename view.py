# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 22:15:57 2017

@author: Amalia
"""

import sys
import compute

# Input: string ticker
# Output: a plot

def get_input():
    """Get input data from the command line."""
    ticker = str.capitalize(sys.argv[1])
    p1 = sys.argv[2]
    p2 = sys.argv[3]
    p3 = sys.argv[4]
    p4 = sys.argv[5]
    Cols = []
    if p1:
        Cols.append('Close')
    if p2:
        Cols.append('Adj_Close')   
    if p3:
        Cols.append('Open')
    if p4:
        Cols.append('Adj_Open')
    return ticker, Cols

def present_output(ticker, Cols):
    """Write results to terminal window."""
    s = compute.compute(ticker, Cols)
    print 'Generated Graph for %: %' % (ticker, s)
