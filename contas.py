class ContaBancaria:
    def __init__ (self, nome, cpf, saldo):
        self.nome = nome
        self.numero = cpf
        self.saldo = saldo

#função sacar vai verificar se o cliente tem saldo suficiente
#e vai retornar um valor True ou False, se o valor do saque for
#menor que o valor disponivel em conta, ele da errado e manda repetir

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            print("Saldo indisponivel, tente novamente...")
            return False

#função saldo imprime o saldo atual
        
    def ver_saldo(self):
        print("Saldo disponível: R$ %.2f" %self.saldo)

#função deposito insere o valor informado no saldo atual
        
    def depositar(self, valor):
        self.saldo += valor

#função tranferencia vai sacar de uma conta e depositar em outra, então ele puxa
#a função de sacar, verifica se o valor é True, ou seja, se tem a quantia em
#conta disponivel, e realiza o saque, se não, geraerro pois o valor é insuficiente
        
    def transferir(self, destino, valor):
        if self.sacar(valor) == True:
            destino.depositar(valor)
        else:
            print("ERRO, valor insuficiente!")

            
