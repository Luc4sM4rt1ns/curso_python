# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1
# nome = 'Lucas'
# # print(nome[2])
# # print(nome[-3])
# print('c' in nome) # Retorna True
# print('z' in nome) # Retorna False
# print(10 * '-')
# print('vio' not in nome) # Retorna True
# print('cas' not in nome) # Retorna False

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')