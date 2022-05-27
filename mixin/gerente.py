from autenticavel import AutenticavelMixin
from funcionario import Funcionario

class Gerente(Funcionario, AutenticavelMixin):
    def __init__(self, nome, cpf, salario, senha):
        super().__init__(nome, cpf, salario)
        self._senha = senha

    #Implementação do Método Abstrato
    def bonificacao(self):
        return 500

    def autentica(self, valor):
        if self._senha == valor:
            return True
        else:
            return False
