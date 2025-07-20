# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condiçao verdadeira avalia toda a expressão como verdadeira

# Se qualquer valor for considerado verdadeiro, a expresão inteira será avaliada naquele valor
# São considerados falsy 
# 0 0.0 '' False
# Também existe o tipo None, que é usado para representar um não valor

# entrada = input('[E]entrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrar')

# elif entrada == 'S':
#     print('Sair')
    
# else:
#     print('Opção ou senha incorreta.')

# Avaliação de curto circuito
# print(True or False) # True
# print(bool(1)) # True
# print(0 or False or 0 or 'abc') # abc

senha = input('Senha: ') or 'Sem senha'
print(senha)