# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 18:34:42 2020

@author: CEC
"""

def badFun(n):
    try:
        return 1/n
    except ArithmeticError:
        print("Problema Aritmético")
    return None
badFun(0)