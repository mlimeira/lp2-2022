from abstratas.autenticavel import Autenticavel
from funcionario import Funcionario


class Presidente(Funcionario, Autenticavel):
    def __init__(self, nome, cpf, salario):
        super().__init__(nome, cpf, salario)

    # Implementação do Método Abstrato
    def bonificacao(self):
        return 2000

    def autentica(self, valor):
        if self._senha == valor+'123':
            return True
        else:
            return False
