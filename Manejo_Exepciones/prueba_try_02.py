# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 18:30:53 2020

@author: CEC
"""

try:
    y=1/0
except ArithmeticError:
    print("Problema Aritmético")
except ZeroDivisionError:
    print("Division para cero")
