# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 19:19:46 2024

@author: lpren
"""

import numpy as np

B=np.array([1,9,5,0,20,-4,12,16,7])
objetivo = 12

def app(arreglo, objetivo):
    
    n=arreglo.size
    parejas=[]
    b=[]
    for i in range(0,n-1):
        for j in range(i+1,n):
            # print(i,j)
            if arreglo[i]+arreglo[j] == objetivo:
                
                b.append(arreglo[i])
                b.append(arreglo[j])
                
                parejas.append(b)
        b=[]
    return parejas

print(app(B,objetivo))