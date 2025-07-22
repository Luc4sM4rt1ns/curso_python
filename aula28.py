"""
Exercício
Peça ao usuário que digite o seu nome
Peça ao usuário que digite a sua idade
Se nome e idade foram digitdos:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    Exiba "Desculpa, você deixou campos vazios."
"""

nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invervido é {nome[::-1]}')

    if ' ' in nome:
        print(f'Seu nome contém espaço')
    else:
        print(f'Seu nome não contém espaço')
        
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[- 1]}')
else:
    print('Desculpa, você deixou campos vazios.')