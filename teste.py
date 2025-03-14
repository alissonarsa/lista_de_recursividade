# Exemplo ações 2024
acoes2024 = {
    "acao1": {
        "nome": "Empresa A",
        "precos": [10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 15.5],
        "dividendos_mensais": 0.02  # 2% de dividendo
    },
    "acao2": {
        "nome": "Empresa B",
        "precos": [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
        "dividendos_mensais": 0.015  # 1.5% de dividendo
    },
    "acao3": {
        "nome": "Empresa C",
        "precos": [30, 31.5, 33, 34.5, 36, 37.5, 39, 40.5, 42, 43.5, 45, 46.5],
        "dividendos_mensais": 0.01  # 1% de dividendo
    }
}

def acoes(montante=0, meses=0, investido=0, dividendos=0, cotas=0, bateu_100k=None, bateu_1m=None, max_meses=240):
    investimento_mensal = 80

    while meses < max_meses:
        # Adiciona o valor mensal investido ao montante
        investido += investimento_mensal

        # Calcula os dividendos mensais
        dividendos_mensais = 0
        for acao in acoes2024.values():
            preco_atual = acao["precos"][meses % 12]
            cotas += investimento_mensal / preco_atual
            dividendos_mensais += cotas * preco_atual * acao["dividendos_mensais"]
        
        dividendos += dividendos_mensais

        # Calcula o montante total
        montante = investido + dividendos
        meses += 1

        # Verifica se atingiu o marco de R$ 100.000,00
        if bateu_100k is None and montante >= 100000:
            bateu_100k = (meses // 12, meses % 12, investido, dividendos, montante)

        # Verifica se atingiu o marco de R$ 1.000.000,00
        if bateu_1m is None and montante >= 1000000:
            bateu_1m = (meses // 12, meses % 12, investido, dividendos, montante)

        # Verifica se atingiu ambos os marcos
        if bateu_100k and bateu_1m:
            print(f"100k: {bateu_100k[0]} anos e {bateu_100k[1]} meses, Investido: R${bateu_100k[2]:.2f}, Div: R${bateu_100k[3]:.2f}, Total: R${bateu_100k[4]:.2f}")
            print(f"1M: {bateu_1m[0]} anos e {bateu_1m[1]} meses, Investido: R${bateu_1m[2]:.2f}, Div: R${bateu_1m[3]:.2f}, Total: R${bateu_1m[4]:.2f}")
            print(f"Quantidade de cotas: {cotas:.2f}")
            return

    # Verifica se atingiu o número máximo de meses
    print(f"Terminado após {max_meses} meses.")
    if bateu_100k:
        print(f"100k: {bateu_100k[0]} anos e {bateu_100k[1]} meses, Investido: R${bateu_100k[2]:.2f}, Div: R${bateu_100k[3]:.2f}, Total: R${bateu_100k[4]:.2f}")
    if bateu_1m:
        print(f"1M: {bateu_1m[0]} anos e {bateu_1m[1]} meses, Investido: R${bateu_1m[2]:.2f}, Div: R${bateu_1m[3]:.2f}, Total: R${bateu_1m[4]:.2f}")
    print(f"Quantidade de cotas: {cotas:.2f}")

# Chamar a função
print("AÇÕES")
acoes()