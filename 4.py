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

    if saldo >= 1000000 / 5: # ~200 mil dolar
        anos = meses // 12
        meses_restantes = meses % 12
        return anos, meses_restantes, investido, juros, saldo

    
    # receber rendimento na conta
    
    mes_atual = meses_lista[meses % 12]
    taxa_cambio = dolar2024[mes_atual]
    valor_em_dolar = valormensal / taxa_cambio
    saldo += valor_em_dolar
    investido += valormensal

    # calcular rendimento mensal
    
    if meses > 0:
        rendimento = saldo * 0.0005
        saldo += rendimento
        juros += rendimento

    # montande de 100 mil reais

    if saldo >= 200000 and saldo - valor_em_dolar < 200000:
        print(f"Marco de $20,000.00 atingido em {meses // 12} anos e {meses % 12} meses.")
        print(f"Valor investido até o marco: ${investido:.2f}")
        print(f"Juros compostos até o marco: ${juros:.2f}")
        print("")
        

    return deposita_na_poupança_converte_em_dolar_mensal(valormensal, saldo, meses + 1, investido, juros)

# chamando a função

valor_mensal = 500
anos, meses_restantes, investido, juros, saldo_final = deposita_na_poupança_converte_em_dolar_mensal(valor_mensal)

# professor, a recursividade é limitada :( para atingir os saldos desejados