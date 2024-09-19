
from interface import Criacao_Conta

class Cliente():
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []
        
    def get_contas(self, _contas):
        for line in _contas:
            return _contas
        
    def realizar_transacao(self, conta, transacao):
        pass
        
    def adicionar_conta(self, conta):
        self._contas.append(conta)
        pass
        
    def set_endereco(self, endereco):
        pass



