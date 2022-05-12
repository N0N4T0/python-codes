# Programa que permite adicionar quantos dados queira em um arquivo txt
# O programa só finaliza caso usuário digite Yes quando solicitado
# No final exibe quais dados foram inseridos

final = "No"
arquivo = open("palavras.txt", "w")

while(final == "No"):
    entradaDeDados = input("Entrada: ")
    arquivo.write(str(entradaDeDados)+"\n")

    finalizar = input("\nFinalizar programa? \nAperte qualquer tecla para NAO \nOu escreva Yes para finalizar: \n")
    if(finalizar == 'Yes'):
        final = 'Yes'

print("Inserção de dados finalizada")
arquivo.close()

arquivo = open("palavras.txt", "r")
dados = arquivo.read()
print("Os seguintes dados estão no arquivo:\n{}".format(dados))