nome_funcionario = 'João Snow'

projetos = [
    'Sistema de Vendas',
    'Portal do Cliente',
    'API de Pagamentos'
]

data_admissao = (15, 3, 2025)

funcionario = {
    'nome': nome_funcionario,
    'idade': 33,
    'cargo': 'Desenvolvedor Júnior'
}

tecnologias = {
    'Python',
    'JavaScript',
    'React',
    'SQL',
    'Docker'
}

print('========== DADOS DO FUNCIONÁRIO ==========')

print(f'Nome: {nome_funcionario}')

print('\nProjetos:')
for projeto in projetos:
    print(f'- {projeto}')

print(
    f'\nData de admissão: '
    f'{data_admissao[0]:02d}/{data_admissao[1]:02d}/{data_admissao[2]}'
)

print('\nInformações do funcionário:')
for chave, valor in funcionario.items():
    print(f'{chave.capitalize()}: {valor}')

print('\nTecnologias conhecidas:')
for tecnologia in tecnologias:
    print(f'- {tecnologia}')