def volumePiscina(prof, **infos):
    print(infos)
    vol = prof*infos['largura']*infos['comprimento']

    return vol
    
# {
#     'largura': 4,
#     'comprimento': 5
# }

# {
#     'largura': 4,
#     'comprimento': 5, 
#     'area': 12
# }

volume = volumePiscina(5, largura=4, comprimento=5, area=12)
print('o volume é: ', volume)
