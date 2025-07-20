# Operadores lógicos
# and (e) or (ou) not (não)
# and - todas as condições precisam ser verdadeiras

# Se qualquer valor for considerado falso, a expresão inteira será avaliada naquele valor
# São considerados falsy 
# 0 0.0 '' False
# Também existe o tipo None, que é usado para representar um não valor

# entrada = input('[E]entrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if entrada == 'E' and senha_digitada == senha_permitida:
#     print('Entrar')

# elif entrada == 'S':
#     print('Sair')
    
# else:
#     print('Opção ou senha incorreta.')

# Avaliação de curto circuito
print(True and False and True) # False
print(bool(0)) # False
print(True and 0 and True) # 0