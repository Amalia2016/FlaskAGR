# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 22:33:32 2017

@author: Amalia
"""

import model, view

model.ticker = view.get_input()
view.present_output(model.ticker, model.Cols)
