dolar2024 = { # fonte: https://idealsoftwares.com.br/indices/dolar2024.html
    "1": 4.89,
    "2": 4.93,
    "3": 4.95,
    "4": 5.05,
    "5": 5.11,
    "6": 5.23,
    "7": 5.58,
    "8": 5.66,
    "9": 5.62,
    "10": 5.45,
    "11": 5.80,
    "12": 6.06
}

def deposita_na_poupança_converte_em_dolar_mensal(valormensal, saldo=0, meses=0, investido=0, juros=0):
    meses_lista = list(dolar2024.keys())

    anos = meses // 12
    meses_restantes = meses % 12
    
    # receber rendimento na conta
    
    mes_atual = meses_lista[meses % 12]
    taxa_cambio = dolar2024[mes_atual]
    valor_em_dolar = valormensal / taxa_cambio
    saldo += valor_em_dolar
    investido += valormensal

    # depositar na conta

    return saldo