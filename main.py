from contas import ContaBancaria

#Contas cadastradas no programa:
Conta1 = ContaBancaria("Vinicius", 1, 200)
Conta2 = ContaBancaria("João", 2, 300)



error = "Você digitou algo errado!"
menu = 0 #valor inicial do menu é 0 e é alterado na escolha
while menu !=5:
    print('''Bem Vindo ao Branco!
o que deseja fazer?
[ 1 ] Depositar 
[ 2 ] Ver saldo
[ 3 ] Realizar saque
[ 4 ] Realizar tranferencia
[ 5 ] Sair''')
    menu = int(input("Digite aqui: "))

    if menu == 1:
      conta = 0
      conta = int(input("Digite o numero da conta: (1/2)"))
      if conta == 1:
        valor = int(input("Valor a depositar: "))
        Conta1.depositar(valor)
      elif conta == 2:
        valor = int(input("Valor a depositar: "))
        Conta2.depositar(valor)
      else:
        print(error)
        
    elif menu == 2:
      conta = 0
      conta = int(input("Digite o numero da conta: (1/2)"))
      if conta == 1:
        Conta1.ver_saldo()
      elif conta == 2:
        Conta2.ver_saldo()
      else:
        print(error)
        
    elif menu == 3:
      conta = 0
      conta = int(input("Digite o numero da conta: (1/2)"))
      if conta == 1:
        saque = int(input("Valor a sacar: "))
        Conta1.sacar(saque)
      elif conta == 2:
        saque = int(input("Valor a sacar: "))
        Conta2.sacar(saque)
      else:
        print(error)
        
    elif menu == 4:
      conta = 0
      conta = int(input("Digite o numero da conta: (1/2)"))
      if conta == 1:
        valor = int(input("Valor a transferir: "))
        transf = 0
        transf = int(input("Digite o numero da conta que deseja tranferir: (2)"))
        if transf == 2:
          Conta1.transferir(Conta2, valor)
        else:
          print(error)
      elif conta == 2:
        valor = int(input("Valor a transferir: "))
        transf = 0
        transf = int(input("Digite o numero da conta que deseja tranferir: (1)"))
        if transf == 1:
          Conta2.transferir(Conta1, valor)
        else:
          print(error)
      else:
        print(error)
    elif menu == 5:
        print('Finalizando...')
    else:
        print("Opção invalida, tente novamente!")
    print('=-=' * 10)
print("Fim do programa!")





