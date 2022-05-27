from funcionario import Funcionario

class Diretor(Funcionario):
    def __init__(self, nome, cpf, salario, cod_diretor, senha):
        super().__init__(nome, cpf, salario)
        self._cod_diretor = cod_diretor
        self._senha = senha

    def __str__(self):
        return self.get_nome()

    # Implementação do Método Abstrato
    def bonificacao(self):
        return self._salario * 0.2

    def autentica(self, valor):
        if self._senha == valor:
            return True
        else:
            return False