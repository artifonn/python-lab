def cartao_identificacao(nome, cargo, departamento):
    return (
        f'===== CARTÃO DE IDENTIFICAÇÃO =====\n'
        f'Nome: {nome}\n'
        f'Cargo: {cargo}\n'
        f'Departamento: {departamento}\n'
        f'==================================='
    )

nome = input('Informe o nome do funcionário: ')
cargo = input('Informe o cargo: ')
departamento = input('Informe o departamento: ')

cartao = cartao_identificacao(nome, cargo, departamento)

print(cartao)