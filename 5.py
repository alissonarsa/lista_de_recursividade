bitcoin2024 = { # fonte: https://br.investing.com/crypto/bitcoin/btc-brl-historical-data (usado filto de valor mensal)
    "1": 212335,
    "2": 306600,
    "3": 359693,
    "4": 316571,
    "5": 355299,
    "6": 352600,
    "7": 368540,
    "8": 333842,
    "9": 345411,
    "10": 409131,
    "11": 580819,
    "12": 583265
}

def investir_em_bitcoin(valor_mensal, saldo_biticoin=0, meses=0, investido=0):
    meses_lista = list(bitcoin2024.keys())

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

    if saldo >= 20000 and saldo - valor_em_dolar < 20000:
        print(f"Marco de $20,000.00 atingido em {meses // 12} anos e {meses % 12} meses.")
        print(f"Valor investido até o marco: ${investido:.2f}")
        print(f"Juros compostos até o marco: ${juros:.2f}")

    return deposita_na_poupança_converte_em_dolar_mensal(valormensal, saldo, meses + 1, investido, juros)

# chamando a função

valor_mensal = 500
anos, meses_restantes, investido, juros, saldo_final = deposita_na_poupança_converte_em_dolar_mensal(valor_mensal)

# professor, a recursividade é limitada :( para atingir os saldos desejados