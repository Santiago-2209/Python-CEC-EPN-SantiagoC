# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 19:42:08 2020

@author: CEC
"""

import pandas as pd
titulos=pd.read_csv("data/titles.csv")
print(titulos.head(100))
print("\n"*2)
elenco=pd.read_csv("data/cast.csv", encoding="utf-8")
print(elenco.head(10))
print (len(titulos))
print(titulos.sort_values('year').head(20))
print(titulos[titulos.title=="Romeo and Juliet"].sort_values('year').head(1))
print(len( titulos[titulos.year == 1980] ))
print(len(elenco[elenco.title=="The Godfather"]))
c = elenco[elenco.title == "The Godfather"]
c = c[c.n.isnull()]
print(len( c ))
a=elenco[elenco.title=="The Godfather"]
a=a[a.n.notnull()]
print(len(a))
act=elenco[elenco.title=="2001: A Space Odyssey"].sort_values("n")
act=act[act.n.notnull()]
print(act)