# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 19:19:46 2024

@author: larry Prentt
"""

import numpy as np

A=np.array([0,1,2,3,4,5,6,7,8,9,10,11,-1,12,13,20])
objetivo = 24

def app(arreglo, objetivo):
    
    n=arreglo.size
    parejas=[]
    b=[]
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                # print(i,j,k)
                if arreglo[i]+arreglo[j]+arreglo[k] == objetivo:
                    
                    b.append(arreglo[i])
                    b.append(arreglo[j])
                    b.append(arreglo[k])
                    
                    parejas.append(b)
            b=[]
    return parejas

print(app(A,objetivo))
trio = app(A,objetivo)