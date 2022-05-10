# Exemplo com unpacking
numeros = 1,2,3,5,7,11

a, b, c, d, e, f, g = numeros # "desempacota" a tupla numeros
print("O primeiro vale: {} e o ultimo vale: {}".format(a, g))