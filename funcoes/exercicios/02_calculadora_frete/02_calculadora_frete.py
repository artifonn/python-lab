def calcularValorFinal(valorProduto, valorFrete):
  return valorProduto + valorFrete


print('*********** Calculadora ***********\n')

valorProduto = float(input('Informe o valor do produto: '))
valorFrete = float(input('Informe o valor do frete: '))

valorFinal = calcularValorFinal(valorProduto, valorFrete)

print(f'O valor total do produto mais o frete é: R${valorFinal:.2f}')