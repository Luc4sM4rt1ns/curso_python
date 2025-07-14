nome = input('Digite o seu nome: ')
altura = float(input('Digite a sua altura: '))
peso = int(input('Digite o seu peso: '))
imc = peso / (altura * altura)

print(nome, 'tem', altura, 'de altura, pesa', peso, 'quilos e seu IMC é', imc)