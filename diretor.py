from funcionario import Funcionario

class Diretor(Funcionario):
    def __init__(self, nome, cpf, salario, cod_diretor):
        super().__init__(nome, cpf, salario)
        self._cod_diretor = cod_diretor

    def bonificacao(self):
        return super().bonificacao() + self._salario * 0.2
