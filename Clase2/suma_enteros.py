# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 18:30:00 2024

@author: larry prentt
"""
import time
import pandas as pd
import matplotlib.pyplot as plt
import os

def suma_entero(n):
    return n*(n+1)//2

def suma_entero2(n):
    suma =0
    for i in range(1,n+1):
        suma += i
    return suma

n=10

print(suma_entero(n))
print(suma_entero2(n))


lista_numeros = [100, 1000, 10000, 100000, 1000000, 10000000, 100000000, int(1e+9) ]
 
tiempos = {'suma_entero':[], 'suma_entero2': []}
 
# Medir tiempos de ejecucion

for n in lista_numeros:

   inicio = time.perf_counter()
   suma_entero(n)
   fin = time.perf_counter()
   diferencia = fin - inicio
   tiempos['suma_entero'].append(diferencia)
 
   inicio = time.perf_counter()
   suma_entero2(n)
   fin = time.perf_counter()
   diferencia = fin - inicio
   tiempos['suma_entero2'].append(diferencia)
 
 
# Imprimir los tiempos

for i in tiempos:
   print(f"Tiempos de ejecucion de la ({i}):")
   for j, t in zip(lista_numeros, tiempos[i]):
      print(f"j = {j}: {t} segundos")
   print()
 
# Crear un dataframe
df = pd.DataFrame(tiempos, index=lista_numeros)
df.index.name = "n"
df.reset_index(inplace=True)
 
# Mostrar el dataframe
print(df)
 
# Generar una grafica
plt.plot(df['n'], df['suma_entero'], label="Suma constante", marker='o')
plt.plot(df['n'], df['suma_entero2'], label="Suma lineal", marker='x')
plt.xlabel("n (Numero de elementos)")
plt.ylabel("Tiempos de ejecucion (s)")
plt.title("Comparacion del Tiempo de Ejecicion: Suma Lineal vs Suma Constante")
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.grid(True)
plt.savefig('Sumatorias.png')