# Problema: 
        #  quero transformar meu nome em upper case
        #  sem modificar internamente meu método

# Mas por que usamos decorators?
# Segurança, identificar o que precisa naquele momento modificar ao método
# EU não mexo diretamente no método escrevendo dentro dele

# Definindo um decorator
# Uma função que tem como parâmetro receber outra função
def uppercase(funcao):
    def wrapper(*args):
        funcao(args[0].upper())
    return wrapper


# Teste sem decorator
def nome(nome):
    print("Nome: {}".format(nome))

nome("Lucas")

# Teste com decorator
@uppercase
def nome1(nome):
    print("Nome: {}".format(nome))

nome1("Lucas")

# Teste problemática
def nome2(nome):
    print("Nome: {}".format(nome.upper()))

nome2("João")