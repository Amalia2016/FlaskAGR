# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 22:31:14 2017

@author: Felix
"""

import matplotlib.pyplot as plt
#import simplejson as json
#import requests
import quandl

def compute(ticker, Cols):
    tableused = "EOD/"+str.capitalize(ticker)
    # https://www.quandl.com/api/v3/datasets/EOD/[ticker].json?api_key=byL6HFiAJCnKKXttWCW7&collapse=monthly&start_date=1990-01-01
    quandl.ApiConfig.api_key = 'byL6HFiAJCnKKXttWCW7'
    data=quandl.get(tableused, authtoken="byL6HFiAJCnKKXttWCW7", collapse="monthly", start_date="1990-01-01")
    Cols = ['Open', 'Close']
    df = data.filter(items = Cols)
    s = df.mean()
    return s
