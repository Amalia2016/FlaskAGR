# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 22:31:14 2017

@author: Felix
"""

#import matplotlib.pyplot as plt
#import simplejson as json
#import requests
import numpy as np
import quandl

import pandas as pd

#import io

from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file
from bokeh.resources import CDN, Resources, INLINE
from bokeh.embed import components, autoload_static
#from bokeh.util.browser import view
#from jinja2 import Template

def datetime(x):
    return np.array(x, dtype=np.datetime64)

def plot(ticker, cols, df):
    #pd.DataFrame(np.nan, index=[0], columns=['date', 'price'])
    price_colors = {'close': '#A6CEE3', 'adj_close': '#B2DF8A', 'open': '#33A02C', 'adj_open': '#FB9A99'}
    prices = ['close', 'adj_close', 'open', 'adj_open']
    p1 = figure(x_axis_type="datetime", title="Stock Closing Prices", tools='pan,wheel_zoom,box_zoom,reset,resize', toolbar_location="above", toolbar_sticky=False)
    p1.grid.grid_line_alpha=0.3
    p1.xaxis.axis_label = 'Date'
    p1.yaxis.axis_label = 'Price'
    
    for col in cols:
        if col in prices:
           df_line = df.filter(items = ['date']+[col])
           p1.line(datetime(df_line['date']), df_line[col], color=price_colors[col], legend=ticker.upper()+': '+col.capitalize())

    p1.legend.location = "top_left"
    
#    window_size = 60
#    window = np.ones(window_size)/float(window_size)
#    output_file("plot.html")
#    show(gridplot([[p1]], plot_width=400, plot_height=400))  # open a browser

    resources = INLINE

    js_resources = resources.render_js()
    css_resources = resources.render_css()
    
    script, div = components(p1)
    
    return js_resources, css_resources, script, div

def compute(ticker, cols):
    # https://www.quandl.com/api/v3/datasets/EOD/[ticker].json?api_key=byL6HFiAJCnKKXttWCW7&collapse=monthly&start_date=1990-01-01
    quandl.ApiConfig.api_key = 'byL6HFiAJCnKKXttWCW7'
    data = quandl.get_table('WIKI/PRICES', ticker = ticker)
    if data.empty:
        s = False
        return s,"","","",""
    else:
        s = True
        df = data.filter(items = ['date']+cols)
        js_resources, css_resources, script, div = plot(ticker, cols, df)
        return s, js_resources, css_resources, script, div
