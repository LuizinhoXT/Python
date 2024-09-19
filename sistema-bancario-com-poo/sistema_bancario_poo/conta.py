from historico import Historico
class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agenciac = "0001"
        self._cliente = cliente
        self._historico = Historico()
    
    def get_saldo(self):
        return self._saldo
    
    def set_saldo(self, num):
        self._saldo = num
    
    def nova_conta(self, cliente, numero):
        conta = "conta"
        return conta
    
    def sacar(self, valor):
        saldo = self._saldo
        saldo_insuficiente = valor > self._saldo
        
        if saldo_insuficiente:
            print("@@@ Erro: saldo insuficiente.\n Deseja consultar o saldo? [s, n]")
            var = str(input())
            if var == "s":
                print(f">>> Saldo Atual: R$ {self.get_saldo()}")
                     
            return False
        else:
            self.set_saldo(saldo - valor) 
            
        return False
             
    def depositar(self, valor):
        self._saldo += valor
        
        return True
        


