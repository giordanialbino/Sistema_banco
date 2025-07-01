'''Sistema Bancario dépositos valores Positivos e salvos numa variavel para posterior exibição 
no extrato.
Saque 3 saques diários com limite máximo de 500 reais por saque, caso não tenha saldo em conta 
deve exibir uma msg que não foi possivel realizar o saque por falta de saldo salvos numa variavel
para exibir num extrato
Extrato listar todos os depositos e saques e no final o saldo atual da conta deve ser exibido o 
formato R$ XXXX.XX
'''
menu = """
Selecione a opção que deseja realizar: 

    [d] Depositar
    [s] Saque
    [e] Extrato
    [q] Sair

    =>  """
from datetime import datetime


saldo = 0
limite = 500
extrato = ""
numeros_saques = 1
LIMITE_SAQUES = 3
data = datetime.now()

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Favor digite o valor que deseja depositar: "))
    
        if deposito <= 0:

            print("Favor digite um valor Maior que 0.")
        
        else:
            saldo += deposito

            extrato += f"{data.now().strftime('%d/%m/%Y %H:%M')} Deposito no valor: {deposito:.2f} \n"
            print(f"Deposito realizado com sucesso no valor de R$ {deposito:.2f}, seu saldo ficou R$ {saldo:.2f}")
            
    
    elif opcao == "s":

        saque = float(input("Digite o valor que deseja Sacar: "))
        
        if numeros_saques > LIMITE_SAQUES or saque > limite:
            
            if numeros_saques > LIMITE_SAQUES:
            
                print(f"Voce excedeu o numero de {LIMITE_SAQUES} saques por dia.")
            
            elif saque > limite:

                print(f"Não foi possivel sacar R$ {saque:.2f}, valor limite é de R$ {limite:.2f} por saque.")
        
        else:
            if saque > saldo:
                print(f"Não possível relizar o saque no valor de R$ {saque}, seu saldo é de R$ {saldo}.")
            else:
                numeros_saques += 1
                saldo -= saque
                extrato += f"{data.now().strftime('%d/%m/%Y %H:%M')} Saque no valor de R$ {saque:.2f} \n"            
                print(f"Saque no valor de R$ {saque:.2f} realizado com sucesso. Seu saldo atual é de R$ {saldo:.2f}")

    elif opcao == "e":

        print(extrato)
        print(f"{data.now().strftime('%d/%m/%Y %H:%M')} Seu saldo é de R$ {saldo:.2f}")

    elif opcao == "q":
        break
    
    else:

        print("Operação inválida, por favor selecione novamente a operação desejada.")