# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 19:19:46 2024

@author: larry Prentt
"""

def app(arreglo, objetivo):
    
    n=len(arreglo)
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

n = int(input("Digite el tamaño de la lista "))
print("\n")
num_list = list(int(num) for num in input("Entre # enteros para la lista, separados por espacio ").strip().split())[:n]

print("Lista del Usuario: ", num_list)

objetivo =int(input("Entre el objetivo a encontrar "))

print(app(num_list,objetivo))