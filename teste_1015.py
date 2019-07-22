import math

x1,y1 = input("Digite os valores de x1 e y1: ").split(" ")


# Converte o valor para os tipos necessários 
x1 = float(x1)
y1 = float(y1)

x2,y2 = input("Digite os valores de x2 e y2: ").split(" ")

# Converte o valor para os tipos necessários 
x2 = float(x2)
y2 = float(y2)

dist =  math.sqrt(((x2-x1)**2)+((y2-y1)**2))

print ("Sua distância é de ", "%.2f" %dist)

