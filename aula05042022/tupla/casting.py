# Podemos gerar uma tupla a partir de uma lista...
lista1 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print("Tipo inicial de lista1 : {}".format(type(lista1)))
n1 = tuple(lista1)
print(n1, type(n1))

# ...ou uma lista a partir de uma tupla:
tupla2 = (1, 6, 1, 8)
print("Tipo inicial de tupla2 : {}".format(type(tupla2)))
n2 = list(tupla2)
print(n2, type(n2))