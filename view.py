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
    ticker = sys.argv[1]
    ticker = ticker.capitalize()
    p1 = sys.argv[2]
    p2 = sys.argv[3]
    p3 = sys.argv[4]
    p4 = sys.argv[5]
    cols = []
    if p1:
        cols.append('close')
    if p2:
        cols.append('adj_close')   
    if p3:
        cols.append('open')
    if p4:
        cols.append('adj_open')
    return ticker, cols

def present_output(ticker, cols):
    """Write results to terminal window."""
    s = compute.compute(ticker, cols)
    print 'Generated Graph for %: %' % (ticker, s)
