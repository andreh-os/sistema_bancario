from datetime import datetime
from datetime import date

menu = """

Selecione a operação:

[d] - Deposíto
[s] - Saque
[e] - Extrato
[q] - Sair

"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
while True:
    opcao = input(menu)
    if opcao == 'd':
        deposito = float(input("Digite o valor do depósito: "))
        if deposito > 0:
            saldo += deposito
            operacoes = f"{datetime.now()} Depósito realizado no valor de R$ {deposito:.2f} \n"
            print(operacoes)
            extrato += operacoes
        else:
            print(f"Valor inválido, tente novamente.")
    elif opcao == 's':
        saque = float(input("Digite o valor do saque: "))
        if numero_saques < LIMITE_SAQUES:
            if saque > saldo:
                print(f"Saldo insuficiente, tente novamente.")
            elif saque > 500:
                print(f"Limite máximo atingido, tente novamente.")
            else:
                saldo -= saque
                operacoes = f"{datetime.now()} Saque realizado no valor de R$ {saque:.2f} \n"
                print(operacoes)
                extrato += operacoes       
                numero_saques += 1
        else:
            print("Limite de saques atingido.")
    elif opcao == 'e':
        print(extrato)
        print(f"Seu saldo é de: R$ {saldo}")
    elif opcao == 'q':
        break
    else:
        print("Opção inválida, tente novamente.")
    