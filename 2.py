def somar_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + somar_lista(lista[1:])

teste = [1, 2, 3, 4, 5]   
print(somar_lista(teste))