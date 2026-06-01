print('Exercicio Manipulação de Strigns')

i = 0

nomes = [
    "Ana",
    "Bruno",
    "Carlos",
    "Daniela",
    "Eduardo"
]

sobrenomes = [
  "Silva",
  "Garcia",
  "Magno",
  "Portela",
  "Pedrosa"
]

# while i < len(nomes):
#     print(f'Nome: {nomes[i]} {sobrenomes[i]}')
#     i += 1

for nome, sobrenome in zip(nomes, sobrenomes):
    print(f'Nome: {nome} {sobrenome}')