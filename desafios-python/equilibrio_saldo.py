# Em uma análise inicial, foi identificado pela equipe financeira a necessidade de desenvolver uma solução que permita ao cliente equilibrar seu saldo bancário. Dessa forma, o programa deve solicitar uma entrada que representa o saldo atual do funcionário, e após, seja informado o valor de duas transações, sendo elas: um depósito e um saque. O programa deve atualizar o saldo com base nas transações e exibir o saldo final.


saldo_atual = float(input())
valor_deposito = float(input())
valor_retirada = float(input())

saldo_atualizado = ((saldo_atual + valor_deposito) - valor_retirada)

print(f"Saldo atualizado na conta: {saldo_atualizado:.1f}")
