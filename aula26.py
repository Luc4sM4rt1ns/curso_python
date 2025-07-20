"""
Formatação básica de strings
s - strings
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
 > - Esquerda
 < - Direita
 ^ - Centro
 = - Força o número a aparecer antes dos zeros
 Sinal - + ou -
 Ex.: 0>-100,.1f
 Conversion flags - !r !s !a
"""
variavel = 'abc'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel:0^8}')
print(f'{2000.789426578456842:0=+10,.1f}')
print(f'O hexadecial de 1500 é {1500:08X}')
print(f'{variavel!r}')