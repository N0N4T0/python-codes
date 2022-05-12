# salva no copiateste.txt o mesmo conteudo do teste.txt

with open('teste.txt', 'r') as arquivolido:
    with open('copiateste.txt', 'w') as arquivocriado:
        for linha in arquivolido:
            arquivocriado.write(linha)
