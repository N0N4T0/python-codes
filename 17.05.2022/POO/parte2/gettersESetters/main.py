# Getter = obtem o valor
# Setter = configura o valor
# São proteções para o atributo

# Os setters são como e fossem filtros

class Produto:
    def __init__(self, nome, preco):
        # Atributos 
        self.nome = nome
        self.preco = preco
    
    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual/100))

    # Getter para nome
    @property
    def nome(self):
        return self._nome

    # Setter para nome
    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()

    # Getter para preco
    # chama o mesmo nome da variável lá do init, que ness caso é self.preco
    @property
    def preco(self):
        # por segurança mudamos o nome da variável pra evitar um loop
        # or convenção colocamos um _naFrenteDaVariável
        return self._preco

    # Setter para preço
    # valor refere a variável preco lá do init
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        
        self._preco = valor


         

p1 = Produto('CAMISETA', 'R$15')
p1.desconto(10)
print(p1.preco)

# Fluxo
# meu getter pede o self.preco lá do init
# ai ele retorna como self._preco
# então fica self._preco = preco
# então meu setter filtra o valor que vem do meu init, nesse caso preco
# preco entra como parâmetro no meu setter, sendo nomeado como valor
# após validação caso precise ele retorna para o meu self._preco meu novo valor
# só depois disso executa o processamento que precisa, nesse caso o cálculo de desconto