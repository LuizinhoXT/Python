class Historico:
    transacoes = []
    
    def registrar_transacao(self, nova_transacao):
        self.transacoes.append(nova_transacao)
        return True