menu = """
    [ 1 ] - DEPÓSITO
    [ 2 ] - SAQUE
    [ 3 ] - EXTRATO
    [ 0 ] - SAIR
    
    Digite a opção desejada: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

atendimento_banco = " AUTO-ATENDIMENTO HGMS "

print("=" * 34)
print(atendimento_banco.center(34, "="))
print("=" * 34)

while True:

    opcao = int(input(menu))

    if opcao == 1:
        print()
        print("=" * 34)
        print(f'{" DEPÓSITO ".center(34, "=")}')
        print()
        valor = float(input("Informe o valor do depósito:\n"
                            "R$ "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

        print()
        print(f'{" OPERAÇÃO FINALIZADA ".center(34, "=")}')
        print("=" * 34)

    elif opcao == 2:
        print()
        print("=" * 34)
        print(f'{" SAQUE ".center(34, "=")}')
        print()
        valor = float(input("Informe o valor do saque:\n"
                            "R$ "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\nOperação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("\nOperação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("\nOperação falhou! Limite de saque diário excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

        print()
        print(f'{" OPERAÇÃO FINALIZADA ".center(34, "=")}')
        print("=" * 34)

    elif opcao == 3:
        print()
        print("=" * 34)
        print(f'{" EXTRATO ".center(34, "=")}')
        print()

        print("Não foram realizadas movimentações.\n" if not extrato else extrato)
        print(f'Saldo R$ {saldo:.2f}')

        print()
        print(f'{" OPERAÇÃO FINALIZADA ".center(34, "=")}')
        print("=" * 34)

    elif opcao == 0:
        print()
        print("=" * 34)
        print(f'{" ATENDIMENTO FINALIZADO ".center(34, "=")}')
        print("=" * 34)
        print()
        break

    else:
        print("Opção inválida, selecione novamente a opção desejada.")

print("OBRIGADO POR UTILIZAR NOSSO SISTEMA DE AUTO-ATENDIMENTO!")
