from conta import Conta

class conta_corrente(Conta):
    def __init__(self, numero, cliente):
        super().__init__(numero, cliente)
        self._numero = numero
        self._cliente = cliente
        
    
    def get_limite(self):
        return self._limite
        
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """