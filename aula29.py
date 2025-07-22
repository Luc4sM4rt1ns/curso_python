"""
Introdução ao try/except
try - tentar executar o código
execpt - ocorreu algum erro ao executar
"""
# print(1234)
# print(456)
# int('a')

numero = input('Vou dobrar o número que você digitar: ')

# Fast Fail
try:
    numero_float = float(numero)
    print(f'O dobro de {numero_float} é {numero_float * 2:.2f}')
except:
    print(f'Isso não é um número')