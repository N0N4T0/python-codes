class Pessoa:
    
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade= idade
        self.comendo = comendo
        self.falando = falando

        variavel = 'Constutor foi iniciado'
        print(variavel)

    def outro_metodo(self):
        # Caso eu chame esse método lá no meu objeto irá da erro, 
        #visto que variável pertence a meu método init

        print(variavel)


    