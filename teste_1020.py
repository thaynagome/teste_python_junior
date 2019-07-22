#!/usr/bin/env python 
# -- coding: utf-8 --

#Solicita inserção de dias de idade do usuario
dias = int(input("Digite sua idade em dias: "))

#Divide dias por 365 e no resultado obtém apenas a parte inteira da divisão
anos = dias // 365

# Obtem o resto da operação e divide por 30 com objetivo de obter a parte inteira
meses = (dias % 365) // 30

    #Esta parte obterá o resto da operaçao, depois resolverá a operação em 
    #parenteses que irá obter o resto da operação indicada, dividir por 30
    #obtendo sua parte inteira, e depois e obter esse resultado irá multiplicar
    #por 30, que por fim, resolverá os parenteses da direita e subtrairá da
    #primeira operação
dias = (dias % 365) - (((dias % 365)//30) * 30)


print (anos ,"ano(s)")
print (meses ,"mes(es)")
print (dias ,"dia(s)")



