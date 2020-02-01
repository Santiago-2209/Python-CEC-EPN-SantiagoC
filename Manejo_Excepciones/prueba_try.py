# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 18:19:27 2020

@author: CEC
"""

try:
    x=int(input("Ingrese un numero: "))
    y=1/x
    print(y)
except ZeroDivisionError:
    print("No puede dividir para cero")
except ValueError:
    print("Debe ingresar un valor entero")
except:
    print("Algo salió mal")
    
print("The End")