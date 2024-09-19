from cliente import Cliente
from conta import Conta
class pessoa_fisica(Cliente):
   def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf



pessoa = pessoa_fisica("Luiz", "03/03/2023",56460951829, "av santa fé")
conta1 = Conta(1,f"{pessoa.nome} {pessoa.cpf}")

pessoa.adicionar_conta(conta1)

print(pessoa._contas)

