def funcaoRecursiva(numero):
    if(numero != 1):
        funcaoRecursiva(numero - 1)
    print(numero)

print("Testando a função recursiva")
funcaoRecursiva(10)