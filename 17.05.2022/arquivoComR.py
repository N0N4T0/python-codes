# AO executar esse comando um arquivo com o nome "teste.txt" será lido
arquivolido = open("teste.txt", "r")

# A função read() retorna todo o conteúdo do arquivo como uma string.
dados = arquivolido.read()

# Observação, se não tiver dado nenhum o print retornará vazio
print(dados)
print("O tipo de dado do arquivo é: {}".format(type(dados)))