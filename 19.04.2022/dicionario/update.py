dadosCidade = {
    'nome': 'São Paulo',
    'estado': 'São Paulo',
    'area_km2': 1521,
    'populacao_milhoes': 12.18,
}

novosDados = {
    'populacao_milhoes': 15,
    'fundacao': '25/01/1554'
}

dadosCidade.update(novosDados)

print("Dicionario dadosCidade \n {}".format(dadosCidade))