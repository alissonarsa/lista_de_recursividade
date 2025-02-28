def inverter_string(argumento):
    if argumento == '':
        return ''
    else:
        return argumento[-1] + inverter_string(argumento[:-1])

teste = "alisson"

print(inverter_string(teste))