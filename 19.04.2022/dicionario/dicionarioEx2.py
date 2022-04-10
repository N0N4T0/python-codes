# Demosntração dicionário
dados_cidade = {
    'nome': 'São Paulo',
    'estado': 'São Paulo',
    'restaurantes' : {
        'boteco do Franca' : "Rua villa veede",
        'boteco do Americo' : "Rua Villa Amarela"
    },
    'area_km2': 1521,
    'populacao_milhoes': 12.18,
}

print(dados_cidade['restaurantes'])

print(type(dados_cidade['restaurantes']))
print(type(dados_cidade['restaurantes']['boteco do Franca']))
print(dados_cidade['restaurantes']['boteco do Franca'])
