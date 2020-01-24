# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 12:22:13 2020

@author: CEC
"""

def fib(n):
    a, b = 0,1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
