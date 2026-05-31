# Crie um programa que:
  # Pergunte o nome do usuário.
  # Pergunte a idade.
  # Pergunte a altura.
  # Pergunte a cidade.
  # Exiba todas as informações.
  # Mostre o tipo de cada informação.
  # Calcule a idade daqui a 10 anos.
  # Informe se a pessoa é maior de idade.

nome = input('Informe o seu nome: ')
idade = int(input('Informe a sua idade: '))
altura = float(input('Informe a sua altura: '))
cidade = input('Cidade: ')
estudante = True

print('---------- Dados Cadastrados ----------')
print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Altura: {altura}')
print(f'Cidade: {cidade}')

print('---------- Tipo de cada informação ----------')
print(f'Nome: {type(nome).__name__}')
print(f'Idade: {type(idade).__name__}')
print(f'Altura: {type(altura).__name__}')
print(f'Cidade: {type(cidade).__name__}')

print('---------- Idade daqui a 10 anos ----------')
print(idade + 10)

print('----------- É maior de idade? -----------')
if idade >= 18 :
  print(f'{nome}, é maior de idade.')
else :
  print(f'{nome}, você é menor de idade.')

print('---------- Pode participar do Programa ----------')
print(idade >= 18 and estudante)