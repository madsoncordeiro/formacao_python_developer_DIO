# -*- coding: utf-8 -*-
"""
Objetivo Geral:
    Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.

Desafio:
    Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a
    linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

Operação de Depósito:
    Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, essa forma não precisamos
    nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na
    operação de extrato.

Operação de Saque:
    O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve
    exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e
    exibidos na operação de extrato.

Operação de Extrato:
    Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato
    estiver em branco, exibir a mensagem: Não foram realizadas movimentações. Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
    1500.45 = R$ 1500.45



"""

menu = """

========================MENU===============================

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

===========================================================
"""


saldo = float(0)
limite = float(500)
extrato = ""
numero_saques = int(0)
LIMITE_SAQUES = int(3)
saque = float(0)

while 1 == 1:
    usuario_menu = input(menu)
    if usuario_menu == "d":
        deposito = float(input("\nQuanto você deseja depositar em sua conta? \n"))
        if deposito > 0:
            saldo += deposito
            extrato += f"\nDepósito efetuado: R${deposito:.2f}. \n"
        else:
            print("\nVocê informou um valor negativo. \n")
    elif usuario_menu == "s":
        saque = float(input("\nQuanto você quer sacar? \n"))
        saque_maior_que_saldo = saque > saldo
        valor_a_sacar_maior_que_limite = saque > limite
        quantidade_saque_maior_que_limite = numero_saques >= LIMITE_SAQUES

        if saque_maior_que_saldo:
            print("\nVocê não tem dinheiro suficiente em sua conta. \n")
        elif valor_a_sacar_maior_que_limite:
            print("\nVocê só pode sacar até R$500,00. \n")
        elif quantidade_saque_maior_que_limite:
            print("\nVocê só pode realizar até 3 saques diariamente. \n")
        elif saque > 0:
            saldo -= saque
            extrato += f"\nSaque realizado: R${saque:.2f}. \n"
            numero_saques += 1
        else:
            print("\nO valor que você informou é inválido. \n")
    elif usuario_menu == "e":
        print("================ EXTRATO ================")
        print("\nNão foram realizadas movimentações.\n" if not extrato else extrato)
        print(f"\nSaldo restante: R$ {saldo:.2f}.\n ")
        print("==========================================")
    elif usuario_menu == "q":
        break
    else:
        print("\nVocê realizou uma operação inválida. Escolha uma das alternativas disponíveis no menu. \n")