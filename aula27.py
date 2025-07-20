"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::] [início:fim:pular]
Obs.: a função len rerorna a quantidade de caracteres da str
Índices começam a ser contados a partir do 0, caracteres a partir do 1
Para fazer inversão do texto, pode ser usado [::-1] Ex. odnum álO
Para travar com o texto invertido, as numerações precisam ser negativas
"""

var = 'Olá mundo'
#print(var[4:8]) #Índice final não é incluso, ou seja, o valor final precisa ter acréscimo +1
# print(len(var))
#print(var[0:len(var):2]) #len(var) nesse caso é o 9, ou o final da string
print(var[::-1]) # odnum álO