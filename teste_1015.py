#!/usr/bin/env python 
# -- coding: utf-8 --

#Importa a biblioteca para a raiz quadrada
import math 

#Solicitará em uma linha a inserção dos valores em uma linha
x1,y1 = input("Digite os valores de x1 e y1: ").split(" ")


# Converte os valor para flutuantes
x1 = float(x1)
y1 = float(y1)

#Solicitará em uma linha a inserção dos valores em uma linha
x2,y2 = input("Digite os valores de x2 e y2: ").split(" ")

# Converte os valor para flutuantes 
x2 = float(x2)
y2 = float(y2)

#Faz a conta necessária
dist =  math.sqrt(((x2-x1)**2)+((y2-y1)**2))

#Mostra para o usuário o resultado com duas casas decimais após a virgula
print ("%.4f" %dist)

