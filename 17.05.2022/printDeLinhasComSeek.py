file = open('novo.txt', 'w+')
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')

# A cada criação de uma linha o meu cursor vai para o final da linha,
# então na minha última linha criada o cursor ficou no final
# e quando eu pedi para ler ele me mostrou vazio
print('Lendo linhas:')
print(file.read())

# Com a função seek eu posso mover o cursor de volta para o inicio permitindo ler a linhas que escrevi
file.seek(0,0)
print('Lendo linhas depois de usado o seek:')
print(file.read())

file.close()