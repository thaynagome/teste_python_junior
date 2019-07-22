#!/usr/bin/env python 
# -- coding: utf-8 --

#Solicita que o usuario digite a velocidade do carro Y em KM
Y = int(input("Digite a velocidade do carro Y em Km: "))

#Loop que obriga o usuario a inserir um valor maior do que 0 para continuar a operação
while(Y <= 0):
        Y = int(input("Digite a velocidade do carro Y: "))
else:
        carroy = Y * 2

#Apresenta resultado
print (carroy,"minutos")

