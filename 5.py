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

def investir_em_bitcoin(valor_mensal, saldo_bitcoin=0, meses=0, investido=0, marco_100k=False, marco_1bitcoin=False):
    meses_lista = list(bitcoin2024.keys())

    saldo_reais = saldo_bitcoin * bitcoin2024[meses_lista[meses % 12]]
    
    #  1M de bitcoin em reais

    if saldo_reais >= 1000000:
        anos = meses // 12
        meses_restantes = meses % 12
        return anos, meses_restantes, investido, saldo_reais, saldo_bitcoin
    
    # adicionar valor mensal
    
    mes_atual = meses_lista[meses % 12]
    preco_btc = bitcoin2024[mes_atual]
    valor_em_bitcoin = valor_mensal / preco_btc
    saldo_bitcoin += valor_em_bitcoin
    investido += valor_mensal

    # verifica se tem 100 mil
    
    saldo_reais = saldo_bitcoin * bitcoin2024[mes_atual]
    if not marco_100k and saldo_reais >= 100000:
        marco_100k = True
        print(f"Montante de R$ 100.000,00 reais em bitcoin atingido em {meses // 12} anos e {meses % 12} meses.")
        print(f"Valor investido até o montante: R$ {investido:.2f}")
    
    # 1 Bitcoin

    if not marco_1bitcoin and saldo_bitcoin >= 1:
        marco_1bitcoin = True
        print(f"Marco de 1 Bitcoin atingido em {meses // 12} anos e {meses % 12} meses.")
        print(f"Valor investido até o montante: R$ {investido:.2f}")

    return investir_em_bitcoin(valor_mensal, saldo_bitcoin, meses + 1, investido, marco_100k, marco_1bitcoin)