#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Author: Nicolas Muñoz Monreal

"""Se pide un número entre 0.0001 y 0.9999, de cuatro decimales como máximo.
Si no cumple las condiciones, se debe introducir otro número hasta que se cumplan (bucle while).
Input introducido por el usuario es float, valor decimal.
"""

x = 1

while float(x)<=0.0001 or float(x)>=0.9999 or float(x)*10000 != int(float(x)*10000):
    print("Por favor, introduzca un número entre 0 y 1 con un máximo de cuatro decimales")
    x=float(input());
    
    
"""Conversión del input decimal a un número entero para facilitar la división entera"""

num_   = x*10000
denom_ = 10000


""""Operaciones para encontrar la fracción irreducible: el numerador y el denominador de 
la fracción son ambos divisibles por el mismo número divisor <d>"""

d=2

while d<10000:
    while num_/d==int(num_/d) and denom_/d==int(denom_/d):
        num_=num_/d
        denom_=denom_/d
    d=d+1;

print("La fracción irreducible de su número es ", int(num_),"/", int(denom_));

