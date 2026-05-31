frutas = ["Maçã", "Banana", "Laranja", "Uva", "Manga"]

print('------ Imprime o primeiro item da lista (Maçã) ------')
print(frutas[0])
print('------ Imprime o quinto item da lista (Manga) ------')
print(frutas[4])
# Adiciona Abacaxi a lista
frutas.append('Abacaxi')

print('Imprime a lista de frutas')
for fruta in frutas:
  print(fruta)