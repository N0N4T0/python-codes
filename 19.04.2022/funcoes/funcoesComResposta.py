def somatorio(lista):
    soma = 0
    for item in lista:
        soma = soma + item
    return soma

numeros = [1, 2, 3, 4, 5]
soma_dos_numeros = somatorio(numeros)
print("A soma dos elementos da lista vale: ", soma_dos_numeros)

if somatorio(numeros) > 50:
    print("Que soma grande!")
else:
    print("Que soma pequena!")