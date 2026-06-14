def conversor_de_moedas(real, dolar) :
  total = real / dolar
  return total

real = float(input('Informe o valor em reais para conversão: '))
dolar = float(input('Informe a cotação atual do dolar: '))

resultado = conversor_de_moedas(real, dolar)


print('--------- Conversor de Moedas ---------')
print(f'Dólar atual: {dolar:.2f}')
print(f'Valor em reais: R${real:.2f}')
print(f'Valor convertido: US${resultado:.2f}')