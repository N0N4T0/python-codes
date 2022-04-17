dadosCidade = {
    'nome': 'São Paulo',
    'estado': 'São Paulo',
    'area_km2': 1521,
    'populacao_milhoes': 12.18,
}

dadosCidade1 = dadosCidade.copy()
dadosCidade1['estado'] = 'Rio de Janeiro'

print("Dicionario dadosCidade \n {} \n".format(dadosCidade))
print("Dicionario dadosCidade1 \n {}".format(dadosCidade1))
