allowedAccess = ['Danilo', 'Lucio', 'Daiana', 'Vanessa']

requestName = input("Por gentileza informa seu nome para verificar nivel de permissão: ")

for name in allowedAccess:
    if(name == requestName):
        print("Acesso autorizado a " + requestName)
        break
    else:
        print("Acesso negado a " + requestName)
        break
