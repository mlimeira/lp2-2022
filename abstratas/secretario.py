from funcionario import Funcionario


class Secretario(Funcionario):
    def __init__(self, nome, cpf, salario):
        super().__init__(nome, cpf, salario)

    #A implementação do método abstrato na classe filha
    #é obrigatório
    def bonificacao(self):
        return 10