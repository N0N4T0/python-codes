# for em dicionário

personInformation = {
    'nome':'Marcelo',
    'sexo': 'Masculino',
    'idade': 25,
    'peso': 68
}

for person in personInformation:
    print('{}: {}'.format(person, personInformation[person]))