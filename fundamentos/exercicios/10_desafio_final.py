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
maior_de_idade = True

print('---------- Dados Cadastrados ----------')
print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Altura: {altura}')
print(f'Cidade: {cidade}')

print('---------- Tipo de cada informação ----------')
print(type(nome))
print(type(idade))
print(type(altura))
print(type(cidade))

print('---------- Idade daqui a 10 anos ----------')
print(idade + 10)

print('---------- Maior de idade ----------')
print(idade >= 18 and maior_de_idade)