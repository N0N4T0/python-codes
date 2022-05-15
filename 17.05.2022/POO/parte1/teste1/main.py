from pessoa import Pessoa

# Para criar um objeto a partir da minha classe(meu molde), eu tenho que instanciar
# esse objeto
# EU posso ter várias pessoas vindo de um mesmo molde

# Estamos criando um objeto a partir de uma classe
p1 = Pessoa()
p2 = Pessoa()

p1.falar()


# São únicos, p1 != p2
# Endereços de memória diferentes
print(p1)
print(p2)