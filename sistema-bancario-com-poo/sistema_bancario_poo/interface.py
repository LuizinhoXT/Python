from abc import ABC, abstractclassmethod, abstractproperty


class Transacao(ABC):
    @property
    @abstractproperty
    def receber_dado(self):
        pass

    @abstractclassmethod
    def registrar_transação(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor) :
        super().__init__()
        self._valor = valor
        self._tipo - "Saque"

    
    def valor(self, valor):
        return valor
    
    def registrar_transação(self, conta):
        return self.tipo, self.valor, conta
    
class Deposito(Transacao):
    def __init__(self, valor) :
        super().__init__()
        self._valor = valor
        self._tipo - "deposito"

    
    def registrar_dado(self, valor):
        return valor
    
    def registrar_transação(self, conta):
        return self.tipo, self.valor, conta
    
class Criacao_Conta():
    def __init__(self, valor) :
        super().__init__()
        self._valor = valor
        self._tipo = "Criação"

 
    def registrar_dado(self, valor):
        return valor
    
    def registrar_transação(self, conta):
        return conta