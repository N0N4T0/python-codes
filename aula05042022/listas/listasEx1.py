# Exibindo valores da lista  com for
comidas = ['Cebola', 'Tomate', 'Cenoura', 'Ovo', 'Queijo']

print("indice - elemento")
for indice, elemento in enumerate(comidas):
	print (f"{indice:<10}{elemento}")
