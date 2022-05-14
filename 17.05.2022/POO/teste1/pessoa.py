# Classe = molde

class Pessoa:
    # Método da classe
    # O parâmetro self faz referência a instância que está sendo chamado
    # No meu objeto quando eu escrevo p1.falar(), 
        # o argumento que está dentro do falar() na minha instância é o p1
        # é como se eu escrevesse p1.falar(p1)
    def falar(self):
        print('Pessoa está falando')