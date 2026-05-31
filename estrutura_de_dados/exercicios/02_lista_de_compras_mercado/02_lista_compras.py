numero = int(input('Informe a quantidade de itens que deseja adicionar à sua lista: '))

lista = []
contador = 1

while contador <= numero:
    item = input('Informe o item que deseja adicionar à sua lista: ')
    lista.append(item)
    contador += 1

print('\nItens da lista:')

for item in lista:
    print(item)